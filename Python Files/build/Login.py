from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import ImageTk, Image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("REPLAC3 - Login")
window.geometry("1024x768")
window.configure(bg="#FFFFFF")
window.title("Login")


def close_win():
    window.destroy()
    import SelectCar
    
def printUser():
    puser = entry_2.get()
    print(puser)
    
def printPass():
    global ppass
    ppass = entry_1.get()
    print(ppass)


canvas = Canvas(window, bg = "#FFFFFF", height = 768, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
bg1 = ImageTk.PhotoImage(file="assets/BG.png")
my_canvas = canvas.create_image(512.0, 384.0, image=bg1)


button_image_1 = PhotoImage(file=relative_to_assets("GuestLogin.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: close_win(), relief="flat")
button_1.place(x=638.0, y=590.0, width=272.08453369140625, height=86.0)


button_image_2 = PhotoImage(file=relative_to_assets("Login.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: [printUser(), printPass(), close_win()], relief="flat")
button_2.place(x=671.0, y=436.0, width=198.0, height=82.0)


image_image_2 = PhotoImage(file=relative_to_assets("LoginBack.png"))
image_2 = canvas.create_image(770.0, 182.0, image=image_image_2)


entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(773.5, 305.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0, fg='black')
entry_1.place(x=623.0, y=278.0, width=301.0, height=53.0)


entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(769.5, 169.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0, fg='black')
entry_2.place(x=619.0, y=143.0, width=301.0, height=50.0)

window.resizable(False, False)
window.mainloop()
