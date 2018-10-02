class Bus():
    def get_message(self, data):
        return 'Take the airport bus from {departure} to {arrival}. No seat assignment.'.format(**data)

class Plane():
    def get_message(self, data):
        baggage = data.get('baggage', None)
        if baggage:
            return ('From {departure}, take flight {transportation_id} to {arrival}. Gate {gate}, seat {seat}.'
                    'Baggage drop at ticket counter {baggage}.').format(**data)
        return ('From {departure}, take flight {transportation_id} to {arrival}. Gate {gate}, seat {seat}.'
                'Baggage will we automatically transferred from your last leg.').format(**data)

class Train():
    def get_message(self, data):
        return 'Take train {transportation_id} from {departure} to {arrival}. Sit in seat {seat}.'.format(**data)
