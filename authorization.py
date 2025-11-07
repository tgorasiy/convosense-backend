from pydantic import BaseModel, EmailStr


class Token(BaseModel):
access_token: str
token_type: str = "bearer"


class Login(BaseModel):
email: EmailStr
password: str


class Register(BaseModel):
email: EmailStr
name: str
password: str