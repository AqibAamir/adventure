import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_item(self, item):
        self.items.append(item)

    def get_details(self):
        details = f'{self.name}\n{self.description}\n'
        if self.items:
            details += f'Items in the room: {", ".join(self.items)}\n'
        return details

    def move(self, direction):
        return self.paths.get(direction, None)

class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms['Start']
        self.inventory = []
        self.is_over = False

    def create_rooms(self):
        start = Room("Start", "You are at the starting point of your adventure.")
        forest = Room("Forest", "You are in a dark forest. It's eerily quiet.")
        cave = Room("Cave", "You have entered a damp cave. You hear water dripping.")
        mountain = Room("Mountain", "You are at the base of a tall mountain. The peak is hidden by clouds.")
        village = Room("Village", "You find yourself in a small village. The villagers look at you curiously.")
        castle = Room("Castle", "You stand before a grand castle. The gates are open.")
        dungeon = Room("Dungeon", "You have been captured and thrown into a dark dungeon.")
        treasure = Room("Treasure Room", "You've discovered a room filled with gold and jewels!")
        library = Room("Library", "You are in a library filled with ancient books and scrolls.")
        tower = Room("Tower", "You climb a tower and see the entire kingdom.")
        garden = Room("Garden", "You are in a beautiful garden with colorful flowers and fountains.")
        lake = Room("Lake", "You arrive at a peaceful lake surrounded by trees.")
        blacksmith = Room("Blacksmith", "You enter a blacksmith's forge, filled with tools and weapons.")
        market = Room("Market", "You find yourself in a bustling market filled with shops and stalls.")
        temple = Room("Temple", "You stand in a serene temple. The air is filled with the scent of incense.")
        graveyard = Room("Graveyard", "You walk through a spooky graveyard. It's very quiet.")
        waterfall = Room("Waterfall", "You find a beautiful waterfall cascading into a clear pool below.")
        meadow = Room("Meadow", "You are in a wide, open meadow filled with wildflowers.")
        
        start.add_paths({'north': forest, 'east': village, 'west': mountain})
        forest.add_paths({'south': start, 'east': cave, 'north': garden})
        cave.add_paths({'west': forest, 'north': waterfall})
        mountain.add_paths({'east': start, 'north': castle, 'west': graveyard})
        village.add_paths({'west': start, 'north': castle, 'east': lake, 'south': blacksmith})
        castle.add_paths({'south': village, 'north': dungeon, 'east': library, 'west': market})
        dungeon.add_paths({'south': castle, 'north': treasure})
        treasure.add_paths({'south': dungeon})
        library.add_paths({'west': castle, 'north': tower, 'east': temple})
        tower.add_paths({'south': library})
        garden.add_paths({'south': forest, 'east': lake, 'north': meadow})
        lake.add_paths({'west': garden, 'south': village})
        blacksmith.add_paths({'north': village})
        market.add_paths({'east': castle})
        temple.add_paths({'west': library})
        graveyard.add_paths({'east': mountain})
        waterfall.add_paths({'south': cave})
        meadow.add_paths({'south': garden})

        return {
            'Start': start,
            'Forest': forest,
            'Cave': cave,
            'Mountain': mountain,
            'Village': village,
            'Castle': castle,
            'Dungeon': dungeon,
            'Treasure Room': treasure,
            'Library': library,
            'Tower': tower,
            'Garden': garden,
            'Lake': lake,
            'Blacksmith': blacksmith,
            'Market': market,
            'Temple': temple,
            'Graveyard': graveyard,
            'Waterfall': waterfall,
            'Meadow': meadow
        }

    def move(self, direction):
        next_room = self.current_room.move(direction)
        if next_room:
            self.current_room = next_room
            return True
        else:
            return False

    def pick_item(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            return True
        else:
            return False

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.items.append(item)
            return True
        else:
            return False

    def check_inventory(self):
        return self.inventory

    def get_current_room_details(self):
        return self.current_room.get_details()

    def end_game(self):
        self.is_over = True

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.game = Game()

    def move(self, direction):
        if self.game.move(direction):
            return f'You move {direction}. {self.game.get_current_room_details()}'
        else:
            return "You can't go that way."

    def pick_item(self, item):
        if self.game.pick_item(item):
            return f'You picked up {item}.'
        else:
            return f'There is no {item} here.'

    def drop_item(self, item):
        if self.game.drop_item(item):
            return f'You dropped {item}.'
        else:
            return f'You do not have {item}.'

    def check_inventory(self):
        return f'Inventory: {", ".join(self.game.check_inventory())}'

    def get_status(self):
        return f'Player: {self.name}, Health: {self.health}, {self.game.get_current_room_details()}'

class Adventure:
    def __init__(self):
        self.player = None

    def start_game(self):
