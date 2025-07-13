from decimal import Decimal
from sqlmodel import SQLModel, Field

class Province(SQLModel, table=True):
    __tablename__ = "provinces"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    type: str = Field(index=True)  # e.g., "primary", "secondary"
    price: Decimal
