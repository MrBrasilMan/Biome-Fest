from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
from time import sleep
from tkinter import messagebox
import subprocess
import pexpect
import time

version = 1.0

import properties
from os import system, listdir, getcwd

window = Tk()
window.title("Biome Fest v" + str(version))
window.geometry("500x450")
window.resizable(False, False)
global randomInteger


#TODO
#Sync settings with server DONE
# Create seperate server control window when ran DONE
# Have settings change based on server.properties (using properties.py to get results DONE
# Create proper list of players DONE
#Allow for menu selection to kick/ban players DONE
#


    
def saveInput():
    finalMOTD = motdInput.get(1.0, "end-1c").replace("\n", "")
    #Spaced one for visual symertry, remember to replace for true? with MINECON and MOB SPAWNING and PEACEFUL
    if optionMinecon.get() == "True ":
        finalMinecon = "true"
    else:
        finalMinecon = "false"
    if optionMinecon.get() == "Creative":
        finalGamemode = "1"
    else:
        finalGamemode = "0"
    if optionMobSpawning.get() == "True ":
        finalMobs = "true"
    else:
        finalMobs = "false"
    if optionPeaceful.get() == "True ":
        finalPeaceful = "true"
    else:
        finalPeaceful = "false"
    finalMaxP = optionMaxPlayers.get()
    finalWorld = worldInput.get()
    try:
        properties.saveProperties(finalMOTD, finalGamemode, finalMinecon, finalMobs, finalPeaceful, finalMaxP, finalWorld)
    except ZeroDivisionError:
        messagebox.showerror("Error Saving Settings", "Could not save all values")
    except FileNotFoundError:
        messagebox.showerror("Error Saving Settings", "Can't edit server.properties")
def importWorld():
    selectedImport = fd.askdirectory(title="Select a world directory", initialdir="/home/pi/.minecraft-pi/games/com.mojang/minecraftWorlds")
    system("cp -r " + selectedImport + " " + getcwd() + "/games/com.mojang/minecraftWorlds")

def runServer():
    #Spawn processes and messages
    serverOutput.configure(state='normal')
    global commandObject
    commandObject = pexpect.spawn('minecraft-pi-server')
    serverOutput.insert(END, "\n(Server) Sent initiate signal")
    serverOutput.configure(state='disabled')
    stopServer.configure(state='normal')
    runServer.configure(state='normal')
    runServer.configure(state='disabled')
    motdInput.configure(state='disabled')
    dropdownMinecon.configure(state='disabled')
    dropdownMobSpawning.configure(state='disabled')
    dropdownPeaceful.configure(state='disabled')
    dropdownMaxPlayers.configure(state='disabled')
    dropdownGamemode.configure(state='disabled')
    importWorldButton.configure(state='disabled')
    saveChanges.configure(state='disabled')
    worldInput.configure(state='disabled')
    killPlayerButton.configure(state='normal')
    banPlayerButton.configure(state='normal')
    reloadPlayerCount.configure(state='normal')    

def stopServer():
    #Send stop signal
    commandObject.sendline("stop")
    serverOutput.configure(state='normal')
    serverOutput.insert(END, "\n(Server) Sent stop signal")
    serverOutput.configure(state='disabled')
    stopServer.configure(state='disabled')
    runServer.configure(state='normal')
    motdInput.configure(state='normal')
    dropdownMinecon.configure(state='normal')
    dropdownMobSpawning.configure(state='normal')
    dropdownPeaceful.configure(state='normal')
    dropdownMaxPlayers.configure(state='normal')
    dropdownGamemode.configure(state='normal')
    importWorldButton.configure(state='normal')
    saveChanges.configure(state='normal')
    worldInput.configure(state='normal')
    killPlayerButton.configure(state='disabled')
    banPlayerButton.configure(state='disabled')
    reloadPlayerCount.configure(state='disabled')
    #Toggle buttons
#This funcion is bad and Biome Fest will hopefulyl get a much better back end from Mycellium when I implement this
def updatePlayerCount():
        stringLine = ""
        while True:
            stringLine = commandObject.readline()
            randomInteger = "a"
            commandObject.sendline("start-" + randomInteger)
            commandObject.sendline("list")
            commandObject.sendline("end-" + randomInteger)
            while True:
                    stringLine = commandObject.readline()
                    if stringLine == b'[INFO]: All Players:\r\n':
                        counter = 1
                        pListbox.delete(0, END)
                        pListbox.insert(1, "Players Online:")
                        while True:
                            stringLine = commandObject.readline()
                            if stringLine == b'[INFO]: Invalid Command: end-a\r\n':
                                if counter == 1:
                                    pListbox.insert(2, "No Players Online")
                                break
                            else:
                                #odd bug, sometimes end does not display on readline, so i have to make this exception
                                if stringLine != b'end-a\r\n':
                                    counter += 1
                                    pListbox.insert(counter, stringLine.decode("ascii").replace("[INFO]:  - ", "").replace("\r\n", "").replace(" (192.168.1.201)", ""))
                        break
            break
def killPlayer():
    if pListbox.get(ACTIVE) != "Players Online:" or pListbox.get(ACTIVE) != "No Players Online":
            commandObject.sendline("kill " + pListbox.get(ACTIVE))
            serverOutput.insert(END, "\n(Server) Killed " + pListbox.get(ACTIVE))
def banPlayer():
    #Ask if player should be banned
    shouldBanPlayer = messagebox.askquestion("Ban " + pListbox.get(ACTIVE), "Are you sure you want to ban " + pListbox.get(ACTIVE) + "? This can be reverted by editing the blacklist")
    if shouldBanPlayer == "yes":
        if pListbox.get(ACTIVE) != "Players Online:" or pListbox.get(ACTIVE) != "No Players Online":
                commandObject.sendline("ban " + pListbox.get(ACTIVE))
                serverOutput.insert(END, "\n(Server) Banned " + pListbox.get(ACTIVE))
    
# Label
topLabelString = StringVar()
topLabel = Label( window, textvariable=topLabelString)
topLabelString.set("  Message of the Day       Show Minecon Badge          Gamemode")
topLabel.place(x=0, y=20)

#Middle Label
middleLabelString = StringVar()
middleLabel = Label( window, textvariable=middleLabelString)
middleLabelString.set("  Do Mob Spawning              Peaceful Mode               Max Players")
middleLabel.place(x=0, y=80)
#Bottom Label
bottomLabelString = StringVar()
bottomLabel = Label( window, textvariable=bottomLabelString)
bottomLabelString.set("   World Name                           World List                   Import World")
bottomLabel.place(x=0, y=150)

#MOTD label
motdInput = Text(window,
                   width = 17,
                     height=2)
motdInput.place(x=15, y=40)
motdInput.insert(END, properties.motd)


#Show Minecon Badge Dropdown
optionMinecon = StringVar(window)
mineconChoices = {'True ', "False"}
optionMinecon.set("False")
if properties.showMinecon == True:
    optionMinecon.set("True ")
dropdownMinecon = OptionMenu(window, optionMinecon, *mineconChoices)
dropdownMinecon.place(x=200, y=45)

#Show Gamemode Dropdown
optionGamemode = StringVar(window)
gamemodeChoices = {'Survival', "Creative"}
optionGamemode.set("Survival")
if properties.gamemode == "1":
    optionGamemode.set("Creative")
dropdownGamemode = OptionMenu(window, optionGamemode, *gamemodeChoices)
dropdownGamemode.place(x=340, y=45)

#Show Mob Spawning Dropdown
optionMobSpawning = StringVar(window)
mobSpawningChoices = {'True ', "False"}
optionMobSpawning.set("True")
if properties.doMobSpawning == False:
    optionMobSpawning.set("False")
dropdownMobSpawning = OptionMenu(window, optionMobSpawning, *mobSpawningChoices)
dropdownMobSpawning.place(x=30, y=100)

#Show Peaceful Mode Dropdown
optionPeaceful = StringVar(window)
peacefulChoices = {'True ', "False"}
optionPeaceful.set("False")
if properties.isPeaceful == True:
    optionPeaceful.set("True ")
dropdownPeaceful = OptionMenu(window, optionPeaceful, *peacefulChoices)
dropdownPeaceful.place(x=200, y=100)

#Show Maximum Players Dropdown
optionMaxPlayers = StringVar(window)
#maxPlayersChoices = {'1', "2", "3", "4", "5", "6", "7", "8", "9", "10", "15", "20"}
optionMaxPlayers.set(properties.maximumPlayers)
dropdownMaxPlayers = OptionMenu(window, optionMaxPlayers, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "15", "20")
dropdownMaxPlayers.place(x=350, y=100)

#World Name Label
worldInput = Entry(window, width=10)
worldInput.insert(END, properties.worldName)
worldInput.place(x=10, y=170)

#World List
worldList = ScrolledText(window,
                   height = 3,
                   width = 10,
                         )
worldString = ""
for file in listdir("games/com.mojang/minecraftWorlds"):
    worldString = worldString + file + ")\n"
worldList.place(x=190, y=170)
worldList.insert(END, worldString)
worldList.configure(state='disabled')

#Import World Button
importWorldButton = Button(window,
                     text="Import",
                     command=importWorld,
                     width = 3,
                     height = 1,
                     )
importWorldButton.place(x=360, y=170)


#Save Changes Button
saveChanges = Button(window,
                     text="Save",
                     command=saveInput,
                     width = 2,
                     height = 1,
                     )
saveChanges.place(x=0, y=420)

#Run Changes Button
runServer = Button(window,
                     text="Run",
                     command=runServer,
                     width = 2,
                     height = 1,
                     )
runServer.place(x=400, y=420)

#Stop server
stopServer = Button(window,
                     text="Stop",
                     command=stopServer,
                     width = 2,
                     height = 1,
                     )
stopServer.place(x=450, y=420)
#Initally disable button
stopServer.configure(state='disabled')

#Server Information
serverOutput = ScrolledText(window,
                   height = 6,
                   width = 30,
                         )
                         
serverOutput.place(x=0, y=280)
serverOutput.insert(END, "Ready. You are running Biome Fest v" + str(version))
serverOutput.configure(state='disabled')

#Player listbox
pListbox = Listbox(window, width=25, height=6, selectmode=SINGLE)
pListbox.place(x=260, y=280)
pListbox.insert(1, "Players Online:")

#Reload Player Count
reloadPlayerCount = Button(window,
                     text="Reload",
                     command=updatePlayerCount,
                     width = 4,
                     height = 1,
                     )
reloadPlayerCount.place(x=260, y=245)
reloadPlayerCount.configure(state='disabled')

#Player Options Menu
#Kill Player
killPlayerButton = Button(window,
                     text="Kill",
                     command=killPlayer,
                     width = 4,
                     height = 1,
                     )
killPlayerButton.place(x=340, y=245)
killPlayerButton.configure(state='disabled')

#Ban Player
banPlayerButton = Button(window,
                     text="Ban",
                     command=banPlayer,
                     width = 4,
                     height = 1,
                     )
banPlayerButton.place(x=420, y=245)
banPlayerButton.configure(state='disabled')


window.mainloop()