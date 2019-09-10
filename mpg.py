"""
Author:      Greg Prawdzik
Date:        07MAY2018
Assignment:  Chapter 15 Programming Exercise 3(Miles-per-Gallon Calcuator)
Filename:    MPG.py
Description:
        This program creates a GUI interface to enter number of gallons in a car
        as well as number of miles able to be driven.  When the calculate button
        is clicked, it will display the MPG.
"""
import tkinter

class MPG_GUI:
    def __init__(self):

        # Create window and set title
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title('MPG')

        # Create frames to group widgets
        self.gallonsFrame = tkinter.Frame(self.mainWindow)
        self.milesFrame = tkinter.Frame(self.mainWindow)
        self.milesPerGallonFrame = tkinter.Frame(self.mainWindow)
        self.buttonsFrame = tkinter.Frame(self.mainWindow)

        # Create labels and text boxes and pack them
        # Gallons Input
        self.gallonsLabel = tkinter.Label(self.gallonsFrame, \
                                          text = 'Gas capacity in gallons:')
        self.gallonsTextBox = tkinter.Entry(self.gallonsFrame, width = 10)
        self.gallonsLabel.pack(side = 'left')
        self.gallonsTextBox.pack(side = 'left')

        # Miles Input
        self.milesLabel = tkinter.Label(self.milesFrame, \
                                          text = 'Miles driven on a full tank:')
        self.milesTextBox = tkinter.Entry(self.milesFrame, width = 10)
        self.milesLabel.pack(side = 'left')
        self.milesTextBox.pack(side = 'left')

        # Create labels and pack for milesPerGallon frame
        self.resultLabel = tkinter.Label(self.milesPerGallonFrame, \
                                         text = 'MPG')

        # Create StringVar to hold display string that
        # updates upon calculatin of MPG
        self.milesPerGallonString = tkinter.StringVar()

        # Create the milesPerGallon label and bind to StringVar
        self.milesPerGallonLabel = tkinter.Label(self.milesPerGallonFrame, \
                                                 textvariable = self.milesPerGallonString)
        self.resultLabel.pack(side='left')
        self.milesPerGallonLabel.pack(side='left')

        # Create button and pack frame
        self.calcButton = tkinter.Button(self.buttonsFrame, \
                                         text = 'Calculate MPG', \
                                             # callback function to calculate MPG
                                         command = self.calcButton_Click)
        self.calcButton.pack(side = 'left')

        # Pack the frames into the window
        self.gallonsFrame.pack()
        self.milesFrame.pack() 
        self.milesPerGallonFrame.pack() 
        self.buttonsFrame.pack()

        # Enter the main loop
        tkinter.mainloop()

    # the calcButton_Click is an event handler for
    # the "Calculate MPG" button.
    def calcButton_Click(self):
        # Get Miles and Gallons
        miles = float(self.milesTextBox.get())
        gallons = float(self.gallonsTextBox.get())
        # Calculat MPG
        milesPerGallon = (miles / gallons)
        # Update teh StringVardisplay
        self.milesPerGallonString.set(format(milesPerGallon, '.2f'))
        

def main():
    milesPerGallon = MPG_GUI()

# Call main
main()
    

                                                 



