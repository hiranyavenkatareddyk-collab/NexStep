from datetime import date
from sqlalchemy.orm import Mapped,mapped_column
from app.models.base import Base

class Student(Base):
    __tablename__='student'
    student_id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]
    date_of_birth: Mapped[date]
    nationality: Mapped[str]
    state: Mapped[str]
    gender: Mapped[str]