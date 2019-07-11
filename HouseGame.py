items = {'Road': ['Garbage', 'Leaves', 'Onions'], 'Lawn': ['Grass', 'Flowers'], 'Garage': ['Mower'],
         'Dining Hall': ['Spoon', 'Fruits', 'Knife'],
         'TV Room': ['Remote', 'CD'], 'Common Area': ['Pillow', 'Chair'], 'Stair Case': [],
         'Toilet': ['Brush', 'Soap', 'Shampoo'], 'Bedroom': ['Wife', 'Child'],
         'Kitchen': ['Masala', 'Lighter', 'Food'], 'Store Room': ['Tools', 'Scissors']}
mp = [['none', 'none', 'none', 'none', 'none', 'none'],
      ['none', 'Toilet', 'Bedroom', 'Kitchen', 'Store Room', 'none'],
      ['none', 'Dining Hall', 'TV Room', 'Common Area', 'Stair Case', 'none'],
      ['none', 'none', 'none', 'Lawn', 'Garage', 'none'],
      ['none', 'Road', 'Road', 'Road', 'Road', 'none'],
      ['none', 'none', 'none', 'none', 'none', 'none']]
x = 4
y = 1
inventory = []
f = 0


def look():
    print('\n\nLOOK   :-\n')
    print('North  :-', mp[x - 1][y])
    print('East   :-', mp[x][y + 1])
    print('West   :-', mp[x][y - 1])
    print('South  :-', mp[x + 1][y])


def move():
    global x, y
    print('\n\nMOVE   :-\n')
    if mp[x - 1][y] != 'none':
        print('1:--', mp[x - 1][y])
    if mp[x][y + 1] != 'none':
        print('2:--', mp[x][y + 1])
    if mp[x][y - 1] != 'none':
        print('3:--', mp[x][y - 1])
    if mp[x + 1][y] != 'none':
        print('4:--', mp[x + 1][y])
    ch = input('\nEnter Your Choice:- ')
    if ch == '1':
        x = x - 1
    elif ch == '2':
        y = y + 1
    elif ch == '3':
        y = y - 1
    elif ch == '4':
        x = x + 1


def item():
    li = items[mp[x][y]]
    print('\n\nITEMS  :-\n')
    print('0 :-- None')
    for i in range(li.__len__()):
        print((i + 1), ':--', li[i])
    ir = int(input('\nEnter Your Choice:- '))
    if ir != 0:
        inventory.append(li[ir - 1])
        items[mp[x][y]].pop(ir - 1)


def invent():
    print('\n\nINVENTORY :-\n')
    for i in range(inventory.__len__()):
        print((i + 1), ':--', inventory[i])


def drop():
    print('\n\nDROP :-\n')
    for i in range(inventory.__len__()):
        print((i + 1), ':--', inventory[i])
    ir = int(input('\nEnter Your Choice(Press 0 for none):- '))
    if ir != 0:
        items[mp[x][y]].append(inventory[ir - 1])
        inventory.pop(ir - 1)


def view():
    global f
    print('\n\n----------------------------------------------------------\n\n')
    print('Current Position:-', mp[x][y])
    print('1:--Look')
    print('2:--Move')
    print('3:--Item')
    print('4:--Drop')
    print('5:--Inventory')
    print('0:--Exit')
    ch = input('Enter Your Choice:--')
    if ch == '1':
        look()
    elif ch == '2':
        move()
    elif ch == '3':
        item()
    elif ch == '4':
        drop()
    elif ch == '5':
        invent()
    elif ch == '0':
        f = 1


while f == 0:
    view()
