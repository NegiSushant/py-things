 ## TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)
#
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=20, description="Employee Name", example="Sushant Singh Negi")
    department: Optional[str] = 'General'
    # department: Optional[str] = Field(default='General')
    salary: float = Field(..., ge=10000)