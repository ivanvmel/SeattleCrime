from sqlalchemy import Column, Integer, String, Date, Float
from database import Base

class Crime(Base):
    __tablename__ = 'crime'
    id = Column(Integer, primary_key=True)
    description = Column(String(128), index=True)
    date = Column(Date, index=True)
    longitude = Column(Float(Precision=64), index=True)
    latitude = Column(Float(Precision=64), index=True);
    
    def __init__(self, description=None,date=None,longitude=None,latitude=None):
        self.description = description
        self.date = date
        self.longitude = longitude
        self.latitude = latitude
    
    def __repr__(self):
        return '<Description %r Date %r Longitude %r Latitude %r>' % (self.description) % (self.date) % (self.longitude) % (self.latitude)