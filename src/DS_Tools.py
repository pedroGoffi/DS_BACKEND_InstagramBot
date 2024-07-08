from typing import Tuple

def StrToInt(val: str) -> Tuple[int, bool]:
    try:        return int(val), False
    except:     return 0, True