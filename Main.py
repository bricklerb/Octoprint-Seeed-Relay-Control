import argparse

from RelayControl import RelayControl

parser = argparse.ArgumentParser(description='Relay Control Script')
parser.add_argument('-o', '--off', help='Parameter to turn off the relay', action='store_false')
parser.add_argument('-r', '--relay', help='The integer of the relay to change (1-4)', type=int, default=1)

args = parser.parse_args()

setting = args.off
relay = args.relay

#fail quietly if relay number isnt valid
if (relay < 1 or relay > 4):
    exit

if (setting):
    RelayControl.ChangeRelayState(relay, True)
else:
    RelayControl.ChangeRelayState(relay, False)
