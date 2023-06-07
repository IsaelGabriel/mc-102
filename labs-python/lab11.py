class Vector2:
    def __init__(self, coordinates: tuple[int, int]):
        self._coordinates: tuple[int, int] = coordinates
    
    @property
    def x(self) -> int:
        return self._coordinates[1]
    
    @x.setter
    def x(self, new_x: int):
        if new_x < 0: new_x = 0
        self._coordinates = (self._coordinates[0], new_x)

    @property
    def y(self) -> int:
        return self._coordinates[0]
    
    @y.setter
    def y(self, new_y: int):
        if new_y < 0: new_y = 0
        self._coordinates = (new_y, self._coordinates[1])

class Player:
    def __init__(self, hp: int, atk: int, position: Vector2):
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

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, new_position):
        self._position = new_position

    def die(self):
        pass

class Enemy:
    def __init__(self, args: list):
        self._hp: int = int(args[0])
        self._atk: int = int(args[1])
        self._behaviour: str = args[2]
        self._position: Vector2 = Vector2(tuple(map(int, args[3].split(','))))
    
    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, new_position: Vector2):
        self._position = new_position

class Item:
    def __init__(self, args: list):
        self._name: str = args[0]
        self._behaviour: str = args[1]
        self._position: Vector2 = Vector2(tuple(map(int, args[2].split(','))))
        self._value: int = int(args[3])

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, new_position: Vector2):
        self._position = new_position

def input_coordinates(sep: str = " ") -> Vector2:
    return Vector2(tuple(map(int, input().split(sep))))

def formatted_game_map(dimensions: Vector2, enemies: list[Enemy], items: list[Item]) -> list[list]:
    game_map = [[[] for columns in range(dimensions.x)] for lines in range(dimensions.y)]

    for enemy in enemies:
        game_map[enemy.position.y][enemy.position.x].append("E")
    
    for item in items:
        game_map[item.position.y][item.position.x].append("I")
    
    return game_map

def print_game_map(game_map: list):
    pass

def main():
    initial_hp, initial_dmg = map(int, input().split())
    map_dimensions: Vector2 = input_coordinates()
    player_position: Vector2 = input_coordinates(',')
    exit_position: Vector2 = input_coordinates(',')
    monster_quantity: int = int(input())
    monsters: list[Enemy] = list(map(Enemy, [input().split() for _ in range(monster_quantity)]))
    item_quantity: int = int(input())
    items: list[Item] = list(map(Item, [input().split() for _ in range(item_quantity)]))

    game_map = formatted_game_map(map_dimensions, monsters, items)

if __name__ == "__main__":
    main()