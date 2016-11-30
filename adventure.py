from data import locations

directions = {
    'west':(-1,0),
    'east':(1,0),
    'north':(0,-1),
    'south':(0,1),
}

position = (0,0)

while True:
    location = locations[position]
    print 'you are at the %s' % location

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible__location = locations.get(possible_position)
        if possible__location:
            print 'to the %s is a %s' % (k, possible__location)
            valid_directions[k] = possible_position

    direction = raw_input('which direction to you want to go?\n')
    position = valid_directions[direction]


