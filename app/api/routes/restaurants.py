from fastapi import APIRouter, status

from delivery_api.app.schemas.restaurant import RestaurantCreate, RestaurantResponse

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)

restaurants: list[RestaurantResponse] = []


@router.post(
    "",
    response_model=RestaurantResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_restaurant(
        restaurant_data: RestaurantCreate,
) -> RestaurantResponse:
    restaurant = RestaurantResponse(
        id=len(restaurants) + 1,
        **restaurant_data.model_dump(),
    )
    restaurants.append(restaurant)
    return restaurant
