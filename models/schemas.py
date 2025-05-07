from pydantic import BaseModel
from typing import Optional

class ProgramRequest(BaseModel):
    user_id: str
    numberOfWeeks: str
    programName: str
    trainingModality: str
    difficultyLevel: str
    primaryFocus: str
    secondaryFocus: str
    daysPerWeek: str
    sessionDuration: str
    exercisesPerDay: str
    setsPerDay: str
    location: str
    equipmentList: str
    intensifiersUsed: str
    wantProgression: str

class ProgramUpdate(BaseModel):
    numberOfWeeks: Optional[str] = None
    programName: Optional[str] = None
    trainingModality: Optional[str] = None
    difficultyLevel: Optional[str] = None
    primaryFocus: Optional[str] = None
    secondaryFocus: Optional[str] = None
    daysPerWeek: Optional[str] = None
    sessionDuration: Optional[str] = None
    exercisesPerDay: Optional[str] = None
    setsPerDay: Optional[str] = None
    location: Optional[str] = None
    equipmentList: Optional[str] = None
    intensifiersUsed: Optional[str] = None
    wantProgression: Optional[str] = None
