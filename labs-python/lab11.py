game_map: list[list]
enemies: list
items: list

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

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


class GameObject:
    def __init__(self):
        self._position = Vector2(0, 0)
        self._id: int = 0
        self.active = True

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
    
    def update(self):
        direction = Vector2(0, 0)
        match self._behaviour:
            case 'U':
                direction.y = -1
            case 'D':
                direction.y = 1
            case 'L':
                direction.x = -1
            case 'R':
                direction.x = 1
        
        self.position += direction

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
    
    @property
    def value(self) -> int:
        return self._value

    def __str__(self) -> str:
        return f"[{self._behaviour}]Personagem adquiriu o objeto {self._name} com status de {str(self._value)}"

class Player(GameObject):
    def __init__(self, hp: int, atk: int, position: Vector2, exit_position: Vector2):
        global game_map

        super.__init__()
        self._hp: int = hp
        self._atk: int = atk
        self._position: Vector2 = position
        self._exit: Vector2 = exit_position

        game_map[position.y][position.x].append(self)
        self.update_id()

    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, new_hp: int):
        if new_hp < 0: new_hp = 0
        self._hp = new_hp
        if new_hp == 0:
            self.die()

    @property
    def atk(self) -> int:
        return self._atk

    @atk.setter
    def atk(self, new_atk: int):
        self._atk = max(1, new_atk)

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
    
    def sorted_objects(self) -> list[GameObject]:
        global enemies, items

        obj_list: list[GameObject] = []

        for item in items:
            if self.positon == item.position:
                obj_list.append(item)

        for enemy in enemies:
            if self.position == enemy.position:
                obj_list.append(enemy)

        return obj_list

    def update(self):
        global game_map
        
        self.move()

        collisions = self.sorted_objects()

        for game_obj in collisions:
            if not game_obj.active: continue

            if isinstance(game_obj, Item):
                print(game_obj)
                if game_obj.behaviour == 'v':
                    self.hp += game_obj.value
                elif game_obj.behaviour == 'd':
                    self.atk += game_obj.value
                game_obj.active = False

    def die(self):
        pass

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
    global game_map, enemies, items

    initial_hp, initial_atk = map(int, input().split())
    map_dimensions: Vector2 = input_coordinates()
    player_position: Vector2 = input_coordinates(',')
    exit_position: Vector2 = input_coordinates(',')
    enemy_quantity: int = int(input())
    enemies: list[Enemy] = list(map(Enemy, [input().split() for _ in range(enemy_quantity)]))
    item_quantity: int = int(input())
    items: list[Item] = list(map(Item, [input().split() for _ in range(item_quantity)]))


    game_map = create_game_map(map_dimensions, enemies, items)

    player = Player(initial_hp, initial_atk, player_position)
    
    game_active: bool = True

    while game_active:
        pass

if __name__ == "__main__":
    main()