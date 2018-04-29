import itertools
import math

inputval = 300000000
oldval = 0

def store_max_val(newval):
    global oldval
    oldval = newval

def calculate_trignometry_sum(n):
    sumVal = sum(n)
    if(sumVal) == inputval:
        val = math.sin(n[0])+math.sin(n[1])+math.sin(n[2])        
        if oldval < val:
            store_max_val(val)

if inputval >= 3 and inputval <= 3000000:
    combinations = itertools.combinations_with_replacement(range(inputval),3)
    for combination in combinations:
        calculate_trignometry_sum(combination)
    max_value = oldval
    max_value_9_decimals = round(max_value, 9)
    print(max_value)
    print(max_value_9_decimals)
else:
    print("input should satisfy the constraint 3 ≤ n ≤ 3 X 10^6")
