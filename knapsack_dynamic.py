"""
Dynamic programming can be very tricky.

"""
def knapsack(capacity, lst):
    number_items = len(lst)

    table = [[0 for col in range(capacity + 1)] for row in range(number_items + 1)] #+1 for dummy values
    for row in range(1, number_items + 1): #range chops off last one
        for col in range(1, capacity + 1):
            if(col < lst[row - 1][0]): #we have to lose it
                table[row][col] = table[row - 1][col]
            else:
                use_it = lst[row - 1][1] + table[row - 1][col - lst[row - 1][0]] #value plus subproblem value
                lose_it = table[row - 1][col]
                table[row][col] = max(use_it, lose_it)
    return table[-1][-1] #get bottom right value

print(knapsack(7, [(3, 2), (1, 4), (2, 3), (5, 1), (6, 6)]))
