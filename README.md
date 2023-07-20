# Monty_Hall
A program to solve the Monty Hall problem.

The Monty Hall problem is as follows:
You are presented with a choice of 3 doors. 2 doors have no prize behind, 1 door has a prize. You must pick a door to open. The host will then reveal one door that is incorrect.  The host then gives you a chance to switch your door that you initially picked to the other door remaining, or stay with your original door.

Mathematically proven, the odds of winning by switching should be 2/3 and without switching should be 1/3. This programme proves this by iterating NUMBER_OF_RUNS times and calulating the percentage of times each scenario wins. Increasing or decreasing NUMBER_OF_RUNS will get closer or further from the true result.

Randomly Assinging a Chosen Door:
        # Uses a list as a dataset, called pre_door_list, which holds two 0s and one 1.
        # 0 representing a door with no prize, and 1 a door with a prize
        # Randomly picks element from the dataset, and assigns them to positions in a new list.
        # Does this 3 times, the length of the list, to account for every element in the dataset
        # This allows the winning door to be in a random position, as well as there being the required number of losing and winning doors.

Calculating the number of times not switching is successful:
        # Randomly picks a door from the list, variable is door_chosen
        # Mathematics suggests 1/3 chance of winning. This is logical as you choose 1/3 doors and never change your decision.

Calculating the number of times switching is successful:
                # If one option of the two left is the correct door, because the host will reveal the incorrect door leaving you with just the winning door, you have 100% won.
                # Otherwise, if you chose the correct door originally and will be switching, you have 100% lost as you will switch to either incorrect door.
