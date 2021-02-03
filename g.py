#!/bin/python3
# can we pass notes from the MPK, while injecting PCs?
# works!

import mido
import time

outPort = mido.open_output('MidiSport 1x1 MIDI 1')
print("Open OK")

FUCKING_MIDI_CHANNEL = 9 # WHICH IS, OF COURSE, ACTUALLY 10 ! :-(
MAX_DRUMKIT = 102 # +/- 1 ???


# program_change channel=9 program=3 time=0

def changeProgram(port, program):
    msg = mido.Message('program_change', channel=FUCKING_MIDI_CHANNEL, program=program)
    port.send(msg)
    print(msg)

noteCount = 0
newProgram = 0

with mido.open_input('MPKmini2 MIDI 1') as inPort:
    for message in inPort:
        noteCount += 1
        print(message)
        outPort.send(message)

        if noteCount % 4 == 0:
            print("Changing voice!")
            changeProgram(outPort, newProgram)
            newProgram += 1
            newProgram = newProgram % MAX_DRUMKIT # only 100 values OK?

        # to be sure it's THIS PROGRAM doing this, send duplicate note?
        echo = True
        if echo:
            time.sleep(.1)
            outPort.send(message)
