# models/facility.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Facility(Base):
    __tablename__ = 'facilities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    capacity = Column(Integer)  # 최대 수용 인원 추가
    park_id = Column(Integer, ForeignKey('parks.id'))

    park = relationship('Park', back_populates='facilities')
