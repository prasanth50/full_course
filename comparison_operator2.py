name=input('Enter your name? ')
l=len(name)
print(l)
if l<=3:
    print('Name must havee atleast 3 characters')
elif l>50:
    print('Name must have less than 50 cha.')
else:
    print('Name looks good')