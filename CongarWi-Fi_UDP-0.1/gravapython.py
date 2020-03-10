# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
    Funcoes de geracao de arquivo mid
    TO DO:
        Importar arquivo gerado pelo chuck      ok
        Gerar variável de notas                 ok
        Gerar variável de duracoes              ok
        Gerar variável de notas para o MIDI     ok
        Gerar varável de duracoes para o MIDI   ok
        Executar arquivo midi: pmidi -p 14:0 file.mid 

    @author: claudiorogerio
    year: 2020
"""

from midiutil import MIDIFile
import sys

outfile_midi = "midi_chuck"
file_chuck = "out.txt"

show = 1

my_midi_file = []
with open("out.txt") as f:
    for line in f:
        if line != '\n':
            if show:
                print(line)
            line = line.split()
            my_midi_file.append({"track": int(line[0]), "pitch": int(
                line[1]), "dur": float(line[2]), "vol": round(float(line[3])*100)})


track = 0    # n utilizado
channel = 0
time = 0    # In beats

# duration = 1    # In beats
tempo = int(sys.argv[1])   # In BPM
volume = 100  # 0-127 n utilizado

##


def create_midi_file(mididata, outfile, type_write_midi):

    # loop para ver total tracks
    total_track = 0
    for nota in mididata:
        if nota["track"] > total_track:
            total_track = nota["track"]

    print("Total de tracks:", total_track)

    if type_write_midi != "total":
        total_track = 0

    outfile += "_" + type_write_midi + ".mid"

    # Criar um track, formato padrao automatico
    MyMIDI = MIDIFile(total_track + 1)

    # total
    for tk in range(0, total_track+1):
        print("Tracks:", tk, total_track)
        MyMIDI.addTempo(tk, time, tempo)    # add to tempo inicial

        i_time = 0    # ajuste do tempo musical
        for nota in mididata:
            if show:
                print("Nota: ", nota["track"], i_time,
                      nota["pitch"], nota["dur"], nota["vol"])

            # add notas midi por track
            if type_write_midi != "total":
                # sempre sera 1 track por melodia criada
                if nota["track"] == int(type_write_midi):
                    # porcentagem para inteiro
                    MyMIDI.addNote(
                        0, channel, nota["pitch"], time + i_time, nota["dur"], nota["vol"])
                    i_time += 1
            else:
                if nota["track"] == tk:    # varios tracks
                    MyMIDI.addNote(nota["track"], channel, nota["pitch"], time +
                                   i_time, nota["dur"], nota["vol"])  # porcentagem para inteiro
                    i_time += 1

    # gravar arquivo
    with open(outfile, "wb") as output_file:
        MyMIDI.writeFile(output_file)


# loop para ver total tracks
total_track = 0
for nota in my_midi_file:
    if nota["track"] > total_track:
        total_track = nota["track"]

# criar arquivos midis para cada melodia
for tk in range(0, total_track+1):
    create_midi_file(my_midi_file, outfile_midi, str(tk))

# criar melodias unidas
create_midi_file(my_midi_file, outfile_midi, "total")


# nao utilizado
# class midi_file():
#    "Classe para registro de arquivo .mid"
#    def __init__( self, track, pitch, dur, volume ):
#        self.track = track
#        self.pitch = pitch
#        self.dur = dur
#        self.volume = volume
