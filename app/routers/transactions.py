from fastapi import APIRouter
from utils.dependancies import db_dependancy

router = APIRouter(prefix='/transactions')


@router.post('/import')
async def import_transactions():
    return {}