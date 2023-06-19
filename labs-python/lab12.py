suits: dict = {
    'O': 1,
    'E': 2,
    'C': 3,
    'P': 4
}
values: list = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
stack: list = []

class Card:
    def __init__(self, text):
        self.value = text[0:-1]
        self.suit = text[-1]

    def __str__(self):
        return str(self.value) + str(self.suit)

    def __lt__(self, other) -> bool:
        '''Operações de comparação <'''
        if not isinstance(other, self.__class__): return False

        global suits

        if self.value == other.value:
            return suits[self.suit] < suits[other.suit]
        elif self.value.isdigit() and other.value.isdigit():
            return int(self.value) < int(other.value)
        elif self.value == 'A':
            '''Não há valores menores que A'''
            return True
        elif other.value == 'A':
            '''Não há valores menores que A'''
            return False
        elif self.value.isdigit():
            '''O valor de other está dentro do conjunto (J, Q, K)'''
            return True
        elif other.value.isdigit():
            '''O valor desta carta está no conjunto (J, Q, K)'''
            return False
        else:
            '''Opcoes possiveis: J, Q, K'''
            if self.value == 'J':
                '''Não há opção de valor menor que J'''
                return True
            elif self.value == 'K':
                '''Não há opção de valor maior que K'''
                return False
            else:
                '''Caso o valor de other não seja K, ele será J, portanto menor que Q'''
                return other.value == 'K'
    
    def __gt__(self, other) -> bool:
        '''Operações de comparação >'''
        if not isinstance(other, self.__class__): return False

        global suits

        if self.value == other.value:
            return suits[self.suit] > suits[other.suit]
        elif self.value.isdigit() and other.value.isdigit():
            return int(self.value) > int(other.value)
        elif self.value == 'A':
            '''Não há valores menores que A'''
            return False
        elif other.value == 'A':
            '''Não há valores menores que A'''
            return True
        elif self.value.isdigit():
            '''O valor de other está dentro do conjunto (J, Q, K)'''
            return False
        elif other.value.isdigit():
            '''O valor desta carta está no conjunto (J, Q, K)'''
            return True
        else:
            '''Opcoes possiveis: J, Q, K'''
            if self.value == 'J':
                '''Não há opção de valor menor que J'''
                return False
            elif self.value == 'K':
                '''Não há opção de valor maior que K'''
                return True
            else:
                '''Caso o valor de other não seja J, ele será K, portanto maior que Q'''
                return other.value == 'J'

    @staticmethod
    def same_value(card_1, card_2) -> bool:
        if not isinstance(card_1, Card) or not isinstance(card_2, Card): return False

        return card_1.value == card_2.value


def sorted_card_list(l: list) -> list[Card]:
    if len(l) <= 1: return l.copy()
    
    sorted_l = l.copy()

    for i in range(len(sorted_l) - 1):
        for j in range(len(sorted_l) - 1, i, -1):
            if sorted_l[j] < sorted_l[i]:
                sorted_l[i], sorted_l[j] = sorted_l[j], sorted_l[i]

    return sorted_l 


def all_have_cards(player_cards: list[list[Card]]) -> bool:
    for player_hand in player_cards:
        if len(player_hand) == 0: return False
    return True


def print_player_hands(player_cards: list[list[Card]]):
    global stack

    for i in range(len(player_cards)):
        print(f"Jogador {i + 1}")
        print("Mão: " + " ".join(list(map(str, player_cards[i]))))

    print(f"Pilha: {list(map(str, stack))}" if len(stack) > 0 else "Pilha:")


def get_card_value_index(value: str) -> int:
    global values
    if len(values) == 0: return -1
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left+right) // 2
        if values[middle] == value:
            return middle
        elif Card(values[middle] + 'O') < Card(value + 'O'):
            left += 1
        else:
            right -= 1

    return -1


def correct_cards_index(player_hand: list[Card], last_on_stack: str) -> int:
    if last_on_stack == '': return -1
    stack_index = get_card_value_index(last_on_stack)
    for i in range(-1, -(len(player_hand) + 1), -1):
        if get_card_value_index(player_hand[i].value) >= stack_index:
            return i
    
    return -1


def get_discard_list(player_hand: list[Card], last_on_stack: str) -> list:
    i = correct_cards_index(player_hand, last_on_stack)
    l = [player_hand.pop(i)]
    
    while len(l) < 4 and abs(i) <= len(player_hand):
        if Card.same_value(l[0], player_hand[i]):
            l.append(player_hand.pop(i))
        else:
            return l
        
    return l


def main():
    global stack, values

    player_count: int = int(input())
    player_cards: list = [list(map(Card, input().split(', '))) for p in range(player_count)]
    challenge_index: int = int(input())
    challenge_count: int = 0
    last_on_stack: str = ''

    for i in range(len(player_cards)):
        player_cards[i] = sorted_card_list(player_cards[i])[::-1]

    print_player_hands(player_cards)

    current_player = 0
    while all_have_cards(player_cards):

        
        player_cards[current_player] = sorted_card_list(player_cards[current_player])[::-1]
        discard_list = get_discard_list(player_cards[current_player], last_on_stack)
        stack += discard_list.copy()

        if get_card_value_index(last_on_stack) < get_card_value_index(discard_list[0].value):
            last_on_stack = discard_list[0].value

        print(f'[Jogador {current_player + 1}] {len(discard_list)} carta(s) {last_on_stack}')
        print('Pilha: ' + ' '.join(list(map(str, stack))))

        current_player += 1
        if current_player >= player_count:
            current_player = 0

        challenge_count += 1

        if challenge_count == challenge_index:
            print(f"Jogador {current_player + 1} duvidou.")

            affected_player = current_player - 1 if last_on_stack != stack[-1].value else current_player

            player_cards[affected_player] += stack.copy()
            player_cards[affected_player] = sorted_card_list(player_cards[affected_player])[::-1]
            stack = []
            last_on_stack = ''

            print_player_hands(player_cards)

            challenge_count = 0

    for i in range(len(player_cards)):
        if len(player_cards[i]) == 0:
            print(f"Jogador {i + 1} é o vencedor!")


if __name__ == "__main__":
    main()