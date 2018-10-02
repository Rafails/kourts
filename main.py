import sys

from boarding_cards import boarding_cards
from transportations import Bus, Plane, Train

def get_class(str):
    return getattr(sys.modules[__name__], str)

def validate_boarding_cards(boarding_cards):
    departures = set()
    arrivals = set()
    for card in boarding_cards:
        departures.add(card['departure'])
        arrivals.add(card['arrival'])
        if boarding_cards.count(card) > 1:
            return False
    if len(departures - arrivals) >= 2:
        return False
    return True

def sort_boarding_cards(boarding_cards):
    sorted_cards = [boarding_cards.pop()]
    while (len(boarding_cards) > 0):
        for card in boarding_cards:
            if sorted_cards[-1]['arrival'] == card['departure']:
                boarding_cards.remove(card)
                sorted_cards.append(card)
            elif sorted_cards[0]['departure'] == card['arrival']:
                boarding_cards.remove(card)
                sorted_cards.insert(0, card)

    return sorted_cards

def execute(boarding_cards):
    is_valid = validate_boarding_cards(boarding_cards)
    message_as_array = []
    if is_valid:
        sorted_boarding_cards = sort_boarding_cards(boarding_cards)
        for boarding_card in sorted_boarding_cards:
            card_class = get_class(boarding_card['transportation'])
            message_as_array.append(card_class().get_message(boarding_card))
        message_as_array.append('You have arrived at your final destination.')
        return {
            'status': True,
            'sorted_boarding_cards': sorted_boarding_cards,
            'message': '\n'.join(message_as_array)
        }
    else:
        return {
            'status': False,
            'error': 'Bad request data'
        }

if __name__ == "__main__":
    print(execute(boarding_cards))
