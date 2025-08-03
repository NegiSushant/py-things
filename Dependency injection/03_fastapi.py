from fastapi import FastAPI, Depends # type: ignore

app = FastAPI()

class Database:
    def connect(self):
        return "Database connected successfully.....!"
    
    def disconnect(self):
        return "Database disconnected successfully....!"
    
def get_database():
    db = Database()

    try:
        yield db
    finally:
        db.disconnect()



@app.get('/dbconnect')
def red_db(db=Depends(get_database)):
    return {"message": "Hello from red_db functions....!"}
