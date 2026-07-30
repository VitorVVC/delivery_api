from pydantic import BaseModel, Field


class RestaurantCreate(BaseModel):
    name: str = Field(min_length=3, max_length=120)
    category: str = Field(min_length=2, max_length=50)
    delivery_fee: float = Field(ge=0)
    minimum_order: float = Field(ge=0)
    is_open: bool = True


class RestaurantResponse(RestaurantCreate):
    id: int

