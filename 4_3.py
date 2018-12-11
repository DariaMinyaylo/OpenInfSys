CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
CONFIG = CONFIG.split(' ')
VLAN = CONFIG[4].split(',')

print(VLAN)
