from random import randint

for i in range(20):
    a=int(randint(10,60))
    if a>43 and a<60:print(f'large {a} number')
    elif  a>35 and a<43:print(f'medium {a} number')
    elif a>25 and a<35: print(f'small {a} number')
    else:print(f'N.A.{a}')