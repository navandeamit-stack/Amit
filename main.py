from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# ------------------ DATABASE (in-memory) ------------------
patients = []
doctors = []
appointments = []

# ------------------ MODELS ------------------
class Patient(BaseModel):
    id: int
    name: str
    age: int
    disease: str

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int

# ------------------ HEALTH ------------------
@app.get("/")
def home():
    return {"msg": "Hospital Management API Running"}

# ------------------ PATIENT APIs ------------------

# Add patient
@app.post("/patients")
def add_patient(patient: Patient):
    for p in patients:
        if p.id == patient.id:
            raise HTTPException(status_code=400, detail="Patient already exists")
    
    patients.append(patient)
    return {"msg": "Patient added successfully"}

# Get all patients
@app.get("/patients")
def get_patients():
    return {"patients": patients}

# Get patient by ID
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for p in patients:
        if p.id == patient_id:
            return p
    raise HTTPException(status_code=404, detail="Patient not found")

# Delete patient
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    for p in patients:
        if p.id == patient_id:
            patients.remove(p)
            return {"msg": "Patient deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")

# ------------------ DOCTOR APIs ------------------

# Add doctor
@app.post("/doctors")
def add_doctor(doctor: Doctor):
    for d in doctors:
        if d.id == doctor.id:
            raise HTTPException(status_code=400, detail="Doctor already exists")
    
    doctors.append(doctor)
    return {"msg": "Doctor added successfully"}

# Get all doctors
@app.get("/doctors")
def get_doctors():
    return {"doctors": doctors}

# ------------------ APPOINTMENT APIs ------------------

# Book appointment
@app.post("/appointments")
def book_appointment(appo: Appointment):
    # check patient exists
    patient_exists = any(p.id == appo.patient_id for p in patients)
    if not patient_exists:
        raise HTTPException(status_code=404, detail="Patient not found")

    # check doctor exists
    doctor_exists = any(d.id == appo.doctor_id for d in doctors)
    if not doctor_exists:
        raise HTTPException(status_code=404, detail="Doctor not found")

    appointments.append(appo)
    return {"msg": "Appointment booked successfully"}

# Get all appointments
@app.get("/appointments")
def get_appointments():
    return {"appointments": appointments}