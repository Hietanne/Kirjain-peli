import socket
import tkinter as tk

def fetch_game_board(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        game_board = client_socket.recv(4096).decode('utf-8')
        client_socket.close()
        return game_board
    except Exception as e:
        print(f"Error connecting to game server: {e}")
        return None

def main():
    root = tk.Tk()
    root.title("Game Screen")

    server_ip = "127.0.0.1"  # Oletetaan, että palvelin on paikallisessa koneessa
    server_port = 12346  # Oletetaan, että pelipalvelin käyttää porttia 12346

    game_board = fetch_game_board(server_ip, server_port)
    if game_board:
        tk.Label(root, text=game_board).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
