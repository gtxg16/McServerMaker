import sys
import time
import urllib

import wget
import os
import configparser

parser = configparser.RawConfigParser()
if str(os.path.isdir(os.getcwd() + "/mc_server")) in "True":
    os.chdir("mc_server")
    if str(os.path.isfile("mcservermaker_settings.ini")) in "True":
        while True:
            configFilePath = r'mcservermaker_settings.ini'
            parser.read("mcservermaker_settings.ini")
            configVersion = parser.get('server', 'version')
            configType = parser.get('server', 'type')
            launchExistingServer = str(
                input("It seems that you already have a " + configType + " " + configVersion + "server! Do you want "
                                                                                               "to start it? (y/n) "
                                                                                               "")).lower()
            if launchExistingServer in "y":
                print("Ok, we will now start with the RAM amount in the config!")
                time.sleep(1)
                sameRamOrNot = str(input("Or do you want to start with the same RAM as before? (y/n): ")).lower()
                if sameRamOrNot in "y":
                    print("Ok, starting server.")
                    parser.read("mcservermaker_settings.ini")
                    configRam = parser.get('server', 'ram')
                    os.system("java -Xms" + str(configRam) + "M -Xmx" + str(
                        configRam) + "M -jar server.jar nogui")
                    quit()
                elif sameRamOrNot in "n":
                    while True:
                        try:
                            changeRamTo = int(input("What do you want to change the ram to then?: "))
                        except ValueError:
                            print("RAM must be a number!")
                        else:
                            os.remove("mcservermaker_settings.ini")
                            settingsini = open("mcservermaker_settings.ini", "a")
                            settingsini.write(
                                "# Ignore this file. It is used so that McServerMaker can start the server with "
                                "correct RAM.")
                            settingsini.write("\n")
                            settingsini.write("\n")
                            settingsini.write("[ram]")
                            settingsini.write("\n")
                            settingsini.write("ram = " + str(changeRamTo))
                            settingsini.close()
                            os.system("java -Xms" + str(changeRamTo) + "M -Xmx" + str(changeRamTo) + "M -jar "
                                                                                                     "server.jar "
                                                                                                     "nogui")
            elif launchExistingServer in "n":
                print("Ok, bye.")
                sys.exit()

while True:
    print("By running this program you agree to this EULA: https://account.mojang.com/documents/minecraft_eula.")
    time.sleep(1)
    ifPersonAgrees = str(input("Do you agree? (y/n): ")).lower()
    if ifPersonAgrees in "y":
        print("Great!")
        time.sleep(1)
        break
    elif ifPersonAgrees in "n":
        print("This means that you cannot run this program sadly, as this is required.")
        time.sleep(1)
        print("Goodbye.")
        sys.exit()
print("Welcome to the automatic Minecraft Server Maker!")
time.sleep(1)
print("We just need a few things and then we can get going! (psst, when the server is made, dont change the folder "
      "name unless you want to launch the server again)")
time.sleep(1)
print("Enter which server type you want!")
time.sleep(1)
print('These are the options: "vanilla", "snapshot" "bukkit", "spigot", "paper", "bungeecord", "travertine", '
      '"velocity", '
      '"waterfall", "purpur", "tuinity", "yatopia"')
time.sleep(1)
while True:
    try:
        serverTypeChosen = str(input("Server type you want: ")).lower()
    except ValueError:
        print("The server type cannot be a number!")
    else:
        break

serverTypes = ["vanilla", "snapshot", "bukkit", "spigot", "paper", "bungeecord", "travertine", "velocity", "waterfall", "purpur",
               "tuinity", "yatopia"]

if any(x in serverTypeChosen for x in serverTypes):
    print("You have chosen " + serverTypeChosen + ".")
    os.mkdir(os.getcwd() + "/mc_server")
    os.chdir("mc_server")
    while True:
        try:
            version = input("Enter MC version: ")
            print("Downloading...")
            wget.download("https://serverjars.com/api/fetchJar/" + serverTypeChosen + "/" + version, "server.jar", bar=wget.bar_thermometer)
            break
        except urllib.error.HTTPError:
            print("File not found!")
    eula = open("eula.txt", "a")
    eula.write("# This server was auto generated by McServerMaker.")
    eula.write("\n")
    eula.write("eula=true")
    eula.close()
    while True:
        try:
            print("\n")
            ramAmount = int(input("Enter RAM Amount (in MB, for example if i wanted 4gb i would say 4096): "))
        except ValueError:
            print("RAM Amount needs to be an integer!")
        else:
            settingsini = open("mcservermaker_settings.ini", "a")
            settingsini.write("# Ignore this file. It is used so that McServerMaker can start the server with correct "
                              "RAM.")
            settingsini.write("\n")
            settingsini.write("\n")
            settingsini.write("[ram]")
            settingsini.write("\n")
            settingsini.write("ram = " + str(ramAmount))
            settingsini.close()
            while True:
                try:
                    ifStartServer = str(input("Do you want to start the server? (y/n) ")).lower()
                except ValueError:
                    print("Enter y/n.")
                if ifStartServer in "n":
                    print("Ok then, goodbye.")
                    sys.exit()
                elif ifStartServer in "y":
                    print("Ok, starting server.")
                    os.system("java -Xms" + str(ramAmount) + "M -Xmx" + str(ramAmount) + "M -jar server.jar nogui")
                    sys.exit()
                else:
                    print("You need to enter y or n!")
