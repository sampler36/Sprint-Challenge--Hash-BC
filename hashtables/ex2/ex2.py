#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    # looking on the test ticket should equal none on start
    your_ticket = None

    # Add key value to the hash table for every ticket 
    for ticket in range(length):
        hash_table_insert(hashtable, tickets[ticket].source, tickets[ticket].destination)
        # Check if the ticket flight is None
        if tickets[ticket].source == "NONE":
            # Assign it to your_ticket
            your_ticket = tickets[ticket].destination
            # Assign your_ticket to first route array
            route[0] = your_ticket

    for ticket in range(1, length):
        # Use hash_table_retrieve to find next destination
        next_destination = hash_table_retrieve(hashtable, your_ticket)
        # Assign next_destination to the route array
        route[ticket] = next_destination
        # Assing your_ticket to next destination
        your_ticket = next_destination

    return route