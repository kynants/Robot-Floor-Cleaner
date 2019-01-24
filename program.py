class Robot:
    def __init__(self, power, distance, button_pressed):            # Object
        self.power = power
        self.distance = distance
        self.button_pressed = button_pressed

    def response(self, power):                                      # Method
        power = input('Turn the robot on? (y/n)')
        if power == 'n' or 'N':
            while power == 'n' or 'N':
                ask_again = input('Robot is off. Quit program? (y/n)')
                if ask_again == 'y' or 'Y':
                    exit()
                else:
                    power = 'y'

    response()