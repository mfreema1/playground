def sum(lst):
        """
        Add up the values in the list
        """
        res = 0
        for item in lst:
            res += item[1]
        return res

def knapsack(lst, weight, items = []):
    """
    lst is a list of lists.  Each inner list is a pair of a weight and a value.

    Determine the maximum value you can get while remaining below the weight limit.
    """
    if weight == 0:
        return (True, items)

    if weight < 0 or lst == []:
        return (False, [])

    use_it = knapsack(lst[1:], weight - lst[0][0], items + [lst[0]])
    lose_it = knapsack(lst[1:], weight, items)

    if use_it[0] and lose_it[0]:
        if(sum(use_it[1]) >= sum(lose_it[1])):
            return use_it
        return lose_it

    if use_it[0]: return use_it
    if lose_it[0]: return lose_it

    return (False, [])

print(knapsack([[5, 20], [10, 25], [5, 10]], 10)) #(True, [[5, 20], [5, 10]])

def knapsack_dynamic(lst, weight, items = [], dict = {}):

    if(weight == 0):
        return (True, items)
    if(weight < 0 or lst == []): #you have to fill the bag
        return (False, [])

    if(dict.get(weight)):
        return (True, dict[weight])

    use_it = knapsack_dynamic(lst[1:], weight - lst[0][0], items + [lst[0]], dict)
    lose_it = knapsack_dynamic(lst[1:], weight, items, dict)

    if(use_it[0] and lose_it[0]):
        if(sum(use_it[1]) >= sum(lose_it[1])):
            larger = use_it
        else:
            larger = lose_it
    elif(use_it[0]):
        larger = use_it
    elif(lose_it[0]):
        larger = lose_it
    else:
        return (False, [])

    if(dict.get(weight)):
        if(sum(dict[weight]) < sum(larger[1])):
            dict[weight] = larger[1]
        return (True, dict[weight])
    else:
        dict[weight] = larger[1]
        return (True, dict[weight])

print(knapsack_dynamic([[5, 20], [10, 25], [5, 10], [5, 15], [5, 30], [10, 30]], 25))