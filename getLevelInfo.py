import gd, os, pathlib

client = gd.Client()

level_id = input('LevelID > ')

# Checkers

def checkSCORE(level: gd.Level):
    if level.score != 0:
        return level.score
    else:
        return "None"

def checkDESC(level: gd.Level):
    if level.description != '':
        return level.description
    else:
        return "None"

def checkPASS(level: gd.Level):
    if level.password != None:
        return level.password
    else:
        return "None"

def levelratedata(level: gd.Level):
    returndata = ''
    if level.is_rated() == True:
        returndata += f"Rated: True\nStars: {level.stars}\nCoins: {level.coins}"
        if level.is_featured() == True:
            returndata += f"\nFeatured: True\nScore (featured score): {checkSCORE(level)}"
        else:
            returndata += "\nFeatured: False"
        if level.is_epic() == True:
            returndata += f"\nEpic: TrueScore (featured score): {checkSCORE(level)}"
        else:
            returndata += "\nEpic: False"
        if level.is_demon() == True:
            returndata += "\nDemon: True"
        else:
            returndata += "\nDemon: False"
        if level.is_auto() == True:
            returndata += "\nAuto: True"
        else:
            returndata += "\nAuto: False"
    else:
        returndata += "Rated: False"
    return returndata

def is_orig(level: gd.Level):
    if level.is_original() == True:
        return 'Original: True'
    else:
        if level.original_id == level.id:
            return 'Original: True'
        else:
            return f'Original: False\nOriginal level: {level.original_id}'

def checkReqStars(level: gd.Level):
    if level.requested_stars != 0:
        return level.requested_stars
    else:
        return 'None'

class Main:
    async def Program():
        global lvlid
        try:
            level = await client.get_level(int(level_id))
            lvlid = level.id 
        except gd.MissingAccess:
            print('Wrong levelID!')
            os.system('pause')
            exit()
        except gd.HTTPError:
            print('Server error!')
            os.system('pause')
            exit()
        try:
            path = pathlib.Path().resolve()
            os.makedirs(str(path)+'/levels/txt')
        except:
            pass
        LEVEL_STRING = f"""Level ID: {level.id}
Name: {level.name}
Description: {checkDESC(level)}
Creator: {level.creator}
Version: {level.version}
Game version: {level.game_version}
Downloads: {level.downloads}
Likes / Dislikes: {level.rating}
Song: {level.song}
Difficulty: {str(level.difficulty).split('.')[1]}
{levelratedata(level)}
Password: {checkPASS(level)}
{is_orig(level)}
Length of level: {str(level.length).split('.')[1]}
Requested stars: {checkReqStars(level)}
Objects in level: {level.objects}
Data / string: {level.data}"""
        f=open(f'levels\\{lvlid}.LEVEL', 'w')
        f.write(LEVEL_STRING)
        f.close()
        f=open(f'levels\\txt\\{lvlid}.txt', 'w')
        f.write(LEVEL_STRING)
        f.close()

client.run(Main.Program())
print(f'Level info files created! | .LEVEL file: levels/{lvlid}.LEVEL | .txt file: levels/txt/{lvlid}.txt')
os.system('pause')