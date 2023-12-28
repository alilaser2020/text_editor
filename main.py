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
    [sg.Multiline(key="-DATA-", no_scrollbar=True, size=(60, 30))],
]

smileys_menu = smileys[1] + smileys[3] + smileys[5]

window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Word Count":
        full_text = values["-DATA-"]
        clean_text = full_text.replace("\n", " ").split(" ")
        word_count = len(clean_text)
        char_count = len("".join(clean_text))
        sg.popup_ok_cancel(f"Word count: {word_count}\nCharacter count: {char_count}", grab_anywhere=True)
    if event in smileys_menu:
        current_text = values["-DATA-"]
        new_text = current_text + " " + event
        window["-DATA-"].update(new_text)

window.close()
