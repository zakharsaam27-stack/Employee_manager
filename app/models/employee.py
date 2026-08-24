from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.department import Department
    from app.models.job_title import Job_title


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        ForeignKey(column="users.id"), primary_key=True)
    full_name: Mapped[str]
    department_id: Mapped[int] = mapped_column(
        ForeignKey(column="departments.id"))
    job_title_id: Mapped[int] = mapped_column(
        ForeignKey(column="job_titles.id"))

    user: Mapped["User"] = relationship(
        "User", back_populates="employee")
    department: Mapped["Department"] = relationship(
        "Depatment", back_populates="employees")
    job_title: Mapped["Job_title"] = relationship(
        "Job_title", back_populates="employees")
    
    def __repr__(self) -> str:
        return f"Employee(id={self.id!r}, full_name={self.full_name!r}, department_id={self.department_id!r}, job_title_id={self.job_title_id!r})"
