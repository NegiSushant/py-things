from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {'id': 101, 'name':"Sushant", 'is_active': True}
# input_data = {'id': 101, 'name':"Sushant", 'is_active': 'True'} //runsmoothly
# input_data = {'id': '101', 'name':"Sushant", 'is_active': True} // run smoothly
# input_data = {'id': '101a', 'name':"Sushant", 'is_active': True} // give error
# input_data = {'id': 101, 'name':"Sushant", 'is_active': 'shi hai'} // give error

user = User(**input_data)
print(user)