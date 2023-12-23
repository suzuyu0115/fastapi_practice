from sqlalchemy import Column, ForeignKey, Integer, String, Datetime
from .database import Base

class User(Base):
  __tablename__ = 'users'
  user_id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)

class Room(Base):
  __tablename__ = 'rooms'
  room_id = Column(Integer, primary_key=True, index=True)
  room_name = Column(String, unique=True, index=True)
  capacity = Column(Integer)

class Booking(Base):
  __tablename__ = 'bookings'
  booking_id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
  room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='SET NULL'), nullable=False)
  booked_num = Column(Integer)
  start_date_time = Column(Datetime, nullable=False)
  end_date_time = Column(Datetime, nullable=False)