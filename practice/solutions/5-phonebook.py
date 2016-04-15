phonebook = {}

cmd = None
while cmd != 'quit':
    print('Command? list or add or get or quit')
    cmd = input()
    if cmd == 'list':
        for name in phonebook:
            print(name)
    elif cmd == 'add':
        print('Name?')
        name = input()
        print('Phone number?')
        number = input()
        phonebook[name] = number
    elif cmd == 'get':
        print('Name?')
        name = input()
        number = phonebook.get(name, 'no entry')
        print(name + ' -- ' + number)
    else:
        print('Unknown command: ' + cmd)
