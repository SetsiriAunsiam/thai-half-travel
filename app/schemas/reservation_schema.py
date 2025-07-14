from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

from ..schemas.province_schema import ProvinceResponse

class ReservationBase(BaseModel):
    user_id: int
    province_id: int
    reserved_price: Decimal
    check_in: datetime
    check_out: datetime

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(BaseModel):
    reserved_price: Optional[Decimal] = None
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None

class ReservationResponse(ReservationBase):
    id: int
    reserved_at: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            Decimal: lambda v: str(v)  # Convert Decimal to string for JSON serialization
        }
        