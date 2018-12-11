NAT = "ip nat inside source list ACL interface FastEthernet01 overload"
NEWNAT = NAT.replace('Fast', 'Giga')
print(NAT.replace('Fast', 'Giga'))
