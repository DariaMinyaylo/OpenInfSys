import time
delay = 10
def xor_cipher( str, key ):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return  encript_str    
 
strg = "Много разных букв"
key  = 2
print( "original:\t", strg )
encr_strg = xor_cipher( strg, key ) 
print( "encript:\t", encr_strg )
print( "decript:\t", xor_cipher( encr_strg, key ) )

time.sleep (delay)