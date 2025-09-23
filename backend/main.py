from fastapi import FastAPI
from backend.routers import certificates, corrections

app = FastAPI(title="Blockchain Certificate Verification System")

app.include_router(certificates.router)
app.include_router(corrections.router)

@app.get("/")
def root():
    return {"message": "Certificate Verification API Running"}
