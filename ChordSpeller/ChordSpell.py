# 65 - 71 is the range of the scale A-G via ord()
# I think notes also needs to be a class so that we can pass accidentals around easier
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
        self.qualities = {"Maj": [4,3,4],
                          "Min": [3,4,3],
                          "Aug": [4,4,3],
                          "Dim": [3,3,3],
                          "Dom": [4,3,3]
                          }
        self.intervals = self.qualities[q]
        self.name = r.name + q
        self.root = r
        # print('making note: ',self.root.letter, self.root.accidental[1],' in chord', self.name)
        self.third = next_third(self.root.letter, self.root.accidental[1], self.intervals[0])
        # print('making note: ', self.third.letter, self.third.accidental[1], ' in chord', self.name)
        self.fifth = next_third(self.third.letter,self.third.accidental[1], self.intervals[1])


def build_note(input):
    if len(input) == 2:
        if input[1] == '#':
            return Note(input[0], "1")
        elif input[1].upper() == 'B':
            return Note(input[0], "-2")

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


def next_third(note, accidental=0, interval=4):

    # find the next letter
    n = ord(note)
    if n + 2 > 71:
        t = n + 2 - 7
    else:
        t = n + 2
    # determine sharpness or flatness
    scale = build_chromatic_scale(note)
    # print(scale)
    scale_interval = scale.index(chr(t)) - scale.index(note) - accidental
    # print('scale interval {}  interval {}'.format(scale_interval, interval))
    if scale_interval < interval:
        key = (interval - scale_interval)

    elif scale_interval > interval:
        key = (scale_interval - interval)

    else:
        key = 0
    newNote = Note(chr(t), str(key))
    return newNote


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
            print(rootNote.name)
            print(rootNote.accidental)
            print(rootNote.letter)
            print(newChord.name)
            print(newChord.root.name)
            print(newChord.third.name)
            print(newChord.fifth.name)
