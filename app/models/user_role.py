from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from app.models.role import Role
    from app.models.user import User

class User_role(Base):
    __tablename__ = "user_roles"
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)
    
    role: Mapped["Role"] = relationship(
        "Role", back_populates="user_roles")
    user: Mapped["User"] = relationship(
        "User", back_populates="user_roles")