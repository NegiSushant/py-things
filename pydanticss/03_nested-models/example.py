from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    adress: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # Self refrencing or self replying
    
Comment.model_rebuild()

address = Address(
    street = "123 Something",
    city= "Nainital",
    postal_code= '201102'
)

user = User(
    id= 1,
    name= 'Sushant',
    adress= address
)

comment = Comment(
    id = 1,
    content='Hey there how are you?',
    replies=[
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply2"),
        Comment(id=4, content="reply3"),
    ]
)