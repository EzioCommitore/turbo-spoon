from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class UserPhysicalAddress(Base):
    __tablename__ = "user_physical_address"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,)
    address: Mapped[str] = mapped_column(String(35), nullable=False,)
    city: Mapped[str] = mapped_column(String(15), nullable=False,)
    state: Mapped[str] = mapped_column(String(2), nullable=False,)
    zip: Mapped[str] = mapped_column(String(5), nullable=False,)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
