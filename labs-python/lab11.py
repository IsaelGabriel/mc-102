class Vector2:
    def __init__(self, i: int, j: int):
        self._coordinates: tuple[int, int] = (i, j)
    
    @property
    def x(self) -> int:
        return self._coordinates[1]
    
    @x.setter
    def x(self, new_x: int):
        self._coordinates = (self._coordinates[0], new_x)

    @property
    def y(self) -> int:
        return self._coordinates[0]
    
    @y.setter
    def y(self, new_y: int):
        self._coordinates = (new_y, self._coordinates[1])

class Enemy:
    def __init__(self, args: list):
        self._hp: int = int(args[0])
        self._atk: int = int(args[1])
        self._behaviour: str = args[2]
        self._position: tuple[int] = tuple(map(int, args[3].split(',')))
    
    @property
    def position(self) -> tuple[int, int]:
        return self._position
    
    @position.setter
    def position(self, new_position: tuple[int, int]):
        self._position = tuple(new_position[0], new_position[1])

class Item:
    def __init__(self, args: list):
        self._name: str = args[0]
        self._behaviour: str = args[1]
        self._position: tuple[int] = tuple(map(int, args[2].split(',')))
        self._value: int = int(args[3])

    @property
    def position(self) -> tuple[int, int]:
        return self._position
    
    @position.setter
    def position(self, new_position: tuple[int, int]):
        self._position = tuple(new_position[0], new_position[1])

def input_coordinates(sep: str = " ") -> tuple[int]:
    return tuple(map(int, input().split(sep)))

def formatted_game_map(dimensions: tuple[int], enemies: list[Enemy], items: list[Item]) -> list[list]:
    game_map = [[[] for columns in range(dimensions[1])] for lines in range(dimensions[0])]

    for enemy in enemies:
        game_map[enemy.position[0]][enemy.position[1]].append("E")
    
    for item in items:
        game_map[item.position[0]][item.position[1]].append("I")

def main():
    initial_hp, initial_dmg = map(int, input().split())
    map_dimensions: tuple[int] = input_coordinates()
    inital_position: tuple[int] = input_coordinates(',')
    exit_position: tuple[int] = input_coordinates(',')
    monster_quantity: int = int(input())
    monsters: list[Enemy] = list(map(Enemy, [input().split() for _ in range(monster_quantity)]))
    item_quantity: int = int(input())
    items: list[Item] = list(map(Item, [input().split() for _ in range(item_quantity)]))

    

if __name__ == "__main__":
    main()