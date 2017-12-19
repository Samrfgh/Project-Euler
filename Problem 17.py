numbers = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
          10:"ten", 11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
          20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def letters_in_number(x):
    if (x < 20) or (x % 10 == 0 and x < 100):
        return numbers[x]
    elif x < 100:
        return letters_in_number(x // 10 * 10) + letters_in_number(x % 10)
    elif x % 100 == 0 and x < 1000:
        return numbers[x // 100] + "hundred"
    elif x < 1000:
        return letters_in_number(x // 100 * 100) + "and" + letters_in_number(x % 100)
    else:
        return letters_in_number(x // 1000) + 'thousand' + letters_in_number(x % 1000)

print letters_in_number(9999)
