from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class UserContactInfo(Base):
    __tablename__ = "user_contact_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,)
    contact_type: Mapped[str] = mapped_column(String(15), nullable=False,)
    value: Mapped[str] = mapped_column(String(20), nullable=False,)
    description: Mapped[str] = mapped_column(String(50), nullable=True,)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
