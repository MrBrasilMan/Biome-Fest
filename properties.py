f = open("server.properties", "r")

for line in f.readlines():
    if "motd=" in line:
        motd = line.replace("motd=", "")
    if "show-minecon-badge=" in line:
        minecon_str = line.replace("show-minecon-badge=", "")
        if minecon_str == "true\n":
            showMinecon = True
        else:
            showMinecon = False
    if "game-mode=" in line:
        gamemode = int(line.replace("game-mode=", ""))
    if "spawn-mobs=" in line:
        mobspawn = line.replace("spawn-mobs=", "")
        if mobspawn == "true\n":
            doMobSpawning = True
        else:
            doMobSpawning = False
    if "peaceful-mode=" in line:
        peacefulmode = line.replace("peaceful-mode=", "")
        if peacefulmode == "true\n":
            isPeaceful = True
        else:
            isPeaceful = False
    if "world-name=" in line:
        worldName = line.replace("world-name=", "").replace("\n", "")
    if "max-players=" in line:
        maximumPlayers = line.replace("max-players=", "").replace("\n", "")
f.close()

def saveProperties(finalMOTD, finalGamemode, finalMinecon, finalMobs, finalPeaceful, finalMaxP, finalWorld):
    try:
        serverDotProperties = f"\nmotd={finalMOTD}\nshow-minecon-badge={finalMinecon}\ngame-mode={finalGamemode}\nport=19132\nseed=\nspawn-mobs={finalMobs}\npeaceful-mode={finalPeaceful}\nworld-name={finalWorld}\nmax-players={finalMaxP}\nwhitelist=false"
    except:
        return ZeroDivisionError
    try:
        f = open("server.properties", "w")
        f.write(serverDotProperties)
        f.close()
    except:
        return FileNotFoundError
    
    