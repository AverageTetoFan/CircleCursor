import tkinter as tk
import pyautogui
import pystray
from PIL import Image, ImageDraw
import threading


# ============================================================
# CONFIGURACIÓN
# ============================================================

RADIO = 12
COLOR = "red"


# ============================================================
# VENTANA DEL CÍRCULO
# ============================================================

root = tk.Tk()

root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "black")

root.geometry(f"{RADIO * 2}x{RADIO * 2}")

canvas = tk.Canvas(
    root,
    width=RADIO * 2,
    height=RADIO * 2,
    bg="black",
    highlightthickness=0
)

canvas.pack()

canvas.create_oval(
    2,
    2,
    RADIO * 2 - 2,
    RADIO * 2 - 2,
    outline=COLOR,
    width=3
)


# ============================================================
# MOVER EL CÍRCULO CON EL CURSOR
# ============================================================

def seguir_cursor():
    try:
        x, y = pyautogui.position()

        root.geometry(
            f"{RADIO * 2}x{RADIO * 2}+{x - RADIO}+{y - RADIO}"
        )

        root.after(10, seguir_cursor)

    except tk.TclError:
        pass


# ============================================================
# ICONO DE LA BANDEJA DEL SISTEMA
# ============================================================

def crear_icono():
    # Crear una imagen sencilla para el icono
    imagen = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    dibujo = ImageDraw.Draw(imagen)

    dibujo.ellipse(
        (10, 10, 54, 54),
        outline="red",
        width=6
    )

    # Menú con botón "Salir"
    menu = pystray.Menu(
        pystray.MenuItem(
            "Salir",
            salir
        )
    )

    icono = pystray.Icon(
        "CursorVisual",
        imagen,
        "Cursor Visual",
        menu
    )

    icono.run()


# ============================================================
# SALIR DEL PROGRAMA
# ============================================================

def salir(icono, item):
    icono.stop()

    root.after(
        0,
        root.destroy
    )


# ============================================================
# INICIAR
# ============================================================

seguir_cursor()

# El icono de la bandeja se ejecuta en otro hilo
threading.Thread(
    target=crear_icono,
    daemon=True
).start()

root.mainloop()
