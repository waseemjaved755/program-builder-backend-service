from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from utils.prompt_builder import build_prompt, build_prompt_from_dict
from models.schemas import ProgramRequest
from firebase.client import db
import os
import traceback
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def save_program_to_firebase(user_id: str, program_input: dict, program_output: str):
    data = {
        "inputs": program_input,
        "generated_program": program_output
    }
    db.collection("programs").document(user_id).set(data)

def get_program_from_firebase(user_id: str):
    doc = db.collection("programs").document(user_id).get()
    return doc.to_dict() if doc.exists else None

def update_program_in_firebase(user_id: str, update_data: dict):
    
    nested_update = {f"inputs.{key}": value for key, value in update_data.items()}
    db.collection("programs").document(user_id).update(nested_update)

    updated_doc = get_program_from_firebase(user_id)
    full_inputs = updated_doc.get("inputs")

    try:
        prompt = build_prompt_from_dict(full_inputs)

        model = ChatAnthropic(
            model=os.getenv("ANTHROPIC_MODEL"),
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.7,
            max_tokens=4000,
        )

        response = model.invoke([HumanMessage(content=prompt)])
        db.collection("programs").document(user_id).update({
            "generated_program": response.content
        })

        return {"message": "Program updated and regenerated", "programText": response.content}

    except Exception as e:
        logger.error("Prompt regeneration failed:\n%s", traceback.format_exc())
        return {"error": "Program regeneration failed", "exception": str(e)}

async def generate_program_response(data: ProgramRequest):
    
    logger.info("Anthropic API Key present")
    

    try:
        prompt = build_prompt(data)

        model = ChatAnthropic(
            model=os.getenv("ANTHROPIC_MODEL"),
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.7,
            max_tokens=4000,
        )

        logger.info("Sending prompt to Claude...")
        response = model.invoke([HumanMessage(content=prompt)])
        logger.info("Claude response received.")

        save_program_to_firebase(user_id=data.user_id,program_input=data.dict(exclude={"user_id"}),program_output=response.content)

        return {"user_id": data.user_id, "programText": response.content}

    except Exception as e:
        error_trace = traceback.format_exc()
        logger.error("Claude model invocation failed:\n%s", error_trace)

        return {
            "error": "Claude API invocation failed",
            "exception": str(e),
            "traceback": error_trace
        }