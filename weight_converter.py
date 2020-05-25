weight=int(input('weight: '))
ch=input('(L)bs or KGs:')
if ch.upper()=='L':
    weight=weight*0.453592
    print(f'your weight is {weight} kgs')
elif ch.upper()=='K':
    weight=weight/0.453592
    print(f'your weight is {weight} pounds')
