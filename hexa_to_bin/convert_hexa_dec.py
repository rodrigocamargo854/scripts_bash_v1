import sys

def hex_to_decimal_ip(hex_ip):
    hex_parts = hex_ip.split(' ')
    decimal_parts = [str(int(part, 16)) for part in hex_parts]
    
    return '.'.join(decimal_parts)

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        hex_ip = sys.argv[1]
        decimal_ip = hex_to_decimal_ip(hex_ip)
        print(decimal_ip)
    else:
        print("Por favor, forneça um endereço IP hexadecimal como argumento.")
