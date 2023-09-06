from typing import List
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,)
    user_contact_info_ids: Mapped[List[int]] = mapped_column(ForeignKey("user_contact_info.id"), nullable=False,)
    user_physical_address_id: Mapped[int] = mapped_column(ForeignKey("user_physical_address.id"), nullable=False,)
    active: Mapped[bool] = mapped_column(default=False, nullable=False,)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False,)
    middle_name: Mapped[str] = mapped_column(String(30), nullable=True,)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False,)
    password: Mapped[str] = mapped_column(String(64))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
