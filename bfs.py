from collections import deque

"""
We can implement a graph by having dictionary entries map to lists.  We only record the people that someone immediately knows.  People who do not know anybody are not included
"""
graph = {
    'Mark': ['Ashley', 'Sarah', 'Ed', 'Bob'],
    'Ashley': ['Rick', 'Paul'],
    'Sarah': ['Jenny', 'Mike', 'Ashley'],
    'Ed': ['John', 'Bill', 'Lauren'],
    'Bob': ['Tim', 'Courtney'],
    'Rick': ['Bob'],
    'Paul': ['Caroline']
}

"""We don't keep a hash table for this because it would only map to true or false and devolve into a linked list anyways"""
def _is_mango_seller(name):
    return name[-1] == 'm'

def knows_mango_seller(name):
    #grab the people that the first person knows
    queue = deque()
    queue += graph[name]
    visited = []

    while(queue):
        #pop the first person off the queue, see if they are a mango seller
        person = queue.popleft()
        if(person not in visited):
            if(_is_mango_seller(person)):
                print('{} is a mango seller!'.format(person))
                return True
            elif(graph.get(person)): #if they know people add them in
                queue += graph[person]
                visited += [person]
    return False #we couldn't find any mango sellers

print(knows_mango_seller('Mark'))