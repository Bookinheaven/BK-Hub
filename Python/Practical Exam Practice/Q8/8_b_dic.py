"""
Given the following dictionary:
inventory = {
'gold' : 500,
'pouch' : [‘stone', 'klint', 'wine', 'gem’,],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
Try to do the following operations and show the dictionary elements after each operation:
 Add a new key to the inventory ‘purse’ with list of values such as ‘small’, ‘medium’,
‘large’,’XL’.
 Sort the items under the ‘pouch’ key
 Delete the value ‘bedroll’ under ‘backpack’ key
 Add 100 to the value of ‘gold’ key
"""

inventory = {
'gold' : 500,
'pouch' : ['stone', 'klint', 'wine', 'gem'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory.update({ 'purse': ['small', 'medium','large','XL']})
inventory['pouch'].sort()
inventory['backpack'].remove('bedroll')
inventory['gold'] += 100
print(inventory)