
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Role(Base):
    __tablename__ = "roles"

    __table_args__ = (
        UniqueConstraint(
            "department_id",
            "name",
            name="uq_roles_department_name",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    department: Mapped["Department"] = relationship(
        back_populates="roles",
    )
    employees: Mapped[list["Employee"]] = relationship(
        back_populates="role",
    )
