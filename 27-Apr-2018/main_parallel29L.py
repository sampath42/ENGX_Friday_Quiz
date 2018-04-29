import itertools
import math

inputval = 2920383
values = []
oldval = 0

def store_max_Val(newval):
    global oldval
    oldval = newval

def calculateSum(n):
    sumVal = sum(n)
    if(sumVal) == inputval:
        val = math.sin(n[0])+math.sin(n[1])+math.sin(n[2])        
        if oldval < val:
            store_max_Val(val)
        #values.append(val)

    #return sumVal
# def fun(*args):
#     print(sum(*args))
#     return sum(*args)

# input = ((x,y,z) for x,y,z in itertools.combinations_with_replacement(range(4), 3))
# print(input)
#results = p.map(fun, input)
#p.close()
#p.join()
#print(results)

combinations = itertools.
#print(combinations)
for v in combinations:
    calculateSum(v)
# if __name__ == "__main__":
#     with Pool(4) as p:
#         p.map(calculateSum,combinations,chunksize=10)

# print("values")
# print(values)
max_value = oldval#max(values)
max_value_9_decimals = round(max_value, 9)
print(max_value)
print(max_value_9_decimals)

    # print(result)
#print(sum(combinations[0]))
#result = map(calculateSum, combinations)
#print(result)
#print([sum(val) for val in combinations])
#print(sumvalues)

# def parity(p):
#   for i,element in enumerate(p):
#     length = len(p)-1
#     if i != length:
#       if (p[i]%2==0 and p[i+1]%2==0) or (p[i]%2==1 and p[i+1]%2==1):
#         return False
#   return True

# for pair in permutations:
#   if parity(pair):
#     print(pair)