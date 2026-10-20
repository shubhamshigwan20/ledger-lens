from fastapi import APIRouter
from routers import auth, reports, transactions

router = APIRouter()

router.include_router(auth.router)
router.include_router(transactions.router)
router.include_router(reports.router)