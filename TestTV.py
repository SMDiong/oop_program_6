# Diong, Shan Marc C.
# BSCPE 1-2

# Word Format and Text to Speech
import pyttsx3

text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)
green = "\033[0;32m"
blue = "\033[0;34m"

# Import TV
from TV import TV


# Create the test driver program that will create two objects from Class TV
def test_tv():
    # Creating the first TV object
    tv_1 = TV()
    # Turn on TV 1
    tv_1.turn_on()
    # Set volume of TV 1 to 3
    tv_1.set_volume(3)
    # Set channel of TV 1 to 30
    tv_1.set_channel(30)

    # Creating the second TV object
    tv_2 = TV()
    # Turn on TV 2
    tv_2.turn_on()
    # Set volume of TV 2 to 3
    tv_2.set_volume(2)
    # Set channel of TV 2 to 30
    tv_2.set_channel(3)

    # Output results of both TV objects


test_tv()
