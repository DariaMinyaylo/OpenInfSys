MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.replace(':','')
MAC = int(MAC, 16)
MAC = bin(MAC)

print(MAC)
