import socket

def banner_grabing(port,host):
	try:
		s = socket.socket()
		s.timeout(2)
		s.connect((host,port))
		banner=s.recv(1024)
		return banner
		
	except Exception as e:
        return f"Não foi possível conectar ou receber o banner: {e}"
    finally:
        s.close()
        
#host = 'exemplo.com'  
#port = 80  
#banner = banner_grabbing(host, port)
#print(banner)
