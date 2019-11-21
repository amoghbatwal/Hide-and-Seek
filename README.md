# Hide-and-Seek

Working: The map is loaded into the fringe which is checked on every iteration for the condition of consisting of the same number of friends on board as requested via arguments. To place a friend at any position, certain conditions need to be satisfied. So, only when these conditions are passed, F is placed on the position we are at. So, the main brain of the code is the function ‘conditionchecking’. In this function, there are 8 conditions which are checked with respect to my current position on the board. My code is checking if F can be placed in the row and then whether F can be placed in that column. Condition checks in order are: In row validation:

1. If there is a friend in my row after my position
2. If a friend is there, is there an ampersand (&) between me and F which I found in step 1.
3. If there is a friend in my row before my position
4. If a friend is there, is there an ampersand (&) from my position to F which I found in step 3.

In column validation, similar checks happen:

1. If there is a friend in my column after my position
2. If a friend is there, is there an ampersand (&) between me and F which I found in step 1.
3. If there is a friend in my column before my position
4. If a friend is there, is there an ampersand (&) from my position to F which I found in step 3. 

Only when all these conditions are met, my code allows to place friend ‘F’ on the position I am at. Then, the goal is check and the board is returned with the no of friends entered.
