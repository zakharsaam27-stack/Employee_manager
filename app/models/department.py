from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.employee import Employee


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    employees: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="department")

    def __repr__(self) -> str:
        return f"Department(id={self.id!r}, name={self.name!r})"
