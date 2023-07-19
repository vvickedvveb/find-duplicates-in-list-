import json
import collections

"""
Instructions
----
Copy the array: Everything in, and including square brackets ONLY from the file to and assign to 'list_with_possible_dupes'.
e.g.: list_with_possible_dupes = ["400048","400048", "400049", "400199","400199", "400200", "400201", "400048"]

REPLACE
-------
Run script:
- e.g.: python3 find_dupes_in_list.py
- Copy generated list (everything in and including square brackets) from 'Removed from List:' and replace back. *** Take care replacing. ***
OR
Search import file with values in 'Dupes Found:' array, search and replace in file. *** Note format when replacing e.g.: quotes, brackets. ***
"""

# Assign array below
array_with_possible_dupes = ["400801","400534","400001","400010","400012","400016","400017","400019","400020","400021","400023","400024","400025","400028","400029","400035","400037","400039","400043","400044","400045","400046","400047","400048","400049","400052","400053","400054","400057","400058","400059","400505","400506","400507","400508","400509","400510","400511","400512","400513","400514","400515","400516","400517","400519","400520","400521","400524","400527","400528","400529","400531","400532","400533","400534","400535","400536","400538","400539","400543"]
############################################################################################

list_with_possible_dupes = list(array_with_possible_dupes)

dupe_list = []
no_dupe_list = []

throwaway_list = [no_dupe_list.append(x) if x not in no_dupe_list else dupe_list.append(x) for x in list_with_possible_dupes]
# print("\nOriginal List: ", list_with_possible_dupes)
print("\nDupes Found: ", json.dumps(dupe_list))
print("\nRemoved from List (Copy/Paste): ", json.dumps(no_dupe_list))


def dbl_chk_test(no_dupe_list, array_with_possible_dupes):
    """ Double check 'no_dupe_list' has no duplicates. """
    orig_array_set = set(array_with_possible_dupes)
    orig_array_list = list(orig_array_set).sort()
    no_dupe_list = list(no_dupe_list).sort()

    if orig_array_list == no_dupe_list:
        print("\nDbl Check Test: no more duplicates.\n")
    else:
        print("\nDbl Check Test: There ARE Duplicates.\n")
    return


# dbl_chk_test(no_dupe_list, array_with_possible_dupes)