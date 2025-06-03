ADMINS = {1061444753}
OTZ  = {1061444753}
KADR  = {1061444753}
def get_user_role(user_id):
    """
    Get the role of a user based on their user ID.
    """
    if user_id in ADMINS:
        return 'admin'
    elif user_id in OTZ:
        return 'otz'
    elif user_id in KADR:
        return 'kadr'
    return 'user'