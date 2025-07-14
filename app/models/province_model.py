from decimal import Decimal
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

from ..schemas.province_schema import ProvinceType

if TYPE_CHECKING:
    from .reservation_model import Reservation

class Province(SQLModel, table=True):
    __tablename__ = "provinces"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    type: ProvinceType = Field(sa_column_kwargs={"type_": ProvinceType}, index=True)
    price: Decimal

    # Relationships
    reservations: list["Reservation"] = Relationship(back_populates="province")
