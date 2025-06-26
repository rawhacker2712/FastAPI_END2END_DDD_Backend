from pydantic import BaseModel, EmailStr


class EmployeeCreateDTO(BaseModel):
    name: str
    email: EmailStr
  

class EmployeeUpdateDTO(BaseModel):
    name: str
    email: EmailStr

class EmployeeOutDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    


    model_config = {
        "from_attributes": True
    }