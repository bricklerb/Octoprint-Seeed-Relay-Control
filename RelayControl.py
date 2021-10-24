from Lib import relay_lib_seeed

class RelayControl:
    def ChangeRelayState(relay_num, state):
        if (state):
            relay_lib_seeed.relay_on(relay_num)
        else:
            relay_lib_seeed.relay_off(relay_num)