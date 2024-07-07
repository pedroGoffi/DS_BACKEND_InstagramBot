# 0 -> Pouco
# 1 -> Necessário
# 2 -> TUDO 
from os import environ

DEBUG_NADA          = 0
DEBUG_NECESSARIO    = 1
DEBUG_TUDO          = 2

def setDebug(lvl):    
    environ["GOFFI_DS_BOT_DEBUG_LVL"] = str(lvl)

def getDebug() -> int:
    return int(environ["GOFFI_DS_BOT_DEBUG_LVL"])
