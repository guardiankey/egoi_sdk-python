from egoi_api.paths.lists_list_id.get import ApiForget
from egoi_api.paths.lists_list_id.delete import ApiFordelete
from egoi_api.paths.lists_list_id.patch import ApiForpatch


class ListsListId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
