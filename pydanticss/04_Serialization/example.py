from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime(
                '%d-%m-%Y %H:%M:%S'
            )
        }
    )

# Creating a user instance
user = User(
    id = 1,
    name = "Sushant Singh Negi",
    email= "something@email.com",
    createAt=datetime(2024, 3, 15, 14, 30),
    address= Address(
        street = "Something",
        city = "Nainital",
        zip_code = "202101"
    ),
    is_active= True,
    tags=['premium', 'subscriber']
)

# serializations
# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)

print('**'*25)
# Using model_dump_json()
json_str = user.model_dump_json()
print(json_str)