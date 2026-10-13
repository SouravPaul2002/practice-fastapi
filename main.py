from typing import List, Optional

from fastapi import FastAPI, HTTPException, Path
from pydantic import AnyUrl, BaseModel, Field

app= FastAPI()
patients = {
    "P001": {
        "name": "Rahul Sharma",
        "age": 25,
        "gender": "Male",
        "height": 175.0,
        "weight": 70.0,
        "bmi": 22.86,
        "city": "Kolkata",
        "email": "rahul@example.com",
        "married": False,
        "allergies": ["Dust", "Pollen"],
        "website": "https://example.com",
        "blood_group": "O+"
    },
    "P002": {
        "name": "Priya Singh",
        "age": 28,
        "gender": "Female",
        "height": 160.0,
        "weight": 55.0,
        "bmi": 21.48,
        "city": "Delhi",
        "email": "priya@example.com",
        "married": True,
        "allergies": [],
        "website": "https://example.org",
        "blood_group": "A+"
    },
    "P003": {
        "name": "Amit Das",
        "age": 35,
        "gender": "Male",
        "height": 180.0,
        "weight": 85.0,
        "bmi": 26.23,
        "city": "Mumbai",
        "email": "amit@example.net",
        "married": True,
        "allergies": ["Penicillin"],
        "website": "https://example.net",
        "blood_group": "B+"
    },
    "P004": {
        "name": "Sneha Roy",
        "age": 22,
        "gender": "Female",
        "height": 165.0,
        "weight": 58.0,
        "bmi": 21.30,
        "city": "Kolkata",
        "email": "sneha@example.com",
        "married": False,
        "allergies": ["Peanuts"],
        "website": "https://example.com",
        "blood_group": "AB+"
    },
    "P005": {
        "name": "Arjun Patel",
        "age": 45,
        "gender": "Male",
        "height": 172.0,
        "weight": 90.0,
        "bmi": 30.42,
        "city": "Ahmedabad",
        "email": "arjun@example.org",
        "married": True,
        "allergies": [],
        "website": "https://example.org",
        "blood_group": "O-"
    }
}


@app.get("/")
def Hello():
    return {
        "message": "Hello"
    }

@app.get("/patient/{patient_id}")
def getPatient(patient_id: str = Path( description="give Id of the patient", examples="P001")):
    if patient_id in patients:
        return patients[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient Not Found")


sample_patient= {
        "name": "Rahul Sharma",
        "age": 25,
        "gender": "Male",
        "height": 175.0,
        "weight": 70.0,
        "bmi": 22.86,
        "city": "Kolkata",
        "email": "rahul@example.com",
        "married": False,
        "allergies": ["Dust", "Pollen"],
        "website": "https://example.com",
        "blood_group": "O+"
    }

class Patient(BaseModel):
    name: str
    age: int = Field(ge=0, lt=120, description="Enter Age")
    gender: str
    height: float
    weight: float
    bmi: float
    city: Optional[str] = None # None is default
    email: str
    married: bool
    allergies: List[str]
    website: AnyUrl
    blood_group: str

validated_patient= Patient(**sample_patient)
print(validated_patient)