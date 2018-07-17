i = 0
j = 0
while i < 9:
    while j < i + 1:
        print('%d x %d = %d' % ((j + 1),(i + 1),(i + 1)*(j + 1)) , end = '     ')
        j += 1
    print('\n')
    i += 1
    j = 0

