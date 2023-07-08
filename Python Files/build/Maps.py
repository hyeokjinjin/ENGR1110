from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter
import tkintermapview
import webbrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("REPLAC3 - Local Mechanic Search")
window.geometry("1024x768")
window.configure(bg = "#FFFFFF")
window.title("Mechanic Finder")

def close_win():
    window.after(3000, lambda: window.destroy())

def lookup():
    map_widget.set_address(entry_1.get())

def google_search():
    webbrowser.open_new("https://www.google.com/search?tbs=lf:1,lf_ui:14&tbm=lcl&sxsrf=ALiCzsbwjX7XF-pO1O5dH-WyIxUPDrG2kA:1668054412668&q=Car+Mechanics+Near+" + entry_1.get())

canvas = Canvas(window, bg = "#FFFFFF", height = 768, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("BG.png"))
image_1 = canvas.create_image(512.0, 384.0, image=image_image_1)


map_widget = tkintermapview.TkinterMapView(window, width=350, height=350, corner_radius=0)
map_widget.place(relx=0.58, rely=0.5, anchor=tkinter.W)
map_widget.set_position(32.6098566, -85.4807825)  #Auburn
map_widget.set_zoom(15)


button_image_1 = PhotoImage(file=relative_to_assets("Button.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: [lookup(), google_search(), close_win()], relief="flat")
button_1.place(x=709.0, y=675.0, width=118.0, height=54.0)


entry_image_1 = PhotoImage(file=relative_to_assets("zip_enter.png"))
entry_bg_1 = canvas.create_image(767.5, 638.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0, fg='black')
entry_1.place(x=617.0, y=612.0, width=301.0, height=50.0)


image_image_2 = PhotoImage(file=relative_to_assets("mechanic.png"))
image_2 = canvas.create_image(765.0, 308.0, image=image_image_2)

window.resizable(False, False)
window.mainloop()
