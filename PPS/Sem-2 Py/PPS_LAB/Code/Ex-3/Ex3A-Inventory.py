"""
Given the following dictionary:

inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
Try to do the followings:
● Add a key to inventory called 'pocket'.
● Set the value of 'pocket' to be a list consisting of the strings 'seashell',
'strange berry', and 'lint'.
● .sort() the items in the list stored under the 'backpack' key.
● Then .remove('dagger') from the list of items stored under the 'backpack'
key.
● Add 50 to the number stored under the 'gold' key.
"""
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# 1
inventory.update(
    {
        "pocket": ['seashell', 'strange berry', 'lint']
    }
)
print(f"Created new key: {inventory}")

# 2
inventory.get('backpack').sort()
print(f"Sorted: {inventory.get('backpack')}")

# 3
inventory.get('backpack').remove('dagger')
print(f"Removed: {inventory.get('backpack')}")

# 4
add = inventory['gold'] + 50
print(f"Gold: {add}")

print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")