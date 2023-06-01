from dataclasses import dataclass


@dataclass
class Part:
    weakness: str
    max_dmg: int
    coordinates: tuple[int]

    def calculate_damage(self, damage_type: str, coordinates: tuple[int]) -> int:
        distance = (abs(self.coordinates[0] - coordinates[0]) + abs(self.coordinates[1] - coordinates[1]))
        damage = self.max_dmg - distance
        if damage < 0: return 0

        if self.weakness == 'todas' or damage_type == self.weakness:
            return damage
        else:
            return damage // 2


@dataclass
class Enemy:
    _hp: int
    atk: int
    _parts: dict[str, Part]

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def parts(self) -> dict:
        return self._parts
    
    @parts.setter
    def parts(self, new_parts: dict):
        if len(self._parts.keys()) < len(new_parts.keys()):
            new_keys: list[str] = list(set(new_parts.keys()) - set(self._parts.keys()))
            for key in new_keys:
                if type(new_parts[key]) == Part:
                    self._parts[key] = new_parts[key]
    
    def take_damage(self, part_name: str, arrow_type: str, coordinates: tuple[int]):
        if part_name not in self._parts.keys(): return

        self._hp -= self._parts[part_name].calculate_damage(arrow_type, coordinates)



def main():
    
    max_hp: int = int(input())
    current_hp: int = max_hp

    total_arrows: dict = {}

    arrow_line: str = input().split()
    for i in range(0, len(arrow_line), 2):
        total_arrows[arrow_line[i]] = int(arrow_line[i + 1])
    del(arrow_line)

    total_enemies: int = int(input())
    
    wave_enemy_count: int = 0
    current_wave: int = 0

    while wave_enemy_count < total_enemies and current_hp > 0:
        wave_total = int(input())
        wave_enemy_count += wave_total
        enemies: list[Enemy] = []

        for _ in range(wave_total):
            line: list[str] = input().split()
            hp: int = int(line[0])
            atk: int = int(line[1])
            number_of_parts: int = int(line[2])
            parts: dict[Part] = {}

            for i in range(number_of_parts):
                line: list[str] = input().split(", ")
                weakness: str = line[1]
                max_dmg: str = int(line[2])
                coordinates: tuple[int] = tuple((int(line[3]), int(line[4])))

                parts[line[0]]: Part = Part(weakness, max_dmg, coordinates)
            
            enemies.append(Enemy(hp, atk, parts))

        print(f'Combate {current_wave}, vida = {current_hp}')
        criticals: list[dict] = [{} for _ in enemies]

        arrows_used: dict = {}

        while (not all(enemy.hp <= 0 for enemy in enemies)) and current_hp > 0 and sum(arrows_used.values()) != sum(total_arrows.values()):
            for _ in range(3):
                attack = input().split(", ")
                enemy_index = int(attack[0])
                part: str = attack[1]
                arrow_type: str = attack[2]
                coordinates: tuple[int] = tuple((int(attack[3]), int(attack[4])))
                enemies[enemy_index].take_damage(part, arrow_type, coordinates)

                if arrow_type in arrows_used.keys():
                    arrows_used[arrow_type] += 1
                else:
                    arrows_used[arrow_type]: int = 1

                if coordinates == enemies[enemy_index].parts[part].coordinates:
                    if coordinates in criticals[enemy_index].keys():
                        criticals[enemy_index][coordinates] += 1
                    else:
                        criticals[enemy_index][coordinates]: int = 1

                if enemies[enemy_index].hp <= 0:
                    print(f"Máquina {str(enemy_index)} derrotada")

                    if all(enemy.hp <= 0 for enemy in enemies):
                        break
                
                if sum(arrows_used.values()) == sum(total_arrows.values()):
                    break

            
            for enemy in enemies:
                if enemy.hp <= 0: continue
                current_hp -= enemy.atk
                if current_hp < 0: current_hp = 0

        print(f"Vida após o combate = {current_hp}")

        if not current_hp > 0: 
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            return
        elif sum(arrows_used.values()) == sum(total_arrows.values()):
            print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
            return
        
        print("Flechas utilizadas:")
        for arrow, total in total_arrows.items():
            if arrow not in arrows_used.keys(): continue
            print(f"- {arrow}: {str(arrows_used[arrow])}/{str(total)}")
        
        if not all(len(critical_list.keys()) == 0 for critical_list in criticals):
            print("Críticos acertados:")
            for enemy_index in range(len(criticals)):
                if len(criticals[enemy_index].keys()) == 0: continue
                print(f"Máquina {str(enemy_index)}:")
                for part in enemies[enemy_index].parts.values():
                    if part.coordinates in criticals[enemy_index].keys():
                        coordinates = part.coordinates
                        print(f"- {str(coordinates)}: {str(criticals[enemy_index][coordinates])}x")

        if current_hp != max_hp:
            current_hp += max_hp//2
            if current_hp > max_hp: current_hp = max_hp
        
        current_wave += 1

    print("Aloy provou seu valor e voltou para sua tribo.")
    return


if __name__ == "__main__":
    main()