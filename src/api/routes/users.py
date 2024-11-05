from fastapi import APIRouter
from src.api.object.users import UserRegistration
from src.datalayer.models.user import UserModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post('/register')
async def register(body: UserRegistration):
    user = await UserModel.create(
        name = body.name,
        email = body.email,
        password = body.password
    )
    return {'created': user} 