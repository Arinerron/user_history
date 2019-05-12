import subprocess, getpass, os

directory = 'logs'

user = getpass.getuser()

if not os.path.exists(directory):
    os.makedirs(directory)

def getCommands():
    output = subprocess.getoutput('w | cat') # ignore command injection for now
    
    output = output.split('\n')[1:]
    header = output.pop(0)

    offset = header.find('WHAT')
    return [[x.split(' ')[0], x[offset + 1:]] for x in output]


previous = []

while True:
    commands = getCommands()
    compileds = []


    for command in commands:
        compiled = command[0] + ': ' + command[1]
        compileds.append(compiled)

        if not compiled in previous:
            previous.append(compiled)

            # log command
            print(command[1])
            with open('logs/%s_history' % command[0], 'a+') as f:
                f.write(command[1] + '\n')
    
    for compiled in previous:
        if not compiled in compileds and not compiled == '%s: /bin/sh -c w | cat' % user and not compiled == '%s: w' % user and not compiled == '%s: cat' % user:
            previous.remove(compiled)

            # no longer executing command

