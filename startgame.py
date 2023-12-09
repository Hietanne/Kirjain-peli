import socket
import tkinter as tk

def fetch_game_board(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        game_board = client_socket.recv(4096).decode('utf-8')
        client_socket.close()
        return game_board.split('\n')  # Muutetaan pelilauta listaksi rivejä
    except Exception as e:
        print(f"Error connecting to game server: {e}")
        return []

def create_board_frame(root, game_board):
    board_frame = tk.Frame(root)
    board_frame.pack()

    for row_idx, row in enumerate(game_board):
        for col_idx, letter in enumerate(row):
            # Muutetaan kirjain isoksi kirjaimeksi
            letter = letter.upper()
            label = tk.Label(board_frame, text=letter, font=("Helvetica", 18), width=2, borderwidth=1, relief="solid")
            label.grid(row=row_idx, column=col_idx)
    return board_frame

def main():
    root = tk.Tk()
    root.title("Game Screen")
    root.geometry("600x600")

    # Lue IP-osoite tiedostosta
    with open("server_ip.txt", "r") as file:
        server_ip = file.read().strip()
    server_port = 12346

    game_board = fetch_game_board(server_ip, server_port)
    if game_board:
        create_board_frame(root, game_board)

    root.mainloop()

if __name__ == "__main__":
    main()
