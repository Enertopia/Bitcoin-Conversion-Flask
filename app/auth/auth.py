from . import jwt

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id
