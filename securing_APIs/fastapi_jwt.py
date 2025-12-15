from fastapi import Request, HTTPException, Body, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from fastapi import FastAPI
import time
import jwt


JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"

users = []


class UserSchema(BaseModel):
    username: str
    password: str


def check_user(data: UserSchema):
    for user in users:
        if user.username == data.username and user.password == data.password:
            return True
    return False


def token_response(token: str):
    return {"access_token": token}


def sign_jwt(user_id: str):
    payload = {"user_id": user_id, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM]
        )
        return (
            decoded_token if decoded_token["expires"] >= time.time() else None
        )
    except Exception:
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code."
            )

    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False

        try:
            payload = decode_jwt(jwtoken)
        except Exception:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


api = FastAPI()


@api.get("/", tags=["root"])
async def read_root():
    """
    Description:
    Cette route renvoie un message "Hello World!".

    Args:
    Aucun argument requis.

    Returns:
    - JSON: Renvoie un JSON contenant un message de salutation.

    Raises:
    Aucune exception n'est levée.
    """

    return {"message": "Hello World!"}


@api.get("/secured", dependencies=[Depends(JWTBearer())], tags=["root"])
async def read_root_secured():
    """
    Description:
    Cette route renvoie un message "Hello World! but secured" uniquement si l'utilisateur est authentifié à l'aide du jeton JWT.

    Args:
    Aucun argument requis.

    Returns:
    - JSON: Renvoie un JSON contenant un message de salutation sécurisé si l'utilisateur est authentifié, sinon une réponse non autorisée.

    Raises:
    - HTTPException(401, detail="Unauthorized"): Si l'utilisateur n'est pas authentifié, une exception HTTP 401 Unauthorized est levée.
    """

    return {"message": "Hello World! but secured"}


@api.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    """
    Description:
    Cette route permet à un utilisateur de s'inscrire en fournissant les détails de l'utilisateur. Elle ajoute ensuite l'utilisateur à la liste des utilisateurs et renvoie un jeton JWT.

    Args:
    - user (UserSchema, Body): Les détails de l'utilisateur à créer.

    Returns:
    - str: Un jeton JWT si l'inscription est réussie.

    Raises:
    Aucune exception n'est levée.
    """

    users.append(user)
    return sign_jwt(user.username)


@api.post("/user/login", tags=["user"])
async def user_login(user: UserSchema = Body(...)):
    """
    Description:
    Cette route permet à un utilisateur de se connecter en fournissant les détails de connexion. Si les détails sont valides, elle renvoie un jeton JWT. Sinon, elle renvoie une erreur.

    Args:
    - user (UserSchema, Body): Les détails de connexion de l'utilisateur.

    Returns:
    - str: Un jeton JWT si la connexion réussit.

    Raises:
    - HTTPException(401, detail="Unauthorized"): Si les détails de connexion sont incorrects, une exception HTTP 401 Unauthorized est levée.
    """

    if check_user(user):
        return sign_jwt(user.email)
    return {"error": "Wrong login details!"}
