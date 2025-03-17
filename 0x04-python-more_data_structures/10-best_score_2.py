#!/usr/bin/python3
def best_score(a_dictionary):
    """Gets the name of student with best score from a dictionary

    a_dictionary: Dictionary with student as keys and respective score as value

    """
    if not a_dictionary:
        return None

    best = dict()
    # make scores new keys so they can be sorted
    for k, v in a_dictionary.items():
        best[v] = k

    sort_new_key = sorted(best.keys())

    #get highest score in sorted list
    best_score = sort_new_key[-1]

    #return name of student with best score
    return best[best_score]
