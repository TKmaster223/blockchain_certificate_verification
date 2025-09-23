from fastapi import APIRouter, Depends
from backend.schemas import CertificateCreate, CertificateOut
from backend.db import db
from backend.auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/certificates", tags=["Certificates"])

@router.post("/", response_model=CertificateOut)
async def issue_certificate(cert: CertificateCreate, user: dict = Depends(get_current_user)):
    cert_data = cert.dict()
    cert_data["issued_on"] = datetime.utcnow().isoformat()
    cert_data["is_valid"] = True
    await db.certificates.insert_one(cert_data)
    return cert_data

@router.get("/{cert_id}", response_model=CertificateOut)
async def verify_certificate(cert_id: str):
    cert = await db.certificates.find_one({"cert_id": cert_id})
    if not cert:
        return {"error": "Certificate not found"}
    return cert
