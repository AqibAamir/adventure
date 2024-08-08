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
        name = input("Enter your name: ")
        self.player = Player(name)
        print(self.player.get_status())

    def play(self):
        self.start_game()
        while True:
            command = input("> ").split()
            if command[0] in ["go", "move"]:
                direction = command[1]
                print(self.player.move(direction))
            elif command[0] == "pick":
                item = command[1]
                print(self.player.pick_item(item))
            elif command[0] == "drop":
                item = command[1]
                print(self.player.drop_item(item))
            elif command[0] == "inventory":
                print(self.player.check_inventory())
            elif command[0] == "status":
                print(self.player.get_status())
            elif command[0] in ["quit", "exit"]:
                break
            else:
                print("Unknown command.")

class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def interact(self):
        return f'{self.name}: {self.description}'

class GameWithNPC(Game):
    def create_rooms(self):
        rooms = super().create_rooms()
        rooms['Village'].npc = NPC("Villager", "Hello stranger, welcome to our village.")
        rooms['Castle'].npc = NPC("Guard", "You may enter the castle.")
        rooms['Dungeon'].npc = NPC("Prisoner", "Please help me escape.")
        rooms['Library'].npc = NPC("Librarian", "Shh... keep your voice down. This is a library.")
        rooms['Tower'].npc = NPC("Sage", "I can see the future from here.")
        rooms['Garden'].npc = NPC("Gardener", "Do you like the flowers?")
        rooms['Blacksmith'].npc = NPC("Blacksmith", "I can craft weapons for you.")
        rooms['Market'].npc = NPC("Merchant", "Take a look at my wares.")
        rooms['Temple'].npc = NPC("Priest", "May the gods watch over you.")
        rooms['Graveyard'].npc = NPC("Ghost", "Boo! Just kidding. Welcome to the graveyard.")
        rooms['Waterfall'].npc = NPC("Fisherman", "The fish are biting today!")
        rooms['Meadow'].npc = NPC("Shepherd", "The sheep are grazing peacefully.")
        return rooms

class PlayerWithNPC(Player):
    def interact(self):
        if hasattr(self.game.current_room, 'npc'):
            return self.game.current_room.npc.interact()
        else:
            return "There's no one here to interact with."

class AdventureWithNPC(Adventure):
    def start_game(self):
        name = input("Enter your name: ")
        self.player = PlayerWithNPC(name)
        print(self.player.get_status())

    def play(self):
        self.start_game()
        while True:
            command = input("> ").split()
            if command[0] in ["go", "move"]:
                direction = command[1]
                print(self.player.move(direction))
            elif command[0] == "pick":
                item = command[1]
                print(self.player.pick_item(item))
            elif command[0] == "drop":
                item = command[1]
                print(self.player.drop_item(item))
            elif command[0] == "inventory":
                print(self.player.check_inventory())
            elif command[0] == "status":
                print(self.player.get_status())
            elif command[0] == "interact":
                print(self.player.interact())
            elif command[0] == "help":
                print("Commands: go/move [direction], pick [item], drop [item], inventory, status, interact, help, quit/exit")
            elif command[0] in ["quit", "exit"]:
                break
            else:
                print("Unknown command.")

class PuzzleRoom(Room):
    def __init__(self, name, description, puzzle, solution):
        super().__init__(name, description)
        self.puzzle = puzzle
        self.solution = solution
        self.solved = False


    def attempt_puzzle(self, answer):
        if answer.lower() == self.solution.lower():
            self.solved = True
            return "You solved the puzzle!"
        else:
            return "That's not correct."

class GameWithPuzzles(GameWithNPC):
    def create_rooms(self):
        rooms = super().create_rooms()
        puzzle_room = PuzzleRoom("Puzzle Room", "A room with a challenging puzzle.", "What has keys but can't open locks?", "piano")
        rooms['Forest'].add_paths({'north': puzzle_room})
        puzzle_room.add_paths({'south': rooms['Forest']})
        rooms['Puzzle Room'] = puzzle_room
        return rooms

class PlayerWithPuzzles(PlayerWithNPC):
    def attempt_puzzle(self, answer):
        if isinstance(self.game.current_room, PuzzleRoom):
            return self.game.current_room.attempt_puzzle(answer)
        else:
            return "There's no puzzle to solve here."

class AdventureWithPuzzles(AdventureWithNPC):
    def start_game(self):
        name = input("Enter your name: ")
        self.player = PlayerWithPuzzles(name)
        print(self.player.get_status())

    def play(self):
        self.start_game()
        while True:
            command = input("> ").split()
            if command[0] in ["go", "move"]:
                direction = command[1]
                print(self.player.move(direction))
            elif command[0] == "pick":
                item = command[1]
                print(self.player.pick_item(item))
            elif command[0] == "drop":
                item = command[1]

print(self.player.drop_item(item))
            elif command[0] == "inventory":
                print(self.player.check_inventory())
            elif command[0] == "status":
                print(self.player.get_status())
            elif command[0] == "interact":
                print(self.player.interact())
            elif command[0] == "solve":
                answer = " ".join(command[1:])
                print(self.player.attempt_puzzle(answer))
            elif command[0] == "help":
                print("Commands: go/move [direction], pick [item], drop [item], inventory, status, interact, solve [answer], help, quit/exit")
            elif command[0] in ["quit", "exit"]:
                break
            else:
                print("Unknown command.")

class BattleRoom(Room):
    def __init__(self, name, description, enemy):
        super().__init__(name, description)
        self.enemy = enemy
        self.enemy_health = 50

    def battle(self, player):
        while self.enemy_health > 0 and player.health > 0:
            player_damage = random.randint(5, 15)
            enemy_damage = random.randint(5, 15)
            self.enemy_health -= player_damage
            player.health -= enemy_damage
            print(f'You hit the {self.enemy} for {player_damage} damage.')
            print(f'The {self.enemy} hits you for {enemy_damage} damage.')
            if self.enemy_health <= 0:
                return f'You defeated the {self.enemy}!'
            if player.health <= 0:
                player.game.end_game()
                return 'You have been defeated!'
        return 'The battle is over.'

class GameWithBattles(GameWithPuzzles):
    def create_rooms(self):
        rooms = super().create_rooms()
        battle_room = BattleRoom("Battle Room", "A room with a fierce enemy.", "Goblin")
        rooms['Cave'].add_paths({'north': battle_room})
        battle_room.add_paths({'south': rooms['Cave']})
        rooms['Battle Room'] = battle_room
        return rooms

class PlayerWithBattles(PlayerWithPuzzles):
    def battle(self):
        if isinstance(self.game.current_room, BattleRoom):
            return self.game.current_room.battle(self)
        else:
            return "There's no one to battle here."

class AdventureWithBattles(AdventureWithPuzzles):
    def start_game(self):
        name = input("Enter your name: ")
        self.player = PlayerWithBattles(name)
        print(self.player.get_status())

    def play(self):
        self.start_game()
        while not self.player.game.is_over:
            command = input("> ").split()
            if command[0] in ["go", "move"]:
                direction = command[1]
                print(self.player.move(direction))
            elif command[0] == "pick":
                item = command[1]
                print(self.player.pick_item(item))
            elif command[0] == "drop":
                item = command[1]
                print(self.player.drop_item(item))
            elif command[0] == "inventory":
                print(self.player.check_inventory())
            elif command[0] == "status":
                print(self.player.get_status())
            elif command[0] == "interact":
                print(self.player.interact())
            elif command[0] == "solve":
                answer = " ".join(command[1:])
                print(self.player.attempt_puzzle(answer))
            elif command[0] == "battle":
                print(self.player.battle())
            elif command[0] == "help":
                print("Commands: go/move [direction], pick [item], drop [item], inventory, status, interact, solve [answer], battle, help, quit/exit")
            elif command[0] in ["quit", "exit"]:
                break
            else:
                print("Unknown command.")

class MagicRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.spellbook = "Ancient Spellbook"
        self.items.append(self.spellbook)

    def read_spellbook(self):
        return "You read the spellbook and learn powerful magic."

class GameWithMagic(GameWithBattles):
    def create_rooms(self):
