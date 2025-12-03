# ===========================
# app/routers/surat.py
# ===========================
from fastapi import APIRouter

router = APIRouter(
    prefix="/surat",
    tags=["Surat"]
)

@router.get("/")
def surat_home():
    return {"status": "OK", "router": "Surat"}



# ===========================
# app/routers/notim.py
# ===========================
from fastapi import APIRouter

router = APIRouter(
    prefix="/notim",
    tags=["Notim"]
)

@router.get("/")
def notim_home():
    return {"status": "OK", "router": "Notim"}



# ===========================
# app/routers/spt.py
# ===========================
from fastapi import APIRouter

router = APIRouter(
    prefix="/spt",
    tags=["SPT"]
)

@router.get("/")
def spt_home():
    return {"status": "OK", "router": "SPT"}



# ===========================
# app/routers/sppd.py
# ===========================
from fastapi import APIRouter

router = APIRouter(
    prefix="/sppd",
    tags=["SPPD"]
)

@router.get("/")
def sppd_home():
    return {"status": "OK", "router": "SPPD"}



# ===========================
# app/routers/rincian.py
# ===========================
from fastapi import APIRouter

router = APIRouter(
    prefix="/rincian",
    tags=["Rincian"]
)

@router.get("/")
def rincian_home():
    return {"status": "OK", "router": "Rincian"}



# ===========================
# app/routers/kendali.py
# ===========================
from fastapi import APIRouter

router = APIRouter(
    prefix="/kendali",
    tags=["Kendali"]
)

@router.get("/")
def kendali_home():
    return {"status": "OK", "router": "Kendali"}

