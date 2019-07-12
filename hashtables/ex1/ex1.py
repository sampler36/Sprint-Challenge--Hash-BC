#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                      


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # make a loop that include weights
    # pick out the index
    # use insert and hash_table_retrieve
    # return None
    # for i in :
    #     index = hash_table_retrieve(ht, limit - weights[i])

    # else:
    #     hash_table_insert(ht, weights[i], i)
    
    # return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
