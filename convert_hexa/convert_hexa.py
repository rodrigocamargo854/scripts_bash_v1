def hex_to_ascii(hex_string):
    
    hex_string = hex_string.replace("0x", "").replace(" ", "")
           
    ascii_string = ''.join([chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2)])
    
    return ascii_string

# Exemplo de uso
hex_input = input("hexadecial chr ")
ascii_output = hex_to_ascii(hex_input)

print("Valor ASCII:", ascii_output)
