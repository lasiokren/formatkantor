from sqlalchemy import Column, Integer, String
from ..database import Base

class Pegawai(Base):
    __tablename__ = "pegawai"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    nip = Column(String)

