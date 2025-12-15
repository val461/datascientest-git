from flask import Flask
from flask import jsonify
from flask import request
from datetime import timedelta

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {

    "danieldatascientest": {
        "username": "danieldatascientest",
        "name": "Daniel Datascientest",
        "email": "daniel@datascientest.com",
        "hashed_password": pwd_context.hash('datascientest'),
        "resource" : "Module DE",
    },

    "johndatascientest" : {
        "username" :  "johndatascientest",
        "name" : "John Datascientest",
        "email" : "john@datascientest.com",
        "hashed_password" : pwd_context.hash('secret'),
        'resource' : 'Module DS',
    }

}

api.config["JWT_SECRET_KEY"] = "8ceaef331d5231c53be041d5df58ab02a2b51220f737a1730e58a562a5e68b0a"  # Change this!
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
jwt = JWTManager(api)

def check_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(database, username):
    if username in database:
        user_dict = database[username]
        return user_dict

@api.route("/login", methods=["POST"])
def login():
    """
    Description:
    Cette route permet à un utilisateur de s'authentifier en fournissant un nom d'utilisateur et un mot de passe. Si l'authentification est réussie, elle renvoie un jeton d'accès JWT.

    Args:
    - request.json.get("username", None) (str): Le nom d'utilisateur saisi dans le corps de la requête JSON.
    - request.json.get("password", None) (str): Le mot de passe saisi dans le corps de la requête JSON.

    Returns:
    - JSON: Si l'authentification réussit, renvoie un JSON contenant un jeton d'accès.

    Raises:
    - JSONResponse({"msg": "Bad username or password"}, status_code=401): Si l'authentification échoue en raison d'un mauvais nom d'utilisateur ou d'un mot de passe, une réponse JSON avec le statut 401 Unauthorized est renvoyée.
    """

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = get_user(users_db, username)
    if not user or not check_password(password, user['hashed_password']):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@api.route("/user", methods=["GET"])
@jwt_required()
def get_current_user():
    """
    Description:
    Cette route permet de récupérer l'utilisateur actuellement authentifié en utilisant un jeton d'accès JWT.

    Args:
    Aucun argument requis.

    Returns:
    - JSON: Renvoie un JSON contenant le nom d'utilisateur de l'utilisateur actuellement authentifié.

    Raises:
    - Aucune exception n'est levée explicitement, sauf si la validation du jeton d'accès JWT échoue. Dans ce cas, une exception FastAPI sera levée automatiquement.
    """

    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@api.route("/resource", methods=["GET"])
@jwt_required()
def get_resource():
    """
    Description:
    Cette route permet de récupérer une ressource associée à l'utilisateur actuellement authentifié en utilisant un jeton d'accès JWT.

    Args:
    Aucun argument requis.

    Returns:
    - JSON: Renvoie un JSON contenant la ressource et le propriétaire de la ressource.

    Raises:
    - Aucune exception n'est levée explicitement, sauf si la validation du jeton d'accès JWT échoue. Dans ce cas, une exception FastAPI sera levée automatiquement.
    """

    current_username = get_jwt_identity()
    return jsonify({"resource" : get_user(users_db, current_username)['resource'],
    "owner": current_username})
