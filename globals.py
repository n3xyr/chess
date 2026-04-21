import json

pieceHasMoved = False
showSettings = False
settingsButtonsDrawn = False
showPossibleMovesSwitchState = True
disableSoundsSwitchState = False

def getSettingsOriginalValues():
    settingsOriginalValues = {
    "primaryColor" : "739552",
    "secondaryColor" : "ebecd0",
    "pieceChoice" : "Neo",
    "showPossibleMoves" : True,
    "disableSounds" : False
    }
    return settingsOriginalValues

def readTheme():
    with open("theme.json", "r", encoding="utf-8") as f:
        theme = json.load(f)
    return theme