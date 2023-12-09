import tkinter as tk
import subprocess
import os

# Käynnistetään palvelin kun painetaan näppäintä.
def start_server():
    subprocess.Popen(["python", "palvelin.py"])

def join_game():
    # This function will be called when the "Join Game" button is clicked
    # Here, you can add the logic to join a game
    subprocess.Popen(["python", "JoinGame.py"])

# Create the main window
root = tk.Tk()
root.title("LAN Lettergrid Game")

# Set window resolution to 800x800
root.geometry("800x800")

# Create and place buttons
btn_create_server = tk.Button(root, text="Create Server", command=start_server)
btn_create_server.pack(pady=10)

btn_join_game = tk.Button(root, text="Join Game", command=join_game)
btn_join_game.pack(pady=10)

# Start the GUI event loop
root.mainloop()