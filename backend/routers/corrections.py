from fastapi import APIRouter, Depends
from backend.schemas import CorrectionCreate, CorrectionOut
from backend.db import db
from backend.auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/corrections", tags=["Corrections"])

@router.post("/", response_model=CorrectionOut)
async def add_correction(correction: CorrectionCreate, user: dict = Depends(get_current_user)):
    correction_data = correction.dict()
    correction_data["timestamp"] = datetime.utcnow().isoformat()
    await db.corrections.insert_one(correction_data)
    return correction_data

@router.get("/{cert_id}", response_model=list[CorrectionOut])
async def get_corrections(cert_id: str):
    corrections = await db.corrections.find({"cert_id": cert_id}).to_list(100)
    return corrections
