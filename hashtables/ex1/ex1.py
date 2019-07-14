#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
                      


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # set tuple
    # initialise the hash table
    # use enumerate to find index
    # check if there is a difference
    # make a loop that include weights
    # use insert if the differnce been found 
    # then hash_table_retrieve the new table in order
   
        # set tuple
    pair = ()
    # initialise our hash table
    hash_table = {}

    if length <= 1:
        return None
    for i, v in enumerate(weights):
        difference = limit - v
        # Check if we found the difference
        if (validation(hash_table, difference)):
            # if difference has been found, return in proper order
            if (hash_table[difference] > i):
                pair = (hash_table[difference], i)
            else:
                pair = (i, hash_table[difference])
        # else, add to the hash table
        hash_table[v] = i
    return pair


def validation(hash_table, key):
    try:
        hash_table[key]
        return True
    except:
        return False


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
