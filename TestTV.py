# Diong, Shan Marc C.
# BSCPE 1-2

# Import TV
from TV import TV

# Word Format and Text to Speech
import pyttsx3

text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)
green = "\033[0;32m"
blue = "\033[0;34m"


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

    # Output results of TV 1
    output_speech = "TV 1's channel is 30 and volume level is 3"
    print(green + f"\ntv1's channel is {blue}{tv_1.get_channel()}{green} and volume level is {blue}{tv_1.get_volume()}")
    text_to_speech.say(output_speech)
    text_to_speech.runAndWait()

    # Output results of TV 2
    output_speech = "TV 2's channel is 3 and volume level is 2"
    print(green + f"\ntv2's channel is {blue}{tv_2.get_channel()}{green} and volume level is {blue}{tv_2.get_volume()}")
    text_to_speech.say(output_speech)
    text_to_speech.runAndWait()


test_tv()
# End