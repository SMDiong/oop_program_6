# Diong, Shan Marc C.
# BSCPE 1-2

# Create the class named TV
class TV:
    # Constructor for channel, volume level, and on
    def __init__(self):
        self.channel = int
        self.volume_level = int
        self.on = False

    # Creating method for turn on
    def turn_on(self):
        self.on = True

    # Creating method for turn off
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
    def get_volume(self):
        return self.volume_level

    # Creating method for setting the volume ranging from 1 to 7
    def set_volume(self, volume_number):
        if 1 <= volume_number <= 7:
            self.volume_level = volume_number

    # Creating method for switching up the channel
    def channel_switch_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    # Creating method for switching down the channel
    def channel_switch_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    # Creating method for increasing volume
    def volume_level_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    # Creating method for decreasing volume
    def volume_level_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1

# End