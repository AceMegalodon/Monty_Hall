import random

if __name__ == "__main__":
    
    NUMBER_OF_RUNS = 100000
    number_of_times_sticking_was_correct = 0
    number_of_times_switching_was_correct = 0

    for i in range(NUMBER_OF_RUNS):

# =---- Randomly assigning door_chosen:

        pre_door_list = [0,0,1]
        door_list = []
        door_chosen = random.randint(0, 2)

        for i in range(len(pre_door_list)):
            random_int = random.randint(0, len(pre_door_list) -1)
            door_list.append(pre_door_list.pop(random_int))

# =---- Calculating the number of times sticking results in a correct answer:

        if door_list[door_chosen] == 1:
            number_of_times_sticking_was_correct += 1

# =---- Calculating the number of times switching results in a correct answer:

        door_list.pop(door_chosen)
        for i in door_list:
            if i == 1:
                number_of_times_switching_was_correct += 1
                break

    print("Percentage of times sticking won = " + (str((number_of_times_sticking_was_correct / NUMBER_OF_RUNS) * 100)) + "%")
    print("Percentage of times switching won = " + (str((number_of_times_switching_was_correct / NUMBER_OF_RUNS) * 100)) + "%")