from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.role_permission import Role_permission
    from app.models.user_role import User_role


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    role_permissions: Mapped[list["Role_permission"]] = relationship(
        "Role_permission", back_populates="role")
    user_roles: Mapped[list["User_role"]] = relationship(
        "User_role", back_populates="role")

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"
