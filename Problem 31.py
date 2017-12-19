coins = [1,2,5,10,20,50,100,200]

def combines_of_coins(coin_start,target):
    combinations = []
    if target >= coin_start:
        for coin in coins:
            new_target = target - coin
            if new_target == 0:
                combinations.append([coin])
            elif new_target < coin:
                break
            else:
                for i in combines_of_coins(coin_start,new_target):
                    combinations.append([coin] + i)
    return combinations

def remove_repeats(list1):
    for x in list1:
        for y in list1:
            if len(x) == len(y) and list1.index(x) != list1.index(y):
                list1.remove(y)
    return list1

print(remove_repeats(combines_of_coins(1,4)))
