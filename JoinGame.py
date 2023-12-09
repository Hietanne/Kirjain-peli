import tkinter as tk
import socket

def join_game(ip_address):
    # Yritä yhdistää annettuun IP-osoitteeseen
    # Tässä esimerkissä yksinkertaisesti tulostetaan IP
    print(f"Trying to join game at {ip_address}")

# Luo pääikkuna
root = tk.Tk()
root.title("Join a LAN Lettergrid Game")

# Luo tekstikenttä IP-osoitteen syöttämiseen
entry_ip = tk.Entry(root)
entry_ip.pack(pady=5)

# Luo nappi peliin liittymiseen
btn_join = tk.Button(root, text="Join Game", command=lambda: join_game(entry_ip.get()))
btn_join.pack(pady=5)

# Käynnistä GUI:n tapahtumasilmukka
root.mainloop()
