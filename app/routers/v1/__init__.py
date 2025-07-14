from fastapi import APIRouter


from . import (
    auth_router,
    user_router,
    province_router,
    reservation_router,
    )

router = APIRouter(prefix="/v1")
router.include_router(auth_router.router)
router.include_router(user_router.router)
router.include_router(province_router.router)
router.include_router(reservation_router.router)