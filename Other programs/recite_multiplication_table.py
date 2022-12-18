# This is the program that say the table of a number entered by user

import pyttsx3
speaker=pyttsx3.init()
def speak(user):
    speaker.say(user)
    speaker.runAndWait()

speak("Enter, a number to know its multipliacation table: ")
a=int(input("Enter a number to know its multiplication table: "))
for i in range(1,11):
    result=a*i
    speak(str(a)+' '+str(i)+"is"+str(result))
    print(a,' * ',i,' = ',result)



    
