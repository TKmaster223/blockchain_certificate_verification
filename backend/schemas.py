from pydantic import BaseModel
from typing import List

class CertificateCreate(BaseModel):
    cert_id: str
    student_name: str
    course_name: str
    institution: str

class CertificateOut(BaseModel):
    cert_id: str
    student_name: str
    course_name: str
    institution: str
    issued_on: str
    is_valid: bool

class CorrectionCreate(BaseModel):
    cert_id: str
    correction_details: str

class CorrectionOut(BaseModel):
    cert_id: str
    correction_details: str
    timestamp: str
