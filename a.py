#!/bin/python3
# Hello, MIDI!
# works

import mido
import time


port = mido.open_output('MidiSport 1x1 MIDI 1')

for note in range(36, 54):
    msg = mido.Message('note_on', channel=9, note=note)
    print(msg)
    port.send(msg)
    time.sleep(.1)
    msg = mido.Message('note_off', channel=9, note=note)
    print(msg)
    port.send(msg)
    time.sleep(.2)
