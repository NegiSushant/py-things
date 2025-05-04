class Database:
    def connect(self):
        return "Connect to database!"
    
class Service:
    # dependency injection
    def __init__(self, db: Database):
        self.db = db

    def get_data(self):
        return self.db.connect()
    

# Usage
db = Database()
service = Service(db)

print(service.get_data())
