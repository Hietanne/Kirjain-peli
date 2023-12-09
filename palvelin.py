import socket

def get_local_ip():
    # Yritetään saada paikallinen IP-osoite
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Ei tarvitse olla todellinen osoite, vain UDP-yhteys yritys on tarpeen
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return "Unknown"

def start_server():
    # Loput palvelimen koodista...
    pass

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Server's local IP: {local_ip}")
    start_server()
