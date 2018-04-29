import itertools
permutations = list(itertools.permutations(range(1,11)))
def parity(p):
  for i,element in enumerate(p):
    length = len(p)-1
    if i != length:
      if (p[i]%2==0 and p[i+1]%2==0) or (p[i]%2==1 and p[i+1]%2==1):
        return False
  return True

for pair in permutations:
  if parity(pair):
    print(pair)