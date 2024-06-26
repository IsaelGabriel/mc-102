game_map: list[list]
enemies: list
items: list

class Vector2:
    def __init__(self, coordinates: tuple[int, int]):
        self._coordinates: tuple[int, int] = coordinates
    
    @property
    def x(self) -> int:
        return self._coordinates[1]
    
    @x.setter
    def x(self, new_x: int):
        global game_map

        self._coordinates = (self._coordinates[0], new_x)

    @property
    def y(self) -> int:
        return self._coordinates[0]
    
    @y.setter
    def y(self, new_y: int):
        global game_map
        
        self._coordinates = (new_y, self._coordinates[1])
    
    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2((other.y + self.y, other.x + self.x))
        elif isinstance(other, tuple[int, int]):
            return Vector2((other[0] + self.y, other[1] + self.x))

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    def __str__(self) -> str:
        return str(self._coordinates)


class GameObject:
    def __init__(self):
        global game_map

        self._position = Vector2((0, 0))
        self._id: int = 0
        self.active = True

        game_map[0][0].append(self)
        self.update_id()

    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, new_position: Vector2):
        global game_map

        game_map[self._position.y][self._position.x].remove(self)

        self._position.x = min(max(0, new_position.x), len(game_map[0]) - 1)
        self._position.y = min(max(0, new_position.y), len(game_map) - 1)

        game_map[self._position.y][self._position.x].append(self)
        self.update_id()

    def update_id(self):
        self._id = len(game_map[self.position.y][self.position.x]) - 1


class Enemy(GameObject):
    def __init__(self, args: list):
        super().__init__()
        self._hp: int = int(args[0])
        self._atk: int = int(args[1])
        self._behaviour: str = args[2]
        self.position = Vector2(tuple(map(int, args[3].split(','))))
        
    
    @property
    def behaviour(self) -> str:
        return self._behaviour
    
    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, new_hp):
        if new_hp < 0: new_hp = 0
        self._hp = new_hp
        if self._hp == 0:
            self.active = False

    @property
    def atk(self) -> int:
        return self._atk

    def update(self):
        if not self.active: return
        direction = Vector2((0, 0))
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
        super().__init__()
        self._name: str = args[0]
        self._behaviour: str = args[1]
        self.position = Vector2(tuple(map(int, args[2].split(','))))
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

        super().__init__()
        self._hp: int = hp
        self._atk: int = atk
        self.position = position
        self._exit: Vector2 = exit_position
        self._got_to_bottom: bool = False

        game_map[position.y][position.x].append(self)
        self.update_id()

    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, new_hp: int):
        if self._hp == 0: return

        if new_hp <= 0:
            new_hp = 0
            self.active = False
        self._hp = new_hp

    @property
    def atk(self) -> int:
        return self._atk

    @atk.setter
    def atk(self, new_atk: int):
        self._atk = max(1, new_atk)

    def move(self):
        global game_map

        direction = Vector2((0, 0))

        if self._got_to_bottom:
            if self.position.y % 2 == 0:
                direction.x = -1
            else:
                direction.x = 1

            on_limit: bool = (direction.x == -1 and self.position.x == 0)\
                or (direction.x == 1 and self.position.x == len(game_map[0]) - 1)

            if on_limit:
                direction.x = 0
                direction.y = -1
        else:
            direction.y = 1


        self.position += direction
        if direction.y == 1:
            if self.position.y == len(game_map) - 1:
                self._got_to_bottom = True
    
    def sorted_objects(self) -> list[GameObject]:
        global enemies, items

        obj_list: list[GameObject] = []

        for item in items:
            if self.position == item.position and item.active:
                obj_list.append(item)

        for enemy in enemies:
            if self.position == enemy.position and enemy.active:
                obj_list.append(enemy)

        return obj_list

    def fight_enemy(self, enemy: Enemy):
        dmg_caused: int = min(enemy.hp, self.atk)

        enemy.hp -= dmg_caused
        print(f"O Personagem deu {dmg_caused} de dano ao monstro na posicao {enemy.position}")
        
        if enemy.active:
            dmg_taken: int = min(self.hp, enemy.atk)

            self.hp -= dmg_taken
            
            print(f"O Monstro deu {dmg_taken} de dano ao Personagem. Vida restante = {self.hp}")

            if self.hp == 0: 
                self.die()

    def update(self):
        global game_map

        collisions = self.sorted_objects()

        for game_obj in collisions:
            if not self.active: break
            if not game_obj.active: continue

            if isinstance(game_obj, Item):
                print(game_obj)
                if game_obj.behaviour == 'v':
                    self.hp += game_obj.value
                    if self.hp == 0:
                        self.die()

                elif game_obj.behaviour == 'd':
                    self.atk += game_obj.value
                game_obj.active = False
            if isinstance(game_obj, Enemy):
                self.fight_enemy(game_obj)

    def die(self):
        self.active = False

def input_coordinates(sep: str = " ") -> Vector2:
    return Vector2(tuple(map(int, input().split(sep))))

def print_game_map(player: Player, exit_position: Vector2):
    global game_map, enemies, items
    
    text: str = ""
    
    current_position: Vector2 = Vector2((0, 0))

    for y in range(len(game_map)):
        current_position.y = y
        line: list = []
        for x in range(len(game_map[y])):
            current_position.x = x
            if player.position == current_position:
                if player.active:
                    line.append('P')
                else:
                    line.append('X')
            elif exit_position == current_position:
                line.append('*')
            else:
                has_obj: bool = False

                for game_obj in (items + enemies)[::-1]:
                    if game_obj.active and game_obj.position == current_position:
                        line.append(game_obj.behaviour)
                        has_obj = True
                        break

                if not has_obj: line.append('.')

        text += " ".join(line) + "\n"

    print(text)


def main():
    global game_map, enemies, items

    initial_hp, initial_atk = map(int, input().split())
    map_dimensions: Vector2 = input_coordinates()

    game_map = [[[] for column in range(map_dimensions.x)] for line in range(map_dimensions.y)]

    player_position: Vector2 = input_coordinates(',')
    exit_position: Vector2 = input_coordinates(',')
    enemy_quantity: int = int(input())
    enemies = list(map(Enemy, [input().split() for _ in range(enemy_quantity)]))
    item_quantity: int = int(input())
    items = list(map(Item, [input().split() for _ in range(item_quantity)]))

    player = Player(initial_hp, initial_atk, player_position, exit_position)

    print_game_map(player, exit_position)

    while player.active:
        player.move()

        for enemy in enemies:
            if enemy.active:
                enemy.update()
            else:
                enemies.remove(enemy)
        
        if player.position == exit_position:
            print_game_map(player, exit_position)
            player.active = False  
            print("Chegou ao fim!")
        else:
            player.update()
            print_game_map(player, exit_position)



if __name__ == "__main__":
    main()