from typing import TYPE_CHECKING
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.role_permission import Role_permission


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(unique=True)

    role_permissions: Mapped[list["Role_permission"]] = relationship(
        "Role_permission", back_populates="permission")

    def __repr__(self) -> str:
        return f"Permission(id={self.id!r}, action={self.action!r})"
