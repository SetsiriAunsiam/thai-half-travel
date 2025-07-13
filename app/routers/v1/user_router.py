from fastapi import APIRouter, Depends, HTTPException

from ...models.user_model import User
from ...schemas.user_schema import UserCreate, UserResponse
from ...database import SessionDep
from sqlmodel import Session, select
from ...auth.authentication import get_current_user

router = APIRouter(tags=["user"])


@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, session: Session = Depends(SessionDep)):
    statement = select(User).where((User.email == user.email) | (User.username == user.username))
    result = session.exec(statement).first()
    if result:
        raise HTTPException(status_code=400, detail="Email or username already exists")

    db_user = User(
        email=user.email,
        username=user.username,
        password=user.password,  # In a real application, ensure to hash the password
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, session: Session = Depends(SessionDep)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user