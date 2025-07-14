from decimal import Decimal
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user_model import User
    from .province_model import Province

class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    province_id: int = Field(foreign_key="provinces.id")
    reserved_at: datetime = Field(default_factory=datetime.now)
    reserved_price: Decimal
    check_in: datetime
    check_out: datetime

    # Relationships
    user: "User" = Relationship(back_populates="user_reservations")
    province: "Province" = Relationship(back_populates="reservations")