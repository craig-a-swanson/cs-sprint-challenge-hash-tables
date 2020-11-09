#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    # create array for the final route
    route = []
    # create a dictionary to store the source (key) and destination (value)
    ticket_dict = {}

    # iterate through the tickets array that was passed in
    # add each ticket to the dictionary
    for ticket in tickets:
        source = ticket.source
        dest = ticket.destination
        ticket_dict[source] = dest
    
    # start at the current source of "NONE"
    # for each ticket in the dictionary, append its destination to the route array
    # then set the current_source equal to the ticket's destination and loop through
    current_source = "NONE"
    for _ in range(length):
        current_ticket = ticket_dict[current_source]
        route.append(current_ticket)
        current_source = current_ticket

    return route