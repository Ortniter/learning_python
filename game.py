from random import choice
import os
import sys


class Game:
    def __init__(self, rooms, items, player):
        self.rooms = rooms
        self.items = items
        self.player = player

    def find_room(self, room_x, room_y):
        rooms = [room for room in self.rooms if all(
            (room.x == room_x, room.y == room_y))]
        if rooms:
            return rooms[0]
        else:
            return None

    def add_npc(self, npcs):
        rooms = list()
        for npc in npcs:
            room = choice(self.rooms)
            if room not in rooms:
                rooms.append(room)
                npc.player = self.player
                room.room_npc = npc
                room.edit_description()
            else:
                continue

    def add_items(self):
        rooms = list()
        for item in self.items:
            room = choice(self.rooms)
            if room not in rooms:
                rooms.append(room)
                item.room = room
                room.room_item = item
                item.player = self.player
                room.edit_description()
            else:
                continue

    @staticmethod
    def interact_check(act, words):
        for word in words:
            if word in act:
                return True
            continue


class Room:
    def __init__(self, description, x, y):
        self.description = description
        self.x = x
        self.y = y
        self.room_npc = None
        self.room_item = None
        self.update_description = description

    def __repr__(self):
        return f"{self.description}"

    def __str__(self):
        return f"{self.description}"

    def edit_description(self):
        npc = f" And {self.room_npc.appearance} stood there." if self.room_npc else ""
        room_item = f" Also {self.room_item.name} was there." if self.room_item else ""
        self.update_description = f"{self.description}.{room_item}{npc}"


class Player:
    cache_move = tuple()

    def __init__(self, start_room):
        self.cur_room = start_room
        self.x = self.cur_room.x
        self.y = self.cur_room.y
        self.hp = 5
        self.weapon = None
        self.tools = list()

    def check_inventory(self):
        if self.tools:
            print(f"This is your inventory: \n{self.tools}")
            print("(type 'exit' to close inventory)")
            while True:
                check = None
                answer = input("Choose item: ")
                if answer == 'exit':
                    break
                else:
                    for tool in self.tools:
                        if tool.name == answer:
                            tool.inventory_interact()
                            self.tools.remove(tool)
                            check = True
                            break
                    if not check:
                        print('There is no such item in an inventory')
                    continue
        else:
            print("Your inventory is empty")

    def look_around(self):
        print(f'You see: {self.cur_room.update_description}')

    def _move(self, new_x, new_y):
        room = game.find_room(new_x, new_y)
        if room:
            self.cache_move = (int(self.x), int(self.y))
            self.cur_room = room
            self.x = room.x
            self.y = room.y
            self.look_around()
        else:
            print('There is no way you can go there')

    def go_to(self, where):
        if where == 'go north':
            self._move(self.x, self.y + 1)
        elif where == 'go east':
            self._move(self.x + 1, self.y)
        elif where == 'go west':
            self._move(self.x - 1, self.y)
        elif where == 'go south':
            self._move(self.x, self.y - 1)
        elif where == 'go back':
            self._move(self.cache_move[0], self.cache_move[1])
        else:
            print('You can not do this')


class NPC:
    def __init__(self, name, appearance, phrases):
        self.name = name
        self.appearance = appearance
        self.phrases = phrases
        self.player = None

    def __str__(self):
        return self.appearance

    def __repr__(self):
        return self.appearance

    def dialog_with_npc(self):
        self.talk()
        if self.phrases:
            print("(you can type 'go back' to exit a dialog)")
            for phrase in self.phrases:
                answer = input(
                    'Type your answer if you want to continue dialog: ')
                if 'go back' not in answer:
                    print(f"{self.name}: '{phrase}'")
                else:
                    break
        else:
            print('...')

    def talk(self):
        print(f"Unknown person: 'I'm {self.name}. {self.phrases.pop(0)}'")


class Enemy(NPC):
    def __init__(self, name, appearance, phrases, hp, level):
        super().__init__(name, appearance, phrases)
        self.hp = hp
        self.level = level
        self.player = None

    def talk(self):
        print(f"{self.name}: '{self.phrases.pop(0)}'")

    def fight(self, act):
        if self.hp:
            if act:
                self.talk()
                self.player.hp -= 1
            while self.hp != 0:
                print(
                    f'"You are in a fight mode" | Your_HP:{self.player.hp} -- {self.name}_HP:{self.hp}')
                attack = input('Fight: ')
                if attack == 'attack':
                    self.hp -= 1
                elif attack == 'defend':
                    print('You have been protected')
                elif attack == '':
                    self.player.hp -= 1
                    if not self.player.hp:
                        print("You've lost")
                        restart = input(
                            'Type "restart" if you want to start again: ')
                        if restart == 'restart':
                            os.execl(sys.executable,
                                     sys.executable, * sys.argv)
                    else:
                        continue
                else:
                    print('Unsupported action')
        else:
            print(f"{self.name}: 'You have defeated me'")


class Item:
    def __init__(self, name, description, kind):
        self.room = None
        self.player = None
        self.name = name
        self.description = description
        self.kind = kind

    def __repr__(self):
        return f'{self.name} ({self.description})'

    def __str__(self):
        return f'{self.name} ({self.description})'

    def inventory_interact(self):
        if 'healing' in self.kind:
            self.player.hp += 3
            print(f"Your HP now is: '{self.player.hp}'")
        elif 'weapon' in self.kind:
            if self.player.weapon:
                self.player.tools.append(self.player.weapon)
                self.player.weapon = self
                print(f"Your weapon now is: '{self.name}'")
            else:
                self.player.weapon = self
                print(f"Your weapon now is: '{self.name}'")
        else:
            print('Unknown tool')

    def interact(self):
        if self.room:
            if 'tool' in self.kind:
                self.player.tools.append(self)
                self.room.room_item = None
                self.room.edit_description()
                print(f'{self.name} added to your inventory')
            elif self.kind == 'door':
                print('Door was closed')
            elif self.kind == 'chest':
                print('You have opened the chest. But it is empty.')
            else:
                print('You can not interact with this item.')
        else:
            print('There is no items in this room')


game_rooms = [
    Room('A room with a staircase', 5, 5),
    Room('A room with large window and table', 5, 6),
    Room('A big library without people, but strange sound is heard from far away', 4, 5),
    Room('An empty room with large entrance to the basement on the floor', 5, 4),
    Room('An empty corridor leading to east', 6, 5),
    Room('A room with a door to the north. The door seems to be locked', 6, 6)
]

enemies = [
    Enemy('Craven', 'Tall vampire in dark coat', [
          'This is the end of you'], 5, 'first'),
    Enemy('Craven', 'Tall vampire in dark coat', [
          'This is the end of you'], 5, 'first'),
    Enemy('Craven', 'Tall vampire in dark coat',
          ['This is the end of you'], 5, 'first')
]

NPCs = [
    NPC('Garolt the old', 'tough man in rich dresses who looked really nobel despite his age',
        ['Hello stranger, I am the king of this land. What are you doing here?', 'Nice to meet you, my friend.',
         'I see.']),
    NPC('Herbalist', 'young woman with long white hair', ['Who are you, can I help you somehow?',
                                                          'I see, that a really strange place. I hope you will find the way out.',
                                                          'I see.']),
    NPC('Avery Hunter', 'short man with a rifle at his back',
        ['Hello, I am not from here, I try to find the way out. Will you join me?',
         'If you join me, we will able to go for a hunt.', 'What is your favorite place at the border of the empire?',
         'I see'])
]

items = [
    Item('healing herbs', 'has magic color', 'healing tool'),
    Item('healing herbs', 'has magic color', 'healing tool'),
    Item('sword', 'ancient weapon crafted by goblins', 'weapon tool'),
    Item('sword', 'ancient weapon crafted by goblins', 'weapon tool'),
    Item('door on the wall', 'Old wooden door.', 'door'),
    Item('chest', 'Gold chest.', 'chest')
]

player = Player(game_rooms[0])
game = Game(game_rooms, items, player)
game.add_items()
game.add_npc(NPCs)
game.add_npc(enemies)
player.look_around()

while True:
    action = input('What is your next action?: ')
    if 'go' in action:
        player.go_to(action)
        continue
    elif 'look around' == action:
        player.look_around()
        continue
    elif Game.interact_check(action, ['talk', 'speak', 'dialog', 'question']):
        npc = player.cur_room.room_npc
        if isinstance(npc, Enemy):
            npc.fight(True)
        elif npc:
            npc.dialog_with_npc()
        else:
            print('There is nobody to talk with')
    elif Game.interact_check(action, ['fight', 'attack', 'battle', 'combat']):
        player.cur_room.room_npc.fight(False)
    elif Game.interact_check(action, ['take', 'open', 'interact']):
        try:
            player.cur_room.room_item.interact()
        except AttributeError:
            print('There are no items in this room')
    elif Game.interact_check(action, ['inventory', 'bag', 'items', 'tools']):
        player.check_inventory()
    else:
        print('You can not do this')
