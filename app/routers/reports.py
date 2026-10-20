from fastapi import APIRouter
from utils.dependancies import db_dependancy

router = APIRouter(prefix='/reports')

@router.get('/monthly')
async def monthly_reports():
    return{}


@router.get('/trends')
async def trends_reports():
    return {}