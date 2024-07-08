from src.DS_InstaBot    import DS_InstaBot
from src.DS_credenciais import loadAllInstaLoginData
from src.DS_Backend     import backendProcess
from src.DS_Debug       import *

if __name__ in "__main__":     
    backendProcess.loadInstaAccount(
        manual_mode=True,
        username="p__goffi",
        password="Pedrohg31#",
        persistence=True)
    
    

    x = backendProcess.getInstagramFollowersCountByName("p__goffi")
    print(f"p__goffi tem {x} seguidores")