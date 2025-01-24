from pydantic import BaseModel

class UserProfile(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    password: str