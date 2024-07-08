from src.DS_InstaBot    import DS_InstaBot
from src.DS_credenciais import loadAllInstaLoginData, InstaLoginData
from src.DS_Debug       import *
from typing             import Callable, TypeVar, Any
from time               import sleep

GOFFI_ARGUMENT = TypeVar("GOFFI_ARGUMENT", dict[str, Any], None)

class DS_BackendProcess:
    ACTIVE_INSTAGRAM_BOTS: list[DS_InstaBot] = []

    def print(self, *args, **kwargs) -> None: print("[GOFFI-BACKEND]:", *args, **kwargs)
        

    def __init__(self, debug: str = DEBUG_TUDO): 
        self.print(f"INICIANDO PROCESSO BACKEND")
        InitializeEnvironmentVariables()

    def shutDownProcess(self) -> None:
        for bot in self.ACTIVE_INSTAGRAM_BOTS: bot.shutdown()

    def loadKwarg(self, kwargs: dict) -> dict: 
        return kwargs.get("kwargs")

    def SafetyMeasure(self, procedureToCall: Callable, **kwargs) -> None:
        try:             
            procedureToCall(kwargs=kwargs)
        except Exception as err:            
            print(f"[GOFFI-DS_BACKEND]: Medidas de seguranças alcançadas, falha na execução da função {procedureToCall.__name__}, desligando processo backend...")
            self.shutDownProcess()


            print(err)
            exit(1)

    def __LOAD_ALL_INSTA_ACCOUNTS__(self, **kwargs: dict[str, InstaLoginData]) -> bool:        
        self.print("Carregando credenciais presente nas variaveis de ambiente")
        args: dict = self.loadKwarg(kwargs)
        

        if credentials := args.get("credenciais"):            
            for credential in credentials:            
                bot: DS_InstaBot = DS_InstaBot(credential)
                self.ACTIVE_BOTS.append(bot)
    

    def loadInstaAccount(self, **kwargs):        
        if creds := kwargs.get("credenciais"):
            self.SafetyMeasure(self.__LOAD_ALL_INSTA_ACCOUNTS__, credenciais=creds)


        if kwargs.get("manual_mode"):
            username: Optional[str] = kwargs.get("username")
            password: Optional[str] = kwargs.get("password")

            if username is None or password is None:
                self.print("Erro, para manual_mode. Solicito a chave 'username' e 'pwd' estarem setadas.")
                exit(1)

            self.print("AVISO! manual_mode é uma pratica de testes, não coloque o codigo em produção com as credenciais expostas")

            if not isinstance(username, str):
                self.print("ERRO, loadAll espera username ser uma string")
                exit(1)

            if not isinstance(password, str):
                self.print("ERRO, loadAll espera password ser uma string")
                exit(1)

            bot: Optional[DS_InstaBot] = None
            if kwargs.get("persistence"):                
                sleepMins: int = 1
                self.print("FLAG Persistence ativa")
                
                while bot is None:
                    
                    try:
                        bot = DS_InstaBot(InstaLoginData(username=username, password=password))                    
                    except:                        
                        self.print(f"Esperando por {sleepMins} minutos antes de tentar entrar novamente...")
                        sleep(sleepMins * 60)
                        sleepMins += 1
            else:
                bot = DS_InstaBot(InstaLoginData(username=username, password=password))
            
            
            self.ACTIVE_INSTAGRAM_BOTS.append(bot)

    def __del__(self) -> None:
        self.print("Desligando processo backend")
        self.shutDownProcess()        
            

    def getInstagramBotFromName(self, username: str) -> Optional[DS_InstaBot]:
        for bot in self.ACTIVE_INSTAGRAM_BOTS:
            if bot.username == username:
                return bot
            
        return None

    def getInstagramFollowersByName(self, username: str):
        bot: DS_InstaBot = self.getInstagramBotFromName(username)
        if not bot: return {}
        return bot.getFollowers()
    
    def getInstagramFollowersCountByName(self, username: str) -> int:
        bot: DS_InstaBot = self.getInstagramBotFromName(username)
        if not bot: return -1

        return bot.getFollowersCount()

        


backendProcess: DS_BackendProcess = DS_BackendProcess()