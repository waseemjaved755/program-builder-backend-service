from fastapi import APIRouter, Request
from models.schemas import ProgramRequest, ProgramUpdate
from services.program_service import (
    generate_program_response,
    get_program_from_firebase,
    update_program_in_firebase
)

router = APIRouter()

@router.post("/generate")
async def generate_program(data: ProgramRequest, request: Request):
    return await generate_program_response(data)

@router.get("/{user_id}")
async def fetch_saved_program(user_id: str):
    result = get_program_from_firebase(user_id)
    return result if result else {"error": "Program not found"}

@router.patch("/{user_id}")
async def patch_program(user_id: str, data: ProgramUpdate):
    update_program_in_firebase(user_id, data.dict(exclude_unset=True))
    return {"message": "Program updated"}