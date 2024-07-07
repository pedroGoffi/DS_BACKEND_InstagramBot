from src.DS_InstaBot    import DS_InstaBot
from src.DS_credenciais import loadAllInstaLoginData
from src.DS_Backend     import backendProc
from src.DS_debuglvl    import *

if __name__ in "__main__":          
    backendProc.loadAll(loadAllInstaLoginData())
    