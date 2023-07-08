from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def close_win():
    window.destroy()
    import SelectProb


car_types = ["SUVs",
             "Sedans & Wagons",
             "Coupes",
             "Convertibles & Wagons",
             "Electric"
]

suv = ["GLA",
       "GLB",
       "GLC",
       "GLC Coupe",
       "GLE",
       "GLE Coupe",
       "GLS",
       "G-Class",
       "Mercedes-Maybach GLS"
]

sedan = ["A-Class",
         "C-Class",
         "E-Class",
         "S-Class",
         "Mercedes-Maybach",
         "E-Class Wagon"
]

coupes = ["CLA Coupe",
          "C-Class Coupe",
          "E-Class Coupe",
          "CLS Coupe",
          "S-Class Coupe",
          "Mercedes-AMG GT 4-Door Coupe",
          "Mercedes-AMG GT"
]

conv = ["C-Class Cabriolet",
        "E-Class Cabriolet",
        "SL Roadster"
]

elec = ["EQB SUV",
        "EQS Sedan",
        "EQS SUV"
]


window = Tk()
window.title("REPLAC3 - Select Car & Problem")
window.geometry("1024x768")
window.configure(bg = "#FFFFFF")

canvas = Canvas(window, bg = "#FFFFFF", height = 768, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("BG.png"))
image_1 = canvas.create_image(512.0, 384.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("select_car.png"))
image_2 = canvas.create_image(765.0, 229.0, image=image_image_2)

button_image_1 = PhotoImage(file=relative_to_assets("next.png"))
next_button = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: [close_win()], relief="flat")
next_button.place(x=719.0, y=680.0, width=118.0, height=54.0)


car_select = Listbox()
prob_select = Listbox()
car_select.place(x=680, y=200)
prob_select.place(x=680, y= 465)


def list_color(e):
    prob_select.delete(0, END)
    if car_select.get(ANCHOR) == "SUVs":
         for item in suv:
             prob_select.insert(END, item)
    if car_select.get(ANCHOR) == "Sedans & Wagons":
         for item in sedan:
             prob_select.insert(END, item)
    if car_select.get(ANCHOR) == "Coupes":
         for item in coupes:
             prob_select.insert(END, item)
    if car_select.get(ANCHOR) == "Convertibles & Wagons":
         for item in conv:
             prob_select.insert(END, item)
    if car_select.get(ANCHOR) == "Electric":
         for item in elec:
             prob_select.insert(END, item)

def print_color(e):
    global car_type
    car_type = prob_select.get(ANCHOR)
    with open('cartype.txt', 'w') as f:
        f.write(car_type)
    print(car_type)

for item in car_types:
    car_select.insert(END, item)

car_select.bind("<<ListboxSelect>>", list_color)
prob_select.bind("<<ListboxSelect>>", print_color)

window.resizable(False, False)
window.mainloop()
