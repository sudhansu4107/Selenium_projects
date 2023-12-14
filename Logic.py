Data1 = {'a':1,'b':2}
Data2 = {'a':1,'b':2}
keys=(Data2.keys())

for key in keys:
    if Data1.get(key)== Data2.get(key):
        print('yes')