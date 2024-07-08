# L -> Pouco
# N -> Necessário
# A -> TUDO 
from os import environ
from typing import Optional
from uuid import uuid4
from dataclasses import dataclass


DEBUG_TUDO: str         = "A"
DEBUG_NECESSARIO: str   = "N"
DEBUG_POUCO: str        = "L"

def __try_get_env__(key: str) -> Optional[str]:
    
    try:        return environ[key]
    except:     return None
def __try_set_env__(key: str, value: str):
    try: 
        environ[key] = value
        return environ[key]
    
    except: return value
    

def __set_random_or_get__(key: str):
    if (val := __try_get_env__(key)) is not None: return val
    
    __try_set_env__(key, uuid4().__str__())
    ret: str = __try_get_env__(key)
    assert ret, f"[GOFFI-DS_ENV]: Erro ao iniciar variavel ambiente, cheque as permições do codigo."
    return ret
    

def genKey(key: str) -> str: return f"GOFFI_ENV_VAR_{key}"
    
@dataclass
class EnvironVar:
    key:    str
    value:  str
    isPub:  bool

    def __init__(self, key: str, value: str, isPub: bool):
        self.key   = key
        self.value = value 
        self.isPub = isPub


class EnvironVars:
    __variables: dict[str, EnvironVar] = {}
    

    def new(self, env: EnvironVar) -> None:        
        if self.get(env.key): 
            print(f"[GOFFI-DS_ENV]: Erro variavel {env.key} já alocada")
            exit(1)

        self.__variables[env.key] = env        
        environ[genKey(env.key)] = env.value

        if      env.key != "KERNEL":
            print(f"[GOFFI-DS_ENV]: Criado nova variavel ambiente: [{env.key}]")

    def get(self, key: str) -> Optional[EnvironVar]:                 
        env: EnvironVar = self.__variables.get(key)        
        if env is None: return None

        if "KERNEL" in self.__variables.keys():
            if key == "KERNEL":
                print(f"[GOFFI-DS_ENV]: Erro, variavel KERNEL é privada ao backend.")
                exit(1)

            kernel: EnvironVar = self.__variables["KERNEL"]            
            if kernel.value != "ADMIN" and not env.isPub:
                print(f"[GOFFI-DS_ENV]: ERRO, variavel ambiental [{env.key}] é privada ao codigo...")
                exit(1)                

        else:
            assert key == "KERNEL", f"[GOFFI-DS_ENV]: Esperado variavel KERNEL ser exportada"

        
        return env
        

    def set(self, key: str, newValue: str):                
        got: EnvironVar = self.get(key)                

        
        oldValue = got.value
        got.value = newValue
        environ[genKey(key)] = newValue

        if self.get("DEBUG").value in "NA":
            print(f"[GOFFI-DS_ENV]: [{key}] {oldValue} => {newValue}")

    def show(self):
        print(self.__variables)
        for envVar in self.__variables:
            print(envVar)



envVars: EnvironVars = EnvironVars()

def __make_env_var__(key: str, value: str, isPub: bool) -> EnvironVar: 
    return EnvironVar(key, value, isPub)






__try_set_env__("GOFFI_DS_ADMIN_KEY", uuid4().__str__())
__try_set_env__("GOFFI_DS_USER_KEY", uuid4().__str__())
def InitializeEnvironmentVariables():    
    envVars.new(EnvironVar("KERNEL", __try_get_env__("GOFFI_DS_USER_KEY"), True))
    envVars.new(EnvironVar("DEBUG", "A", True))
    

