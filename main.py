##########################
# SykeSecure Main Script # (C)2018
########################## Benjamin Sykes

# <<< SET VARIABLES >>>

print("Setting variables . . . ", end='')
QuitNow = False
print("Done.")

# <<< IMPORT LIBRARIES >>>

print("Importing libraries . . . ", end='')
import easygui as eg
from time import sleep
print("Done.")

# <<< MAIN LOOP >>>

print("Starting main loop . . . ")
while not QuitNow:

    # <<< MAIN MENU >>>

    Current = "Main"
    print("Waiting for main menu choice . . . ", end='')
    MainMenu = eg.indexbox("Please select an action.", "SykeSecure - Main Menu", ["Quit", "Encrypt", "Decrypt"])
    if MainMenu == 0:
        print("Quit.")
        QuitNow = True
        Current = "Quit"
    elif MainMenu == 1:
        print("Encrypt.")
        Current = "Encrypt"
    elif MainMenu == 2:
        print("Decrypt.")
        Current = "Decrypt"

    sleep(0.25)

    if Current == "Encrypt" or Current == "Decrypt":
        Continue = True
        print("Getting input file . . . ", end='')
        InputFile = eg.fileopenbox("Select an input file.", "SykeSecure - Input File")
        if InputFile == None:
            Continue = False
            Current = "Main"
            print("None selected, going back to main menu.")
        else:
            print(str(InputFile))
        sleep(0.25)
        if Continue:
            print("Getting output file . . . ", end='')
            OutputFile = eg.filesavebox("Select an output file.", "SykeSecure - Output File")
            if OutputFile == None:
                Continue = False
                Current = "Main"
                print("None selected, going back to main menu.")
            else:
                print(str(OutputFile))

    sleep(0.25)

    if Current = "E"

print("Goodbye!")
quit()