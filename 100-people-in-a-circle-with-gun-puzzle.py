"""
http://quiz.geeksforgeeks.org/puzzle-100-people-in-a-circle-with-gun-puzzle/:

100 people standing in a circle in an order 1 to 100.
No. 1 has a gun.
He kills the next person (i.e. No. 2) and gives the gun to the next (i.e. No. 3).
All people do the same until only 1 survives. Which number survives at the last?
There are 100 people starting from 1 to 100.
"""

from collections import deque

#Iterative solution that optimizes time complexity using deque
def find_winner(participants):
    assert isinstance(participants, int), "Input needs to be in an integer"
    remaining_participants = deque(i for i in range(1, participants+1))
    while True:
        if len(remaining_participants) <= 1:
            return "The last survivor is particiant #{0}".format(remaining_participants[0])
        else:
            remaining_participants.append(remaining_participants.popleft())
            remaining_participants.popleft()  # Pop sounds better than murder...


print(find_winner(100))
