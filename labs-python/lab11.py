class enemy:
    def __init__(self, args: list):
        self._hp: int = int(args[0])
        self._atk: int = int(args[1])
        self._behaviour: str = args[2]
        self._position: tuple[int] = tuple(map(int, args[3].split(',')))

class item:
    def __init__(self, args: list):
        self._name: str = args[0]
        self._behaviour: str = args[1]
        self._position: tuple[int] = tuple(map(int, args[2].split(',')))
        self._value: int = int(args[3])

def input_coordinates(sep: str = " ") -> tuple[int]:
    return tuple(map(int, input().split(sep)))

def main():
    initial_hp, initial_dmg = map(int, input().split())
    map_dimensions: tuple[int] = input_coordinates()
    inital_position: tuple[int] = input_coordinates(',')
    exit_position: tuple[int] = input_coordinates(',')
    monster_quantity: int = int(input())
    monsters: list[enemy] = list(map(enemy, [input().split() for _ in range(monster_quantity)]))
    item_quantity: int = int(input())
    items: list[item] = list(map(item, [input().split() for _ in range(item_quantity)]))

    

if __name__ == "__main__":
    main()