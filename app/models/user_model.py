from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .reservation_model import Reservation

class User(SQLModel , table=True):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    username: str = Field(index=True, unique=True)
    password: str = Field(index=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    phone: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    user_reservations: list["Reservation"] = Relationship(back_populates="user")
