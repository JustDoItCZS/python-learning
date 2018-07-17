while True:
    import random
    tmp = random.randint(0,2)
    if tmp == 0:
        computer = '石头'
    elif tmp == 1:
        computer = '剪刀'
    elif tmp == 2:
        computer = '布'
    you = input('你要出什么？（石头、剪刀或布）')
    while you != '石头' and you != '剪刀' and you != '布':
        you = input('再问你一次，你要出什么？（石头、剪刀或布）')
    print('电脑出%s' % computer)
    print('你出%s' % you)
    if computer == '石头':
        if you == '石头':
            print('平局！')
        elif you == '剪刀':
            print('你输了！')
        elif you == '布':
            print('你赢了！')
    elif computer == '剪刀':
        if you == '石头':
            print('你赢了！')
        elif you == '剪刀':
            print('平局！')
        elif you == '布':
            print('你输了！')
    elif computer == '布':
        if you == '石头':
            print('你输了！')
        elif you == '剪刀':
            print('你赢了！')
        elif you == '布':
            print('平局！')





