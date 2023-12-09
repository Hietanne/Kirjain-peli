import socket
import tkinter as tk
import subprocess

class GameClient:
    def __init__(self, root):
        self.root = root
        self.root.title("LAN Lettergrid Game")

        # Lisää syöttökenttä IP-osoitteelle
        self.entry_ip = tk.Entry(self.root)
        self.entry_ip.pack()

        # Lisää liittymispainike
        self.btn_join = tk.Button(self.root, text="Join Game", command=self.join_game)
        self.btn_join.pack()

        # Käynnistä GUI:n tapahtumasilmukka
        self.root.mainloop()

    def join_game(self):
        server_ip = self.entry_ip.get()
        server_port = 12345  # Oletetaan, että portti on aina 12345

        # Tallenna IP-osoite tiedostoon
        with open("server_ip.txt", "w") as file:
            file.write(server_ip)

        try:
            self.client_socket.connect((server_ip, server_port))
            print(f"Connected to server at {server_ip}:{server_port}")
            self.root.destroy()  # Sulkee nykyisen ikkunan
            subprocess.Popen(["python", "startgame.py"])  # Avaa pelinäytön
        except Exception as e:
            print(f"Error connecting to server: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    client = GameClient(root)
