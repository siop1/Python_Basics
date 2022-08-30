# Install an external module and use it to do the operation of your interest


# I have installed an external module using pip as:  pip install pyttsx3

# importing the pyttsx library
import pyttsx3
  
# initialisation
engine = pyttsx3.init()
  
# testing
engine.say("I solved this question")
engine.runAndWait()
