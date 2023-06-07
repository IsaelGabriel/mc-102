game_map: list[list]

class Vector2:
    def __init__(self, coordinates: tuple[int, int]):
        self._coordinates: tuple[int, int] = coordinates
        if self.y < 0: self.y = 0
        if self.x < 0: self.x = 0
    
    @property
    def x(self) -> int:
        return self._coordinates[1]
    
    @x.setter
    def x(self, new_x: int):
        global game_map

        if new_x < 0: new_x = 0
        elif new_x > len(game_map[0]) - 1: new_x = len(game_map[0]) - 1
        self._coordinates = (self._coordinates[0], new_x)

    @property
    def y(self) -> int:
        return self._coordinates[0]
    
    @y.setter
    def y(self, new_y: int):
        global game_map
        
        if new_y < 0: new_y = 0
        elif new_y > len(game_map) - 1: new_y = len(game_map) - 1
        self._coordinates = (new_y, self._coordinates[1])
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, tuple[int, int]):
            self.x += other[1]
            self.y += other[0]


class GameObject:
    def __init__(self):
        self._position = Vector2(0, 0)
        self._id: int = 0

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, new_position: Vector2):
        global game_map

        game_map[self.position.y][self.position.x].remove(self._id)

        self._position = new_position

        game_map[self.position.y][self.position.x].append(self)
        self.update_id()

    def update_id(self):
        self._id = len(game_map[self.position.y][self.position.x]) - 1

class Player(GameObject):
    def __init__(self, hp: int, atk: int, position: Vector2):
        super.__init__()
        self._hp: int = hp
        self._atk: int = atk
        self._position: Vector2 = position

    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, new_hp):
        if new_hp < 0: new_hp = 0
        self._hp = new_hp
        if new_hp == 0:
            self.die()

    @property
    def atk(self) -> int:
        return self._atk

    def move(self):
        direction = Vector2(0, 0)

        if self.y % 2 == 0:
            direction.x = -1
        else:
            direction.x = 1

        on_limit: bool = (direction.x == -1 and self.x == 0)\
              or (direction.x == 1 and self.x == len(game_map[0]) - 1)

        if on_limit:
            direction.x = 0
            direction.y = -1

        self.position += direction
    
    def update(self):
        self.move()
    

    def die(self):
        pass

class Enemy(GameObject):
    def __init__(self, args: list):
        super.__init__()
        self._hp: int = int(args[0])
        self._atk: int = int(args[1])
        self._behaviour: str = args[2]
        self._position: Vector2 = Vector2(tuple(map(int, args[3].split(','))))
    
    @property
    def behaviour(self) -> str:
        return self._behaviour

class Item(GameObject):
    def __init__(self, args: list):
        super.__init__()
        self._name: str = args[0]
        self._behaviour: str = args[1]
        self._position: Vector2 = Vector2(tuple(map(int, args[2].split(','))))
        self._value: int = int(args[3])

    @property
    def behaviour(self) -> str:
        return self._behaviour

def input_coordinates(sep: str = " ") -> Vector2:
    return Vector2(tuple(map(int, input().split(sep))))

def create_game_map(dimensions: Vector2, enemies: list[Enemy], items: list[Item]) -> list[list]:
    game_map = [[[] for columns in range(dimensions.x)] for lines in range(dimensions.y)]

    for enemy in enemies:
        game_map[enemy.position.y][enemy.position.x].append(enemy)
    
    for item in items:
        game_map[item.position.y][item.position.x].append(item)
    
    return game_map

def print_game_map(game_map: list):
    pass

def main():
    global game_map

    initial_hp, initial_dmg = map(int, input().split())
    map_dimensions: Vector2 = input_coordinates()
    player_position: Vector2 = input_coordinates(',')
    exit_position: Vector2 = input_coordinates(',')
    monster_quantity: int = int(input())
    monsters: list[Enemy] = list(map(Enemy, [input().split() for _ in range(monster_quantity)]))
    item_quantity: int = int(input())
    items: list[Item] = list(map(Item, [input().split() for _ in range(item_quantity)]))

    game_map = create_game_map(map_dimensions, monsters, items)

if __name__ == "__main__":
    main()