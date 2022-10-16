# Carder Brooks
# Assignment 5
# Milestone #1 Implementation

# references cited:
    # https://realpython.com/pysimplegui-python/
    # https://www.geeksforgeeks.org/user-input-in-pysimplegui/
    # https://www.geeksforgeeks.org/themes-in-pysimplegui/
    # https://holypython.com/gui-with-python-checkboxes-and-radio-buttons-pysimplegui-part-ii/
    # https://www.codegrepper.com/code-examples/python/how+to+open+.png+file+in+python


import PySimpleGUI as sg

# translation dictionary
key_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "   "
}

# get some color going!!!
sg.theme("DarkBlue8")

# initialize input value variable
read_data = ""

######################## main window sections ##############################

# input type, Enlgish or Morse code
select_input_type = [
    [sg.Text("Select what you're translsating from.")],
    [sg.Radio("English", "RADIO1", default=True, key="-ENGLISH-")],
    [sg.Radio("Morse Code", "RADIO1", default=False, key="-MORSE-")],
    [sg.HorizontalSeparator()], [sg.HorizontalSeparator()]
]

# receive input from the user, either text or file upload
input_row = [
    [sg.Text("Enter or upload your message.")],
    [sg.InputText('Type in or copy & paste text here', size=(100, 1), enable_events=True, key="-TEXT-")],
    [sg.Text("OR")],
    [sg.Text("Upload a file"),
    sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
    sg.FileBrowse()],
    [sg.HorizontalSeparator()], [sg.HorizontalSeparator()]
]

# submission and cancel buttons
submission_row = [
    [sg.Text("Submit your message for translation.")],
    [sg.Submit(), sg.Cancel()]
]

# other options
extras_row = [
    [], [], [], [], [], [], [], [], [],
    [sg.HorizontalSeparator()],[sg.HorizontalSeparator()], [sg.HorizontalSeparator()], [sg.HorizontalSeparator()],
    sg.Button("Advanced Options", key="-ADVANCED-"),
    sg.Button("Key", key="-TRANS KEY-"),
    sg.Button("Suggested Messages", key="-SUGG-")
]

######################## end main window sections ########################

###### build the main window
main_layout = [
    [select_input_type, input_row, submission_row, extras_row]
]

##### create main window
main_window = sg.Window("Morse Code Translator", main_layout)


############################## event loop ##############################

while True:
    main_event, main_values = main_window.read()

# terminate if window close or cancel button clicked
    if main_event == "Cancel" or main_event == sg.WIN_CLOSED:
        break

# user uploads a file
    if main_event == "-FILE-":
        file = main_values["-FILE-"]
        # open file and get submitted text
        with open(file, 'r', encoding="utf-8") as f:
            read_data = f.read()

# user inputs text into the text box
    if main_event == "-TEXT-":
        read_data = main_values["-TEXT-"]

# Advanced Options button
    if main_event == "-ADVANCED-":
        advanced_layout = [
            [sg.Text("Select which advanced options you'd like enabled.")],
            [sg.HorizontalSeparator()],
            [sg.Checkbox("Insert slashes between words in translated message", default=False, key="-SLASH-")],
            [sg.Checkbox("", default=False)],
            [sg.Checkbox("", default=False)]
        ]
        advanced_window = sg.Window("Advanced Options", advanced_layout, margins=(100, 50))
        advanced_event, advanced_values = advanced_window.read()

# Key button
    if main_event == "-TRANS KEY-":
        trans_key_layout = [
            [sg.Image("trans_key.png")],
            [sg.Text("https://en.wikipedia.org/wiki/Morse_code")]
        ]
        trans_key_window = sg.Window("Translation Key", trans_key_layout, margins=(100, 50))
        trans_key_event, trans_key_values = trans_key_window.read()

# Suggested Messages button
    if main_event == "-SUGG-":

        eng_column = [
            [sg.Text("SOS")],
            [sg.Text("HELP")]
        ]

        morse_column = [
            [sg.Text("... --- ...")],
            [sg.Text(".... . .-.. .--.")]
        ]

        sugg_layout = [
            [sg.Column(eng_column), sg.VSeperator(), sg.Column(morse_column)]
        ]

        sugg_window = sg.Window("Translation Key", sugg_layout, margins=(100, 50))
        sugg_event, sugg_values = sugg_window.read()

# user submits input
    if main_event == "Submit":

        #make input string upper-case for proper translation
        read_data = read_data.upper()
        # initialite variable
        output = ""

        # translation engine
        for char in read_data:

            # character is not supported
            if char not in key_dict:
                error_layout = [
                    [sg.Text("Unsupported input type. Please only enter letters and numerals. Provided translation "
                             "will omit any other characters.")]
                ]
                error_window = sg.Window("ERROR!", error_layout, margins=(100, 50))
                error_event, error_values = error_window.read()

            # character supported
            else:
                output = output + key_dict[char] + " "

        input_column = [
            [sg.Text("Original Message:")],
            [sg.Text(read_data)]
        ]

        output_column = [
            [sg.Text("Translated Message:")],
            [sg.Text(output)] # placeholder translation example
        ]

        out_layout = [
            [sg.Text("Here is your translation.")],
            [sg.Column(input_column), sg.VSeperator(), sg.Column(output_column)],
            [], [], [], [], [], [], [], [], [], [], [],
            [sg.Button("Download this as a file?", key="-DOWNLOAD-")],
        ]
        window = sg.Window("Translation", out_layout, margins=(100, 50))
        out_event, out_values = window.read()

main_window.close()