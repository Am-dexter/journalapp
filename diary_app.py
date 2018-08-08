

def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------------------')
    print('        MY JOURNAL APP')
    print('--------------------------------')


def run_event_loop():
    print('What do you want to do with your Journal?')
    cmd = None

    journal_data = []

    while cmd != 'x':
        cmd = input('(L)is entries, (A)dd entries, E(x)it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand, '{}'.".format(cmd))

    print('Done, Awesome')


def list_entries(data):
    print('Your Journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}], {}'.format(idx + 1, entry))


def add_entries(data):
    text = input('Type your entry, <Enter> for exit; ')
    data.append(text)


main()