import keyboard
import speech_recognition as sr
from nltk.tokenize import word_tokenize
import tkinter.filedialog as fd                                                                             ## filedialogue for opening files imported twice
import threading
##########################################################################################################
def fileopo():
    flag = "start"
    def controll():
        global cmvalue
        while flag == "start":
            listenit_thread.start()
            listenit_thread.join()
            command = cmvalue
            tokens = word_tokenize(command)
            print(tokens)
            key=["up", "down", "right", "tab" ,"left","stop","next","back","backwards","select","backwards","previous", "enter","open"]
            new_name = None
            for i in tokens:
                if i in key:
                        ##### Up
                    if i == "up":
                        keyboard.press_and_release('up')
                        ##### Down
                    elif i == "down":
                        keyboard.press_and_release('down')
                        ##### Next
                    elif i == "right" or i == "next":
                        keyboard.press_and_release('right')
                        ##### Prevoius
                    elif i == "left" or i == "previous":
                        keyboard.press_and_release('left')
                        ##### Change tab
                    elif i == "tab":
                        keyboard.press_and_release('tab')
                        ##### Back
                    elif i =="back" or i == "backward" or i == "backwards":
                        keyboard.press_and_release('backspace')
                        ##### Select file
                    elif i =="open" or i == "enter" or i == "select":
                        keyboard.press_and_release('enter')
                        ##### Give name directly
                    else:
                        new_name = command
                        print ("command = "+new_name)
            if new_name is not None:
                keyboard.write(new_name)
                print("write"+command)
                keyboard.press_and_release('enter')

    controll_thread = threading.Thread(target=controll)
    controll_thread.start()
    name = fd.askopenfilename(filetypes=[('Image Files', ['.jpeg','.jpg','.png','.gif','.tiff','.tif','.bmp'])],title='Please select a picture to Elementize')     ## shows only these extentions
    if name is not None: 
        flag = "stop"
    print("fileopo "+name) 
    listenit_thread.join()
    controll_thread.join()

def listenit():
    global cmvalue
    r = sr.Recognizer()  
    with sr.Microphone() as source: 
        print("Please wait. Calibrating microphone...")  
        r.adjust_for_ambient_noise(source, duration=5)      
        print("Say something!")  
        audio = r.listen(source)  
    # recognize speech using google  
    try:  
        cmvalue = r.recognize_google(audio)
        print("elements thinks you said '" + cmvalue)  
    except sr.UnknownValueError:  
        print("elements could not understand audio")  
    except sr.RequestError as e:  
        print("elements error; {0}".format(e)) 

listenit_thread = threading.Thread(target=listenit)

if __name__ == "__main__":  
    t1 = threading.Thread(target=fileopo) 
    t1.start()
    t1.join()
############################################################################
###########3 if therer is  no file  ?
#### to backward current directory