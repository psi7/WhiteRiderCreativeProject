import PySimpleGUI as sg
# import PySimpleGUIQt as sg

"""
    Demo - Multiple layouts in a single window that are swapped in and out

    If you've ever wanted to replace the contents of a window with another layout then perhaps
    this demo is for you.  You cannot actually change the layout of a window dynamically, but what
    you can do is make elements visible and invisible.  
    
    To "swap out" a portion of a window, use a Column element for that portion.  Add multiple Columns
    on the same row and make only 1 of them active at a time
"""

# ----------- Create the 3 layouts this Window will display -----------
Virus = ['Human Papillomavirus (HPV)', 'Human Immunodeficiency Virus (HIV)',
         'Human T-lymphotropic Virus 1 (HTLV-1)', 'Human T-lymphotropic Virus 2 (HTLV-2)']
functions = ['Retrovirus Infection Simulation',
             'Virus DNA Mutation', 'Virus Protein Transcription']
# Theme Color for the Gui Application
sg.theme('Dark')
layout1 = [[sg.Text('Welcome to Virus Simulation App!!', size=(45, 1), font=(16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           *[[sg.Radio(f' {Virus[i]}', 1)] for i in range(len(Virus))]]

layout2 = [[sg.Text('Pick a virus simulation form the list to Begin.', size=(45, 1), font=(16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           *[[sg.Radio(f' {functions[i]}', 2)] for i in range(len(functions))]]

layout3 = [[sg.Text('Enter a new Virus Data to the Application:', size=(45, 1), font=(16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           [sg.Input(key='-IN-'), sg.Button('Submit', key='-SubmitVName-')],
           [sg.Text('Enter a new Virus Mutation Rate to the Application:', size=(45, 1), font=(
               16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           [sg.Input(key='-IN2-'), sg.Button('Submit', key='-SubmitVMR-')]]


# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Submit('Choose Virus', key='-MainButton-'), sg.Button('1', auto_size_button=True), sg.Button('2', auto_size_button=True), sg.Button('3', auto_size_button=True), sg.Button('Exit', auto_size_button=True)]]

window = sg.Window('Virus Simulation Application', layout)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-MainButton-':
        window[f'-COL{1}-'].update(visible=False)
        if layout == 1:
            layout += 1
            window[f'-COL{layout}-'].update(visible=True)
            window['-MainButton-'].update('Begin Simulation')
        elif layout == 2:
            layout = 1
            window[f'-COL{layout+1}-'].update(visible=False)
            window[f'-COL{layout}-'].update(visible=True)
            window['-MainButton-'].update('Choose Virus')
    elif event in '123':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
        if layout == 3:
            window['-MainButton-'].update(visible=False)
        else:
            if event in '1':
                window['-MainButton-'].update('Choose Virus',
                                              visible=True)
            elif event in '2':
                window['-MainButton-'].update('Begin Simulation',
                                              visible=True)


window.close()
