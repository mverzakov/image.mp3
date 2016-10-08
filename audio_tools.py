from __future__ import division

from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note


def make_music(notes_tracks, instruments, name='default.mid', tempo=120):
    midi = Midi(tempo=tempo,
                number_tracks=len(notes_tracks),
                instrument=instruments)
    for i, notes in enumerate(notes_tracks):
        midi.seq_notes(dict_to_notes(notes), track=i)
    midi.write("midi/{}".format(name))


def dict_to_notes(notes, volume=120):
    result = NoteSeq()
    for note in notes:
        pitch = note['note']
        octave = note['octave']
        duration = note['duration']
        volume = volume
        result.append(Note(pitch, octave, duration, volume))
    return result