import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the 'encryption' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def encryption(s):
    # Write your code here
    S = s.replace(' ', '')
    root = math.sqrt(len(S))
    row = math.floor(root)
    col = math.ceil(root)
    d = defaultdict(str)
    for i in range(0,len(S),col):
        st = S[i:i+col]
        for x in range(len(st)):
            d[x]+=st[x]
    return(list(d.values()))
print(*encryption(input()))
