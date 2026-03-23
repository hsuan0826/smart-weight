from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional

# Schema for user registration input
class UserCreate(BaseModel):
    email: str
    password: str
    first_name: str
    gender: Optional[str] = None
    last_name: str
    dob: date
    initial_wt: float
    target_wt: float
    height: float

# Schema for user weight log input
class WeightLogCreate(BaseModel):
    weight: float
    time_of_day: str
    date: date

# Schema for user log in input
class UserLogIn(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    class Config:
        from_attributes = True
    user_id: int
    created_at: datetime
    bio: Optional[str] = None
    gender: Optional[str] = None
    email: str
    first_name: str
    last_name: str
    dob: date
    initial_wt: float
    target_wt: float
    height: float


