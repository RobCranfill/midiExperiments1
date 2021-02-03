#!/bin/python3
# name that kit!

import mido
import time

outPort = mido.open_output('MidiSport 1x1 MIDI 1')
print("Open OK")

FUCKING_MIDI_CHANNEL = 10 - 1 # Everyone calls it channel 10, yet we need to use the value 9 ! :-(

# this is the list of SR18 kits, in order, so we can get the Program Change for each.
kits = (
    "Ambient", "Blues01", "Blues02", "Blues03", "Blues04", "Bossa", "Brushes", "Country1", "Country2", "Country3",
    "Dance02", "Dance03", "DarkKit1", "DarkKit2", "Disco02", "ElecTR08", "ElecTR09", "Ethno01", "EthnoTek", "Funk01",
    "Funk02", "Funk03", "Fusion01", "Fusion02", "Fusion03", "GatedKit", "HexKit", "HipHop1", "HipHop2", "HipHop3",
    "HipHop4", "HipHop5", "Jazz01", "Jazz02", "Jazz03", "Jazz04", "Jazz05", "Jazz06", "Jungle01", "Jungle02", "Jungle03",
    "Jungle04", "Latin01", "Latin02", "Latin03", "LiveKit1", "Metal", "NuJack", "Piccolo2", "Power01", "Power02",
    "RegTon01", "RegTon02", "RegTon03", "Rock01", "Rock02", "Rock03", "Rock04", "Rock05", "Rock06", "Rock07", "Rock08",
    "Rock09", "Rock10", "Rock11", "Rock12", "Rock13", "Rock14", "Rock15", "Rock16", "RoomKit1", "RoomKit2", "Samba",
    "Solid1", "Stndrd1", "Studio01", "Studio02", "Studio03", "Techno01", "Techno02", "Techno03", "Techno04", "Techno05",
    "Techno06", "Techno07", "Techno08", "Techno09", "Techno11", "Techno12", "Techno13", "Techno14", "Techno15", "Techno16",
    "TiteKit1", "TiteKit2", "Trance", "VoxKit", "VoxKit2", "World01", "World02", "80sR+B", "PrcSlide")

# print(f"Kits: {kits}")
# print(f"Len: {len(kits)}")
# print(f"#10: {kits[10]}")
# print(f"#101: {kits[101]}")
# print(f"Index of 'Rock11': {kits.index('Rock11')}")

def changeProgram(port, program):
    msg = mido.Message('program_change', channel=FUCKING_MIDI_CHANNEL, program=program)
    port.send(msg)
    print(msg)

def showHelp():
    for i in range(len(kits)):
        print(f"\t{i}: {kits[i]}", end='')
        if i % 5 == 4:
            print("")
    print("")

while True:
    sel = input(f"Select one (0-{len(kits)-1}, x to exit, ? for list): ")
    if sel=="?":
        showHelp()
        continue
    if sel=="x":
        break
    isel = int(sel)
    if isel >= len(kits) or isel < 0:
        print("Out of range!")
        continue
    print(f"\nSelected #{sel}: {kits[isel]}")
    changeProgram(outPort, isel)

outPort.close()
print("Done!")
