import tkinter as tk
import subprocess
import os

# Käynnistetään palvelin kun painetaan näppäintä.
def start_server():
    btn_create_server.config(state="disabled")  # Estä nappi klikkaamisen jälkeen
    subprocess.Popen(["python", "palvelin.py"])
    # Oletetaan, että palvelin kirjoittaa IP-osoitteen tiedostoon
    try:
        with open("server_ip.txt", "r") as file:
            server_ip = file.read().strip()
            lbl_server_ip.config(text=f"Server IP: {server_ip}")
    except Exception as e:
        lbl_server_ip.config(text="Error reading server IP")

def join_game():
    subprocess.Popen(["python", "JoinGame.py"])

# Create the main window
root = tk.Tk()
root.title("LAN Lettergrid Game")
root.geometry("400x400")

# Luodaan Label IP-osoitteelle
lbl_server_ip = tk.Label(root, text="Server IP: Not Started")
lbl_server_ip.pack(pady=10)

# Create and place buttons
btn_create_server = tk.Button(root, text="Create Server", command=start_server)
btn_create_server.pack(pady=10)

btn_join_game = tk.Button(root, text="Join Game", command=join_game)
btn_join_game.pack(pady=10)

# Start the GUI event loop
root.mainloop()
