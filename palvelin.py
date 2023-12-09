import socket
import subprocess
import threading

class GameServer:
    def __init__(self, port=12345, max_players=2):
        self.host = self.get_local_ip()
        self.port = port
        self.max_players = max_players
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.clients = []
        print(f"Server is listening on {self.host}:{port}")

        # Kirjoita IP-osoite tiedostoon
        with open("server_ip.txt", "w") as file:
            file.write(self.host)

    def get_local_ip(self):
        # Luodaan väliaikainen socket yhteys saadakseen LAN IP-osoite
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Käytetään Google DNS:ää IP-osoitteen löytämiseksi, ei muodosteta todellista yhteyttä
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception as e:
            return "127.0.0.1"  # Palautetaan localhost osoite virhetilanteessa

    def start_game(self):
        # Alustetaan peli ja käynnistetään pelipalvelin sekä startgame.py host-koneella
        print("Game is starting...")
        subprocess.Popen(["python", "pelipalvelin.py"])  # Käynnistää pelipalvelimen
        subprocess.Popen(["python", "startgame.py"])  # Avaa pelinäytön host-koneella
        # Lisää muita toimintoja tarvittaessa

    def handle_client(self, client_socket, addr):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Message from {addr}: {message}")
                    # Käsittele viesti täällä
            except:
                client_socket.close()
                return

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Connection from {addr} established.")
            if len(self.clients) == self.max_players:
                self.start_game()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, addr))
            client_thread.start()

if __name__ == "__main__":
    server = GameServer()
    server.start()
