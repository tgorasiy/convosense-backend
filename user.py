from pydantic import BaseModel, EmailStr
from typing import Literal


class UserOut(BaseModel):
id: str
email: EmailStr
name: str
role: Literal["customer","agent","admin"]