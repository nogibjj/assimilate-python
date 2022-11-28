"""
An object oriented soccer player class
"""

class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
        self.all_positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']

#pylint: disable=useless-parent-delegation
class PlayerPhysicalAttributes(Player):
    def __init__(self, name, number, position):
        super().__init__(name, number, position)

    def average_weight_by_position(self):
        """Retuns the average weight of players by position in KG"""
        if self.position == 'Goalkeeper':
            return 80
        elif self.position == 'Defender':
            return 75
        elif self.position == 'Midfielder':
            return 70
        elif self.position == 'Forward':
            return 65
        else:
            return 0

    #create a method that automatically returns average weight by position
    @property
    def weight(self):
        return self.average_weight_by_position()