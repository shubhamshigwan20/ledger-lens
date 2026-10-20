from decimal import Decimal
from pydantic import BaseModel, Field

class PreferenceItem(BaseModel):
    key: str 
    value: str

class CategoryItem(BaseModel):
    name: str
    monthly_budget: Decimal | None = Field(gt=0, default=None)

class RegisterReq(BaseModel):
    email: str = Field(min_length=2, max_length=250)
    password: str = Field(min_length=6, max_length=20)
    full_name: str = Field(min_length=2, max_length=150)
    preferences: list[PreferenceItem]
    categories: list[CategoryItem]


class CategoryResponse(BaseModel):
    id: int
    monthly_budget: Decimal | None


class RegisterResponse(BaseModel):
    id: int
    email: str
    full_name: str
    preferences: dict[str, str]
    categories: dict[str, CategoryResponse]
