#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Check length of weights, if less than two than retrun none
    if length < 2:
        return None

    # Insert the weights into the hash table
    # self, key, value
    for key in range(length):
        # Insert the weights into the table keyed and value based on the weight
        # Following the hints here, honestly the most confusing part is the wording
        hash_table_insert(ht, weights[key], key)

    # Loop through weights and check to see if limit - weight = KEY where KEY is in the hashtable.
    for n in range(length):
        check_num = limit - weights[n]
        index_of_weight = hash_table_retrieve(ht, check_num)
        if index_of_weight:
            if index_of_weight > n:
                return (index_of_weight, n)
            else:
                return (n, index_of_weight)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
