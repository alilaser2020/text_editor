import PySimpleGUI as sg

sg.theme("GrayGrayGray")

smileys = [
    "Happy", [":)", ":D", "3>"],
    "Sad", [":(", ":|", "T_T"],
    "Other", [":3"],
]

layout_menu = [
    ["File", ["Open", "save", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Add", smileys],
]

layout = [
    [sg.Menu(layout_menu)],
    [sg.Text("Untitled", key="-DOCNAME-")],
    [sg.Multiline(key="-DATA-")],
]

window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
