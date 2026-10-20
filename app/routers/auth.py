from fastapi import APIRouter
from utils.dependancies import db_dependancy
from schemas.auth import RegisterReq, RegisterResponse
from models.users import Users
from models.categories import Categories
from models.budgets import Budgets
from datetime import date
from starlette import status

router = APIRouter(prefix='/auth')


@router.post('/register', response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register_user(req:RegisterReq, db: db_dependancy):
    prefs = {item.key: item.value for item in req.preferences}
    db_user = Users(
        email=req.email,
        hashed_password=req.password,
        full_name=req.full_name,
        preferences=prefs,
    )

    try:
        # Flush assigns the user id without committing a partially-created user.
        db.add(db_user)
        db.flush()

        category_db_rows = [
            Categories(user_id=db_user.id, name=item.name)
            for item in req.categories
        ]
        db.add_all(category_db_rows)
        db.flush()

        first_day = date.today().replace(day=1)
        budget_db_rows = [
            Budgets(
                category_id=category.id,
                monthly_limit=item.monthly_budget,
                effective_from=first_day,
            )
            for category, item in zip(category_db_rows, req.categories)
            if item.monthly_budget is not None
        ]
        db.add_all(budget_db_rows)

        response = {
            'id': db_user.id,
            'email': db_user.email,
            'full_name': db_user.full_name,
            'preferences': prefs,
            'categories': {
                item.name: {
                    'id': category.id,
                    'monthly_budget': item.monthly_budget,
                }
                for category, item in zip(category_db_rows, req.categories)
            },
        }
        db.commit()
    except Exception:
        db.rollback()
        raise

    return response

@router.post('/login')
async def login_user():
    return {}
