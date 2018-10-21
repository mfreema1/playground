#just a brief refresher on some dynamic programming

def exactChange(amount, coinList, currList = []):
    if amount == 0:
        return (True, currList)
    
    if amount < 0 or coinList == []:
        return (False, [])

    use_it = exactChange(amount - coinList[0], coinList, currList + [coinList[0]])
    lose_it = exactChange(amount, coinList[1:], currList)

    if(use_it[0] and lose_it[0]):
        if(len(use_it[1]) <= len(lose_it[1])):
            return (True, use_it[1])
        else:
            return (True, lose_it[1])

    if(use_it[0]):
        return (True, use_it[1])
    if(lose_it[0]):
        return (True, lose_it[1])

    return (False, [])

print(exactChange(50, [1, 5, 10, 25]))

def exactChangeNoReplacement(amount, coinList):
    if(amount == 0):
        return True
    
    if(amount < 0 or coinList == []):
        return False
    
    use_it = exactChangeNoReplacement(amount - coinList[0], coinList[1:])
    lose_it = exactChangeNoReplacement(amount, coinList[1:])

    return use_it or lose_it

print(exactChangeNoReplacement(10, [1, 5]))
print(exactChangeNoReplacement(10, [5, 5, 5]))

def powerset(lst, res = []):

    if(lst == []):
        return res

    use_it = powerset(lst[1:], res + [lst[0]])
    lose_it = powerset(lst[1:], res)

    return [use_it] + [lose_it]

print(powerset(['a', 'b', 'c']))