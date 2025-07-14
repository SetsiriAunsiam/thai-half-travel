from fastapi import APIRouter, Depends, HTTPException

from ...models.reservation_model import Reservation
from ...schemas.reservation_schema import ReservationCreate, ReservationResponse
from ...database import SessionDep
from sqlmodel import Session, select
from ...auth.authentication import get_current_user

router = APIRouter(tags=["reservation"])

@router.post("/reservations/", response_model=ReservationResponse)
async def create_reservation(reservation: ReservationCreate, session: Session = Depends(SessionDep)):   
    # Check if the user exists
    user = session.get(reservation.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the province exists
    province = session.get(reservation.province_id)
    if not province:
        raise HTTPException(status_code=404, detail="Province not found")

    db_reservation = Reservation(
        user_id=reservation.user_id,
        province_id=reservation.province_id,
        reserved_price=province.price,
        check_in=reservation.check_in,
        check_out=reservation.check_out
    )
    
    session.add(db_reservation)
    session.commit()
    session.refresh(db_reservation)
    return db_reservation

@router.get("/reservations/me", response_model=list[ReservationResponse])
def get_my_reservations(session: Session = Depends(SessionDep), user=Depends(get_current_user)):
    reservations = session.exec(select(Reservation).where(Reservation.user_id == user.id)).all()
    return reservations

@router.get("/reservations/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: int, session: Session = Depends(SessionDep)):
    reservation = session.get(Reservation, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation