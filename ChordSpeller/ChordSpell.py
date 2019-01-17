# This program can accept a root note and a chord quality (Maj, Min, Dom, Dim, Min7b5, Aug)
# Using those inputs it will write any standard diatonic 7th chord for you!
# (still needs better UI, you have to know what to type or it'll crash)
# This program uses two classes (Note and Chord) and has no global state!

import unicodedata


class Note:
    def __init__(self, n, offset):
        self.accidentals = {
            "2": [chr(0x1d12a), 2],
            "1": [chr(0x266f), 1],
            "0": [chr(0x266e), 0],
            "-1": [chr(0x266d), -1],
            "-2": [chr(0x266d)*2, -2]
             }
        self.accidental = self.accidentals[offset]
        self.name = n + self.accidental[0]
        self.letter = n
        self.number = ord(self.letter)


class Chord:
    def __init__(self, r, q):
        self.qualities = {"Maj": [4, 3, 4],
                          "Min": [3, 4, 3],
                          "Aug": [4, 4, 3],
                          "Dim": [3, 3, 3],
                          "Dom": [4, 3, 3],
                          "Min7b5": [3, 3, 4]
                          }
        self.intervals = self.qualities[q]
        self.name = r.name + q
        self.root = r
        self.third = next_third(self.root.letter, self.root.accidental[1], self.intervals[0])
        self.fifth = next_third(self.third.letter, self.third.accidental[1], self.intervals[1])
        self.seventh = next_third(self.fifth.letter, self.fifth.accidental[1], self.intervals[2])


def build_note(input):
    if len(input) == 2:
        if input[1] == '#':
            return Note(input[0], "1")
        elif input[1].upper() == 'B':
            return Note(input[0], "-1")
    else:
        return Note(input[0], "0")


def build_chromatic_scale(start):
    precedes_sharp = [65, 67, 68, 70, 71]
    h = ord(start)
    steps = 0
    scale = ''
    while steps <= 12:
        scale += chr(h)
        if h in precedes_sharp:
            scale += '#'
            steps += 1
        if h == 71:
            h = 65
        else:
            h += 1
        steps += 1
    return scale


def next_third(note, accidental, interval):
    # find the next letter
    n = ord(note)
    if n + 2 > 71:
        t = n + 2 - 7
    else:
        t = n + 2
    # determine sharpness or flatness
    scale = build_chromatic_scale(note)
    print(scale)
    scale_interval = scale.index(chr(t)) - scale.index(note) - accidental
    print('scale interval {}  interval {}'.format(scale_interval, interval))
    if scale_interval != interval:
        key = (interval - scale_interval)
    else:
        key = 0
    print("key", key)
    newnote = Note(chr(t), str(key))
    return newnote


if __name__ == '__main__':
    while True:
        selection = input("enter a note").upper()
        if selection[0] == 'Q':
            break
        elif ord(selection[0]) > 71 or ord(selection[0]) < 65 or len(selection) > 2:
            continue
        else:
            rootNote = build_note(selection)
            quality = input("what kind of chord?")
            newChord = Chord(rootNote, quality)
                                   
            print(newChord.name)
            print("root: ", newChord.root.name)
            print("third: ", newChord.third.name)
            print("fifth: ", newChord.fifth.name)
            print("seventh: ", newChord.seventh.name)
