from pathlib import Path
from tkinter import *
from tkinter import ttk
import pandas as pd
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dropdown_2():
    global dropdown2
    dropdown2 = ttk.Combobox(window, value=master_prob_list)
    dropdown2.place(x=650, y=430)
    dropdown2.bind("<<ComboboxSelected>>", threeprob)
    button_2.place(x=700.0, y=500.0, width=118.0, height=54.0)

def dropdown_1():
    global button_4
    global dropdown1
    dropdown1 = ttk.Combobox(window, value=master_prob_list)
    dropdown1.place(x=650, y=330)
    dropdown1.bind("<<ComboboxSelected>>", twoprob)
    button_4.place(x=880, y=320.0, width=54.0, height=54.0)
    button_2.place(x=700.0, y=400.0, width=118.0, height=54.0)

def close_win():
    window.destroy()
    import Maps

def oneprob(e):
    global answer
    global ans_list
    position1 = []
    ans_list = []
    user_prob = dropdown.get()
    for i in range(len(hint_list)):
        if user_prob in hint_list[i]:
            position1.append(hint_list.index(hint_list[i]))
    for pos in position1:
        ans_list.append(prob_list[pos])
    print(ans_list)

def twoprob(e):
    global answer
    global ans_list
    ans_list = []
    position1 = []
    position2 = []
    user_prob = dropdown.get()
    user_prob2 = dropdown1.get()
    for i in range(len(hint_list)):
        if user_prob in hint_list[i]:
            position1.append(hint_list.index(hint_list[i]))
    for i in range(len(hint_list)):
        if user_prob2 in hint_list[i]:
            position2.append(hint_list.index(hint_list[i]))
    for pos in set(position1).intersection(position2):
        ans_list.append(prob_list[pos])
    if len(set(position1).intersection(position2)) == 0:
        ans_list = ['Combination Not Found in List of Potential Issues. Try Again.']
    print(ans_list)

def threeprob(e):
    global answer
    global ans_list
    ans_list = []
    position1 = []
    position2 = []
    position3 = []
    user_prob = dropdown.get()
    user_prob2 = dropdown1.get()
    user_prob3 = dropdown2.get()
    for i in range(len(hint_list)):
        if user_prob in hint_list[i]:
            position1.append(hint_list.index(hint_list[i]))
    for i in range(len(hint_list)):
        if user_prob2 in hint_list[i]:
            position2.append(hint_list.index(hint_list[i]))
    for i in range(len(hint_list)):
        if user_prob3 in hint_list[i]:
            position3.append(hint_list.index(hint_list[i]))
    set1 = set(position1).intersection(position2)
    for pos in set1.intersection(position3):
        ans_list.append(prob_list[pos])
    if len(set1.intersection(position3)) == 0:
        ans_list = ['Combination Not Found in List of Potential Issues. Try Again.']
    print(ans_list)

def show():
    ans_listbox.delete(0, "end")
    for item in ans_list:
        ans_listbox.insert(0, item)

def part_finder(e):
    global link
    in1 = ans_listbox.get(ANCHOR)
    if in1 in Solution_Dict:
        in2 = Solution_Dict.get(in1)
        in3 = in2.replace(" ", "+")
        car_type = open('cartype.txt', 'r')
        car = car_type.readline(-1)
        car = car.replace(" ", "+")
        link = "https://mbparts.mbusa.com/search?search_str=" + car + "+" + in3
    else:
        link = ''

def open_internet():
    webbrowser.open_new(link)


window = Tk()
window.geometry("1024x768")
window.configure(bg = "#FFFFFF")
window.title("Problem Selection")


# Read the columns (within limits) on the default 1st sheet of Excel file
LowDeadBatt = pd.read_excel('Problems.xlsx', usecols='A', nrows=4)
PoorAlign = pd.read_excel('Problems.xlsx', usecols='B', nrows=5)
MisTire = pd.read_excel('Problems.xlsx', usecols='C', nrows=4)
FlatLowTire = pd.read_excel('Problems.xlsx', usecols='D', nrows=4)
RustBrake = pd.read_excel('Problems.xlsx', usecols='E', nrows=4)
BadRad = pd.read_excel('Problems.xlsx', usecols='F', nrows=5)
ClogFil = pd.read_excel('Problems.xlsx', usecols='G', nrows=4)
SparkPlug = pd.read_excel('Problems.xlsx', usecols='H', nrows=4)
DeadStart = pd.read_excel('Problems.xlsx', usecols='I', nrows=4)
IrregTire = pd.read_excel('Problems.xlsx', usecols='J', nrows=1)
LooseFuel = pd.read_excel('Problems.xlsx', usecols='K', nrows=4)
BadOxy = pd.read_excel('Problems.xlsx', usecols='L', nrows=4)
LowOil = pd.read_excel('Problems.xlsx', usecols='M', nrows=5)
FailCat = pd.read_excel('Problems.xlsx', usecols='N', nrows=5)

master_list = pd.read_excel('Problems.xlsx', usecols='P', nrows=39)
master_prob_list = master_list['Problems'].tolist()

# Utilize dictionary in order to allow to find keys and values to link to user's problem
Problem_Dict = {
    'Low/Dead Battery': LowDeadBatt['Low/Dead Battery'].tolist(),
    'Poor Alignment': PoorAlign['Poor Alignment'].tolist(),
    'Imbalanced Tires': MisTire['Imbalanced Tires'].tolist(),
    'Flat/Low Tires': FlatLowTire['Flat/Low Tires'].tolist(),
    'Rusted Brakes': RustBrake['Rusted Brakes'].tolist(),
    'Bad Radiator': BadRad['Bad Radiator'].tolist(),
    'Clogged Filter': ClogFil['Clogged Filter'].tolist(),
    'Spark Plug Issues': SparkPlug['Spark Plug Issues'].tolist(),
    'Dead Starter Motor': DeadStart['Dead Starter Motor'].tolist(),
    'Irregular Tire Pressure': IrregTire['Irregular Tire Pressure'].tolist(),
    'Loose Fuel Caps': LooseFuel['Loose Fuel Caps'].tolist(),
    'Bad Oxygen Sensor': BadOxy['Bad Oxygen Sensor'].tolist(),
    'Low Oil': LowOil['Low Oil'].tolist(),
    'Failing Cat. Converter': FailCat['Failing Cat. Converter'].tolist()
}

# Utilize dictionary in order to allow to find keys and values to link to user's problem
Solution_Dict = {
    'Low/Dead Battery': "Car+Battery",
    'Rusted Brakes': "Brakes",
    'Bad Radiator': "Radiator",
    'Clogged Filter': "Filter",
    'Spark Plug Issues': "Spark Plug",
    'Loose Fuel Caps': "Fuel Caps",
    'Bad Oxygen Sensor': "Oxygen Sensor",
    'Failing Cat. Converter': "Catalytic Converter"
}

# One way to find the key of dictionary by values
prob_list = list(Problem_Dict.keys())
hint_list = list(Problem_Dict.values())


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("BG.png"))
image_1 = canvas.create_image(
    512.0,
    384.0,
    image=image_image_1
)


dropdown = ttk.Combobox(window, value=master_prob_list)
dropdown.place(x=650, y=230)
dropdown.bind("<<ComboboxSelected>>", oneprob)


button_image_1 = PhotoImage(
    file=relative_to_assets("next.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [open_internet(), close_win()],
    relief="flat"
)
button_1.place(
    x=700.0,
    y=710.0,
    width=118.0,
    height=54.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("FindSolution.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=show,
    relief="flat"
)
button_2.place(
    x=700.0,
    y=300.0,
    width=118.0,
    height=54.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("add.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [dropdown_1()],
    relief="flat"
)
button_3.place(
    x=880.0,
    y=220.0,
    width=54.0,
    height=54.0
)

button_image_4 = PhotoImage(
        file=relative_to_assets("add.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [dropdown_2()],
    relief="flat"
)

image_image_2 = PhotoImage(
    file=relative_to_assets("newnewnew.png"))
image_2 = canvas.create_image(
    765.0,
    348.0,
    image=image_image_2
)


ans_listbox = Listbox(window, width=48, height=6, bg='#F5F5F5', highlightthickness=0, fg='black')
ans_listbox.place(x=550, y=600)
ans_listbox.bind("<<ListboxSelect>>", part_finder)


window.resizable(False, False)
window.mainloop()
