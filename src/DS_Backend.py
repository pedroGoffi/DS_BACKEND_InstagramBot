from src.DS_InstaBot    import DS_InstaBot
from src.DS_credenciais import loadAllInstaLoginData, InstaLoginData
from src.DS_debuglvl    import *
from os                 import environ
class DS_BackendProcess:
    ACTIVE_BOTS: list[DS_InstaBot] = []

    def print(self, *args, **kwargs) -> None:        
        print("[GOFFI-BACKEND]: ", end="")
        print(*args, **kwargs)

    def __init__(self, debug: int = DEBUG_TUDO): 
        self.print(f"INICIANDO PROCESSO BACKEND")
        setDebug(debug)
        
    def loadAll(self, credentials: list[InstaLoginData]) -> bool:        
        self.print("Carregando credenciais presente nas variaveis de ambiente")
        for credential in credentials:            
            bot: DS_InstaBot = DS_InstaBot(credential)
            self.ACTIVE_BOTS.append(bot)

backendProc: DS_BackendProcess = DS_BackendProcess()