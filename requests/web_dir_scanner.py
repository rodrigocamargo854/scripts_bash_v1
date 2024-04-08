import requests, sys

if len(sys.argv) != 3:
    print("Usage: python script.py <ip_address>")
    sys.exit(1)

host = "http://" + sys.argv[1]
wordlist_path = sys.argv[2]

try:
    with open(wordlist_path, 'r') as file:
        for word in file:
            word = word.strip()  # Removing white spaces and new lines
            get_dir_site = host + '/' + word if not host.endswith('/') else host + word
            site = requests.get(get_dir_site)
            status = site.status_code

            if status == 200:
                print("200 ok")
                print(get_dir_site)
     
		

except FileNotFoundError:
    print(f"File not found: {wordlist_path}")
    sys.exit(1)
    
sys.exit(0)
