import tkinter as tk
import pyautogui

# Tamaño del círculo
RADIO = 12

# Crear ventana
root = tk.Tk()
root.overrideredirect(True)       # Sin bordes
root.attributes("-topmost", True) # Siempre encima
root.attributes("-transparentcolor", "black")

# Ventana pequeña
root.geometry(f"{RADIO * 2}x{RADIO * 2}")

# Canvas transparente
canvas = tk.Canvas(
    root,
    width=RADIO * 2,
    height=RADIO * 2,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# Dibujar círculo
canvas.create_oval(
    2, 2,
    RADIO * 2 - 2,
    RADIO * 2 - 2,
    outline="red",
    width=3
)

def seguir_cursor():
    x, y = pyautogui.position()

    # Centrar el círculo en el cursor
    root.geometry(
        f"{RADIO * 2}x{RADIO * 2}+{x - RADIO}+{y - RADIO}"
    )

    root.after(10, seguir_cursor)

seguir_cursor()
root.mainloop()