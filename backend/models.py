from pydantic import BaseModel
from typing import Optional, List

class CertificateModel(BaseModel):
    cert_id: str
    student_name: str
    course_name: str
    institution: str
    issued_on: str
    is_valid: bool = True

class CorrectionModel(BaseModel):
    cert_id: str
    correction_details: str
    timestamp: str
