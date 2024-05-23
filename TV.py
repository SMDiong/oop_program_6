# Diong, Shan Marc C.
# BSCPE 1-2

# Create the class named TV
class TV:
    # Constructor for channel, volume level, and on
    def __init__(self):
        self.channel = int
        self.volume_level = int
        self.on = False

    # Creating method for turn on and off
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    # Creating method for getting the channel
    def get_channel(self):
        return self.channel

    # Creating method for setting the channel ranging from 1 to 120
    def set_channel(self, channel_number):
        if 1 <= channel_number <= 120:
            self.channel = channel_number

    # Creating method for getting the volume

    # Creating method for setting the volume ranging from 1 to 7

    # Creating method for switching up the channel

    # Creating method for switching down the channel

    # Creating method for increasing volume

    # Creating method for decreasing volume
