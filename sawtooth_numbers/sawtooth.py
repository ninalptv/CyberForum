lst = list('91')
n = len(lst)
if n == 1:
    print('sawtoth')
if n == 2:
    if lst[0]<lst[1]:
        print('sawtoth')
    else:
        print('not sawtoth')
for i in range(2, n):
    if lst[i] < lst[i - 1] > lst[i - 2]:
        if i == n - 1:
            print('sawtoth')
        continue
    elif lst[i] > lst[i - 1] < lst[i - 2]:
        if i == n - 1:
            print('sawtoth')
        continue
    else:
        print('not sawtoth')
        break