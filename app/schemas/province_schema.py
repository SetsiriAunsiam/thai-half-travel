from pydantic import BaseModel
from decimal import Decimal

from enum import Enum

class ProvinceType(str, Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

class ProvinceBase(BaseModel):
    name: str
    type: ProvinceType
    price: Decimal = 0.00

class ProvinceCreate(ProvinceBase):
    pass

class ProvinceUpdate(ProvinceBase):
    name: str | None = None
    type: ProvinceType | None = None
    price: Decimal | None = None

class ProvinceResponse(ProvinceBase):
    id: int

    class Config:
        orm_mode = True
        use_enum_values = True  # Use enum values instead of enum names
        json_encoders = {
            Decimal: lambda v: str(v)  # Convert Decimal to string for JSON serialization
        }