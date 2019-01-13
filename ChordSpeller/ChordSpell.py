# 65 - 71 is the range of the scale A-G via ord()
#


def build_chromatic_scale(start):
    precedes_sharp = [65,67,68,70,71]
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


def next_third(note,accidental, interval=4):
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
    print('scale interval {}  interval {}'.format(scale_interval,interval))
    if scale_interval < interval:
        key = '#' * (interval - scale_interval)
    elif scale_interval > interval:
        key = 'b' * (scale_interval - interval)
    else:
        key = ''
    return chr(t)+key


if __name__ == '__main__':
    while True:
        selection = input("enter a note").upper()
        if len(selection) == 2:
            choice = selection[0]
            if selection[1] == 'B':
                accidental = -1
            elif selection[1] =='#':
                accidental = 1
            else:
                accidental = 0
        else:
            choice = selection[0]
            accidental = 0
        if choice == 'Q':
            break
        elif ord(choice) > 71 or ord(choice) < 65 or len(selection) > 2 or (selection[1] !='B' and selection[1] != '#'):
            continue
        else:
            print('user input{}',format(selection))
            print('parsed acdtnl {}'.format(accidental))
            print(next_third(choice,accidental))
