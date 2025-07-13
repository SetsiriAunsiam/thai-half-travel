from fastapi import APIRouter, Depends, HTTPException

from ...models.province_model import Province
from ...schemas.province_schema import ProvinceCreate, ProvinceResponse
from ...database import SessionDep
from sqlmodel import Session, select
from ...auth.authentication import get_current_user

router = APIRouter(tags=["province"])

@router.post("/provinces/", response_model=ProvinceResponse)
async def create_province(province: ProvinceCreate, session: Session = Depends(SessionDep)):
    statement = select(Province).where(Province.name == province.name)
    result = session.exec(statement).first()
    if result:
        raise HTTPException(status_code=400, detail="Province already exists")

    db_province = Province(
        name=province.name,
        type=province.type,
        price=province.price
    )
    session.add(db_province)
    session.commit()
    session.refresh(db_province)
    return db_province

@router.get("/provinces/{province_id}", response_model=ProvinceResponse)
def get_province(province_id: int, session: Session = Depends(SessionDep)):
    province = session.get(Province, province_id)
    if not province:
        raise HTTPException(status_code=404, detail="Province not found")
    return province