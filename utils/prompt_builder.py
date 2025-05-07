from models.schemas import ProgramRequest

def build_prompt(data: ProgramRequest) -> str:
    return f"""
Create a {data.numberOfWeeks}-week fitness program called "{data.programName}". This program should follow the {data.trainingModality} training style and is designed for someone at the {data.difficultyLevel} level.

The primary focus of this program is {data.primaryFocus}, with a secondary focus on {data.secondaryFocus}. The user will train {data.daysPerWeek} days per week, with each session lasting around {data.sessionDuration} minutes.

Each workout should include exactly {data.exercisesPerDay} exercises and a total of {data.setsPerDay} sets per day.

The workouts will be performed at {data.location}, and the available equipment includes: {data.equipmentList}.

Use the following training intensifiers where applicable: {data.intensifiersUsed}.

Do you want the program to progressively get more challenging each week? {data.wantProgression}.

Please structure the program clearly by week and day. Label each circuit using letters (A, B, C, etc.), and label exercises within each circuit using A1, A2, B1, etc.
"""

def build_prompt_from_dict(data: dict) -> str:
    return f"""
Create a {data['numberOfWeeks']}-week fitness program called "{data['programName']}". This program should follow the {data['trainingModality']} training style and is designed for someone at the {data['difficultyLevel']} level.

The primary focus of this program is {data['primaryFocus']}, with a secondary focus on {data['secondaryFocus']}. The user will train {data['daysPerWeek']} days per week, with each session lasting around {data['sessionDuration']} minutes.

Each workout should include exactly {data['exercisesPerDay']} exercises and a total of {data['setsPerDay']} sets per day.

The workouts will be performed at {data['location']}, and the available equipment includes: {data['equipmentList']}.

Use the following training intensifiers where applicable: {data['intensifiersUsed']}.

Do you want the program to progressively get more challenging each week? {data['wantProgression']}.

Please structure the program clearly by week and day. Label each circuit using letters (A, B, C, etc.), and label exercises within each circuit using A1, A2, B1, etc.
"""

