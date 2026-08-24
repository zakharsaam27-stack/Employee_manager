from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.user_role import User_role

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_pass: Mapped[str]

    employee: Mapped["Employee"] = relationship("Employee",
        back_populates="user")
    user_roles: Mapped[list["User_role"]] = relationship(
        "User_role", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"
