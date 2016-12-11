from data import *

directions = {
    'west':(-1,0),
    'east':(1,0),
    'north':(0,-1),
    'south':(0,1),
}

position = (0,0)

while True:
    location = locations[position]['pName']
    noOfItems = len(locations[position]['Objects'])
    items = locations[position]['Objects']

    print 'you are at the %s - %s\n\nThere are %s items you can pick up.' % (location, locations[position]['Description'],noOfItems)
    for x in items:
        print 'You can pick up the %s' % (x)

    print '\n'
    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible__location = locations.get(possible_position,{}).get('pName')
        if possible__location:
            print 'to the %s is a %s' % (k, possible__location)
            valid_directions[k] = possible_position

    direction = raw_input("\nType the direction to you want to go? Or type 'Pickup (item)' to pickup an item\n")

    command = direction.partition(' ')[0]

    if len(direction.split()) > 1:
        item = direction.split(' ')[1].lower()

    if command == 'pickup' or command == 'drop':
        item_action(items,item,command)
    elif command in valid_directions:
        position = valid_directions[direction]
    elif command == 'inventory':
        show_inventory()
    else:
        print 'This is not a Valid Option'





