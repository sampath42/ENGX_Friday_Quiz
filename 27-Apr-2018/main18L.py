import math

inputs = [10,4,1800228]
for inputval in inputs:
    values = []
    if inputval >= 3 and inputval <= 3000000: #Constraint 3 <= n <= 3*10^6
        for x in range(inputval):
            for y in range(inputval):
                for z in range(inputval):
                    if x+y+z == inputval:
                        val = math.sin(x)+math.sin(y)+math.sin(z)
                        values.append(val)
    max_value = max(values)
    max_value_9_decimals = round(max_value, 9)
    print(inputval)
    print(max_value_9_decimals)
