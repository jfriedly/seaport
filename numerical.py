import copy
import sys


def subsetsum(superset, target):
    """Finds a subset of the integers in superset that sum to target"""
    res = {0 : []}
    closest_larger = (sys.maxsize, [])
    for i in superset:
        newres = dict(res)
        for v, l in res.items():
            if v+i < target:
                newres[v+i] = l+[i]
            elif v+i == target:
                return l+[i]
            else:
                if v+i < closest_larger[0]:
                    closest_larger = (v+i, l+[i])
        res = newres
    return closest_larger[1]

#TODO(jfriedly):  Rewrite this using python sets
def remove_subset(minuend, subtrahend):
    """Removes the set subtrahend from the set minuend.

    difference = minuend - subtrahend
    """
    difference = copy.deepcopy(minuend)
    for element in subtrahend:
        try:
            difference.remove(ship)
        except:
            pass
    return difference
