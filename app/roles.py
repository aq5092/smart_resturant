from typing import List
ADMINS = set()
KADR = {1061444753,2112762237}
OTZ = {1061444753, 306794063, 665777879, 53686779} # 53686779 - ilxom


def get_user_roles(user_id: int) -> List[str]:
    roles = []
    if user_id in ADMINS:
        roles.append("admin")
    if user_id in KADR:
        roles.append("kadr")
    if user_id in OTZ:
        roles.append("otz")
    if not roles:
        roles.append("user")
    return roles

# def get_user_role(user_id: int) -> str:
#     """
#     Get the role of a user based on their user ID.
#     """
#     if user_id in ADMINS:
#         return 'admin'
#     if user_id in KADR:
#         return 'kadr'
#     if user_id in OTZ:
#         return 'otz'
#     return 'user'
