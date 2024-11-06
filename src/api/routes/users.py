from fastapi import APIRouter
from src.api.object.users import UserRegistration, UserLogin
from src.datalayer.models.user import UserModel
from src.api.exceptions.user_error import login_error_exception

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

@router.post("/login")
async def login(body: UserLogin):

    user = None
    try:
        user = UserModel.filter(email=body.email).first()
    except Exception:
        return login_error_exception()
    
    if user.password != body.password:
        return login_error_exception()

@router.get("/get-users")
async def get_users():
    users = await UserModel.all()
    return {"users": users}