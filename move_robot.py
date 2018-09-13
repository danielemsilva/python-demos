# coding: utf-8
# Moving a robot
# 2017, Daniele Aparecida / UFCG

def moveUp(y_axis, steps):
    y_axis += steps
    return y_axis

def moveDown(y_axis, steps):
    y_axis -= steps
    return y_axis

def moveLeft(x_axis, steps):
    x_axis -= steps
    return x_axis

def moveRight(x_axis, steps): 
    x_axis += steps
    return x_axis

def isCenter(x_axis, y_axis):
    return x_axis == 0 and y_axis == 0

def isPortalPosition(x_axis, y_axis):
    return abs(y_axis) == (abs(x_axis) * 2)

x_axis = 0
y_axis = 0
end_game = False

print "Hello! The game is starting...\nEnter your movement: "

command = raw_input()
# The command is in the form "Z, n", where Z is the initial letter for the direction 
# (N for North, S for South, L for Left, R for right) and n is the number of steps.
command = command.split(' ')

direction = command[0]
steps = int(command[1])

while end_game == False:
    if direction == 'N':
        y_axis = moveUp(y_axis, steps)

    elif direction == 'S':
        y_axis = moveDown(y_axis, steps)
    
    elif direction == 'L':
        x_axis = moveLeft(x_axis, steps)
        
    elif direction == 'R':
        x_axis = moveRight(x_axis, steps)
        
    if steps == 0:
        end_game = True
        print "You took 0 steps! End of the game"
    
    elif isPortalPosition(x_axis, y_axis) and not isCenter(x_axis, y_axis):
        end_game = True
        print "Congratulations! Achievement of the portal (%d, %d)" % (x_axis, y_axis)

    else:
        print "Enter your movement: "
        command = raw_input()
        command = command.split(' ')

        direction = command[0]
        steps = int(command[1])
    
