# locations = {
#     (0,0): 'House',
#     (0,1): 'Lake',
#     (1,0): 'Park',
#     (1,1): 'Market',
# }

locations = {
    (0,0): {'pName':'House','map':'H','Description':'A lovely Venecian Mannor','Objects':['keys','coat']},
    (0,1): {'pName':'Lake','map':'L','Description':"It's Deep - Oh So Deep",'Objects':['fishing rod','lilly']},
    (1,0): {'pName':'Park','map':'P','Description':'Green, with trees and grass','Objects':['flowers','grass']},
    (1,1): {'pName':'Market','map':'M','Description':'Sundays and Tuesdays Only!!','Objects':['spices','toys']},
}


inventory = []


def item_action(items, item, action):

    if action == 'pickup':

        if item in items:
            items.remove(item)
            inventory.append(item)

            print 'You have picked up the %s\n' % item

        else:
            print 'You can not see this item'
            show_inventory()

    if action == 'drop':

        if item in inventory:
            inventory.remove(item)
            items.append(item)

            print 'You have dropped the %s\n\n' % item
            show_inventory()

        else:
            print 'you are not holding this item'

def show_inventory():
    print "You are currently carrying : %s" % inventory