import instapi
from pathlib import Path
from . import DS_credenciais
from time import gmtime, strftime
from uuid import uuid4
from typing import Optional, NoReturn, Union, Any

class DS_ErrLog:
    path: Path
    goffiPrefix: str = "GOFFI_LOG"
    logPosFix: str = "GOFFIBOT-BACKEND_LOG"
    globFormatStr: str = f"*.{logPosFix}"
    lastId: Optional[int]    
    what: str     
    def __init__(self, what: str) -> None:
        self.path = Path.cwd() / self.goffiPrefix
        self.what = what
        
    def save(self):
        lastId: int = self.getLastLogId() + 1
        paths: list[Path] = list(self.path.glob(self.globFormatStr))
        newLogName: str = f"LOG{lastId}.{self.logPosFix}"


        for file in paths:
            if file.name == newLogName:
                print(f"[GOFFI-DS_BOT]: FATAL! Erro ao executar script de criação de novos LOGS, LOG: '{newLogName}' já existente.")
                exit(1)            
        
        self.writeLog(newLogName, self.what)
     

    def writeLog(self, newFileLogName: str, logDescription: str) -> None:        
        logFullPath: Path= self.path / newFileLogName
        print(f"[GOFFI-DS_BOT]: Escrevendo novo log em ({logFullPath})")
        with open(logFullPath, "w") as file: 
            timeInformation: str = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            file.write(f"{timeInformation}:\n{logDescription}\n")
        
    def getPathName(self) -> str: 
        return self.path.__str__()    
    
    def readLogIdFromLogFileName(self, logName: str) -> Union[int | NoReturn]:
        numberPositionInLogName: int = logName.find("LOG") + len("LOG")        
        dotPositionInLogName: int = logName.find(".")
        
        logNumberStr: str = logName[numberPositionInLogName: dotPositionInLogName]
        try: 
            return int(logNumberStr)
        
        except ValueError as _:
            print(f"[GOFFI-DS_BOT]: FATAL! Enumeração de logs comprometidas...")
            print(f"[GOFFI-DS_BOT]: Possivel Falha no script, consulte @pedroGoffi")
            print(f"[GOFFI-DS_BOT]: Syntaxe esperada... \"LOG\"<NUMERO>.GOFFIBOT-BACKEND_LOG")
            print(f"[GOFFI-DS_BOT]: Encerrando backend.")            
            quit(1)        
    
    def getLastLogId(self) -> int:                
        files: list[Path] = list(self.path.glob(f"*.{self.logPosFix}"))
        return 0 if len(files) == 0 else max([self.readLogIdFromLogFileName(file.name) for file in files])

class DS_InstaBot:    
    instaClient: instapi.Client
    logged: bool = False
    username: str
    cachedInfo: dict[str, dict[str, dict]] = {}

    def __init__(self, loginData: DS_credenciais.InstaLoginData):        
        print("[GOFFI-DS_BOT]: Iniciando BOT")        
        loginSuccess: bool = self.TryLogin(loginData=loginData)
        self.username = loginData.username
        if not loginSuccess:
            print(f"[GOFFI-DS_BOT]: DS_BOT Não conseguiu entrar na conta, verifique as credenciais.")
            self.shutdown()
            exit(1)

        print(f"[GOFFI-DS_BOT / INFO]: DS_BOT Entrou na conta {loginData.username}")

    def shutdown(self):
        print(f"[GOFFI-DS_BOT]: Obrigado por ultilizar BOT ainda em desenvolvimento, contate pedroGoffi para recomendações.")
        if self.logged:
            
            try: self.instaClient.logout()
            except: pass

    def TryLogin(self, loginData: DS_credenciais.InstaLoginData) -> bool:         
        
        try:             
            self.instaClient = instapi.Client(username=loginData.username, password=loginData.password)
            self.instaClient.login()            
            self.logged = True
        except instapi.errors.ClientLoginError as loginErr:
            print(f"[GOFFI-DS_BOT]: Erro ao entrar na conta")
            print("Verifique o LOG de erro em ")
            DS_ErrLog(loginErr).save()            
            return False                                
        except Exception as unknownErr:
            print(f"[GOFFI-DS_BOT]: Erro Inesperado ao entrar na conta")
            print(f"[GOFFI-DS_BOT]: Perigo de bloqueio de IP")            
            print(f"[GOFFI-DS_BOT]: Verifique o LOG de erro em ")
            DS_ErrLog(unknownErr).save()    
            return False        
        
        return True
    


    def getFollowers(self) -> dict:
        if (cached_followers := self.cachedInfo.get("followers")) is not None:
            return cached_followers.get("followers").get("users")
        

        print(f"[GOFFI-DS_BOT]: Carregando informações de seguidores para [{self.username}]")
        self.cachedInfo["followers"] = {}
        accountFollowersInfo: dict = self.instaClient.user_followers(self.instaClient.authenticated_user_id, self.instaClient.generate_uuid())
        for keyInfo in accountFollowersInfo.keys():            
            info: Any = accountFollowersInfo[keyInfo]
            self.cachedInfo["followers"][keyInfo] = info

            print(f"\t[*] Salvo em cache [{self.username}] [{keyInfo}]")
            
        
        return accountFollowersInfo.get("users")

    
    def getFollowersCount(self): return len(self.getFollowers())