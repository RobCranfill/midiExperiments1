#!/bin/python3
# this correcly passes every command from the MPK to the SR18
# note (haha) that we don't have to change the channel.

import mido
import time


outPort = mido.open_output('MidiSport 1x1 MIDI 1')
print("Open OK")

with mido.open_input('MPKmini2 MIDI 1') as inPort:
    for message in inPort:
        print(message)
        # message.channel = 10
        outPort.send(message)
        time.sleep(.1)
        outPort.send(message)
