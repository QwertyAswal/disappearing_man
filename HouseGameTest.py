class room:
    itemlist = []
    name = ''

    def __init__(self, nm):
        self.n = None
        self.e = None
        self.w = None
        self.s = None
        self.name = nm

    def sides(self, n, e, w, s):
        self.n = n
        self.e = e
        self.w = w
        self.s = s

    def removeitem(self, x):
        if x < self.itemlist.__len__():
            return self.itemlist.pop(x)

    def additem(self, x):
        self.itemlist.append(x)


class man:
    inventory = []

    def __init__(self, obj):
        self.current = obj

    def move(self):
        print("\n\nMove:--\n")
        if self.current.n.name != 'None':
            print('1: North:-- ', self.current.n.name)
        if self.current.e.name != 'None':
            print('2: East:-- ', self.current.e.name)
        if self.current.w.name != 'None':
            print('3: West:-- ', self.current.w.name)
        if self.current.s.name != 'None':
            print('4: South - ', self.current.s.name)
        choice = int(input('Enter Direction: '))
        if choice == 1:
            self.current = self.current.n
        elif choice == 2:
            self.current = self.current.e
        elif choice == 3:
            self.current = self.current.w
        elif choice == 4:
            self.current = self.current.s

    def look(self):
        print("North:-", self.current.n.name)
        print("East:--", self.current.e.name)
        print("West:--", self.current.w.name)
        print("South:--", self.current.s.name)

    def pickup(self):
        print('\n\nItems Available:--\n')
        print('0 :- None')
        for i in range(self.current.itemlist.__len__()):
            print((i + 1), ":-", self.current.itemlist[i])
        inp = int(input('Enter Value to be picked: '))
        if inp != 0:
            self.inventory.append(self.current.itemlist[inp - 1])
            self.current.removeitem(inp - 1)

    def showinvent(self):
        print("\n\nInventory:--\n")
        for i in range(self.inventory.__len__()):
            print((i + 1), ":", self.inventory[i])

    def drop(self):
        print('\n\nDrop:--\n')
        for i in range(self.inventory.__len__()):
            print((i + 1), ":", self.inventory[i])
        inp = int(input('Enter Value to be dropped(0 for none):--'))
        if inp != 0:
            st = self.inventory.pop(inp - 1)
            self.current.additem(st)


road = room('road')
road.itemlist = ['garbge', 'leaves', 'onions']

lawn = room('lawn')
lawn.itemlist = ['grass', 'flower']

garage = room('garage')
garage.itemlist = ['jack', 'mower']

hall = room('hall')
hall.itemlist = ['book', 'pen']

dining = room('dining')
dining.itemlist = ['plate', 'spoon']

bedroom = room('bedroom')
bedroom.itemlist = ['wife', 'wallet']

store = room('store')
store.itemlist = ['screwdriver']

gym = room('gym')
gym.itemlist = ['bag', 'mat']

kitchen = room('kitchen')
kitchen.itemlist = ['knife', 'apple']

road.sides(lawn, room('None'), room('None'), room('None'))
lawn.sides(hall, garage, room('None'), road)
garage.sides(dining, room('None'), lawn, room('None'))
hall.sides(gym, dining, bedroom, lawn)
dining.sides(kitchen, room('None'), hall, garage)
kitchen.sides(room('None'), room('None'), gym, dining)
gym.sides(room('None'), kitchen, store, hall)
store.sides(room('None'), gym, room('None'), bedroom)
bedroom.sides(store, hall, room('None'), room('None'))

player = man(road)
flag = 0


def view():
    global flag
    print("-------------" * 3)
    print("current position :", player.current.name)
    print('1: Look')
    print('2: Move')
    print('3: Pickup')
    print('4: Drop')
    print('5: Inventory')
    print('0: Exit')

    choice = int(input('Enter your choice:-  '))
    if choice == 1:
        player.look()
    elif choice == 2:
        player.move()
    elif choice == 3:
        player.pickup()
    elif choice == 4:
        player.drop()
    elif choice == 5:
        player.showinvent()
    elif choice == 0:
        flag = 1


while flag == 0:
    view()
