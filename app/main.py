from fastapi import FastAPI
from .routers import surat, notim, spt, sppd, rincian, kendali

app = FastAPI(
    title="Format Kantor API",
    version="1.0.0"
)

# Register Routers
app.include_router(surat.router)
app.include_router(notim.router)
app.include_router(spt.router)
app.include_router(sppd.router)
app.include_router(rincian.router)
app.include_router(kendali.router)

@app.get("/")
def home():
    return {"message": "Format Kantor API is running"}
