# MVC design pattern for call park

from .get_huntgroups import GetHuntGroups
from .build_hg_tree import BuildHuntGroup

def list_huntgroups(main_window):
    huntgroupList = GetHuntGroups(main_window.service)
    return BuildHuntGroup(huntgroupList.tree_view)
    

