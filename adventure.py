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
