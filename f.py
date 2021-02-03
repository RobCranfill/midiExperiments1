#!/bin/python3
# this sends notes and PCs,
#  succesfully getting difference voices out of the SR18

import mido
import time

outPort = mido.open_output('MidiSport 1x1 MIDI 1')
print("Open OK")

FUCKING_MIDI_CHANNEL = 9 # WHICH IS, OF COURSE, ACTUALLY 10 ! :-(

# program_change channel=9 program=3 time=0

def sendSomeShit(port, program):
    msg = mido.Message('program_change', channel=FUCKING_MIDI_CHANNEL, program=program)
    port.send(msg)
    print(msg)
    for note in range(36, 40):
        msg = mido.Message('note_on', channel=FUCKING_MIDI_CHANNEL, note=note)
        print(msg)
        port.send(msg)
        time.sleep(.05)
        msg = mido.Message('note_off', channel=FUCKING_MIDI_CHANNEL, note=note)
        print(msg)
        port.send(msg)
        time.sleep(.1)

for prog in range(0, 102):
    print(f"\n**** program {prog}")
    sendSomeShit(outPort, prog)
