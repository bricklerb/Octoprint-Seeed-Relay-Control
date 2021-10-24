from relay_lib_seeed import *

def ChangeRelayState(relay_num, state):
    if (state):
        relay_on(relay_num)
    else:
        relay_off(relay_num)