import socket
import threading
import random

class GameServerLogic:
    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.clients = []
        print(f"Game logic server listening on {host}:{port}")

    def handle_client(self, client_socket):
        try:
            while True:
                # Lähetetään pelilauta asiakkaalle
                client_socket.send(self.create_game_board().encode('utf-8'))
        except Exception as e:
            print(f"Connection error: {e}")
            client_socket.close()

    def create_game_board(self):
        # Luodaan pelilauta
        kirjaimet = "abdeghijklmnoqrstuvyäö"
        matriisi = [''.join(random.choice(kirjaimet) for _ in range(13)) for _ in range(10)]
        return '\n'.join(matriisi)

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr} established.")
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

def handle_game_logic():
    server = GameServerLogic('0.0.0.0', 12346)  # Käytetään eri porttia kuin yhteyspalvelimelle
    server.start()

if __name__ == "__main__":
    handle_game_logic()
