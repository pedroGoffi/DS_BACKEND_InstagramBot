from os import getenv
from dataclasses import dataclass
from .DS_Debug import *
from typing import Optional, List


DS_DOTENV_TEMPLATE: str = "DS_ACCOUNT"


def __getFromKey(key: str) -> Optional[str]: 
    """ Carrega variaveis locais relativas a chave passada """
    return getenv(key=key)

@dataclass
class InstaLoginData:
    username: str
    password: str



def loadInstaLoginFromID(id: int, ignoreErr: bool) -> Optional[InstaLoginData]:
    """ A variavel local deve ser neste formato = DS_ACCOUNT_<INT>=MEUUSUARIO,MINHASENHA """
    dataLogin: Optional[str] = __getFromKey(f"{DS_DOTENV_TEMPLATE}_{id}")            
    if dataLogin is None:
        if not ignoreErr:
            print(f"[GOFFI-DS_CREDENTIALS]: Variaveis locais para login de conta com ID[{id}] não configurada")
        return None
    
    dataLoginList: List[str, str] = dataLogin.split(",")    
    if len(dataLoginList) != 2:
        if not ignoreErr:
            print(f"[GOFFI-DS_CREDENTIALS]: Variaveis locais para login de conta com ID[{id}] mal configurada esperado DS_ACCOUNT_{id}=USUARIO,SENHA")
        return None
    
    username: str = dataLoginList[0]
    password: str = dataLoginList[1]
    if username is None or password is None:
        if not ignoreErr:
            print(f"[GOFFI-DS_CREDENTIALS]: Variaveis locais para login de conta com ID[{id}] não estão configuradas")
        return None        

    return InstaLoginData(username=username, password=password)
    


def loadAllInstaLoginData() -> list[InstaLoginData]:
    id: int = 1
    instaLoginDataList: list[InstaLoginData] = []
    while True:        
        dataLogin: Optional[InstaLoginData] = loadInstaLoginFromID(id=id, ignoreErr=True)                
        if dataLogin is None:
            if envVars.get("DEBUG").value in "NA":
                print(f"[GOFFI-DS_CREDENTIALS]: Carregado com {'ERRO' if len(instaLoginDataList) == 0 else 'SUCESSO'} {len(instaLoginDataList)} credenciais")
            return instaLoginDataList
                
        instaLoginDataList.append(dataLogin)        
        id += 1