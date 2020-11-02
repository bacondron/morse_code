#Barbara Condron
#morse_code.py
#A program that turns input string and encodes it
#Displays string message in morse code
#I certify that this is my own original code

from graphics import *

def main():
    #window
    win = GraphWin("Encoder", 300, 300)
    #background
    win.setBackground("black")
    #instructions
    instructions = Text(Point(50, 25), "Enter message: ")
    instructions.setFill("white")
    instructions.draw(win)
    #entry box for message
    inputBox = Entry(Point(150, 25), 10)
    inputBox.draw(win)
    #encode button
    button = Rectangle(Point(100,100), Point(175,125))
    button_pt = button.getCenter()
    button_txt = Text(button_pt, "Encode")
    button.setFill("white")
    button.draw(win)
    button_txt.draw(win)
    #wait to click encode
    win.getMouse()
    #undraw button
    button.undraw()
    button_txt.undraw()
    #morse code lists
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',   \
  '....', '..', '.---', '-.-','.-..', '--', '-.','---', '.--.', '--.-', '.-.', '...', \
   '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    #encode message
    message = inputBox.getText()       #gets message
    message = message.upper()          #changes message to uppercase
    message = message.split(" ")       #splits words of sentence
    encoded_msg = []
    i = 0
    for i in range(len(message)):
        msg = message[i]                    #singles out words
        for x in range(len(msg)):             #encodes each word
            letter = msg[x]
            index = alphabet.find(letter)
            digit = morse_code[index]
            encoded_msg.append(digit)
    your_code = Text(Point(150,140), "Your code is:")
    code = Text(Point(150,150), encoded_msg[0:])
    code.setSize(15)
    your_code.setFill("white")
    code.setFill("white")
    your_code.draw(win)
    code.draw(win)
    # close
    close = Text(Point(150, 50), "Click anywhere to close")
    close.setFill("white")
    close.draw(win)
    win.getMouse()
    win.close()

main()