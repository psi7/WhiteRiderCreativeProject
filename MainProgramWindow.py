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
Virus=['Human Papillomavirus (HPV)','Human Immunodeficiency Virus (HIV)','Human T-lymphotropic Virus 1 (HTLV-1)','Human T-lymphotropic Virus 2 (HTLV-2)']
functions=['Retrovirus Infection Simulation','Virus DNA Mutation','Virus Protein Transcription']
layout1 = [[sg.Text('Welcome to your Virus Simulation !!',size=(45,1),font=(16),background_color='white', text_color='black',justification='center',relief=sg.RELIEF_RAISED, enable_events=True)],
           *[[sg.Radio(f' {Virus[i]}', 1)] for i in range(len(Virus))]]

layout2 = [[sg.Text('Pick a virus simulation to Begin.')],
           *[[sg.Radio(f' {functions[i]}',2)] for i in range(len(functions))]]
layout3= [[sg.Text('Enter a new Virus to the Application:')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]



# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Button('Cycle Layout'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('Exit')]]

window = sg.Window('Virus Simulation Application', layout)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 1 if layout < 3 else 1
        window[f'-COL{layout}-'].update(visible=True)
    elif event in '123':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)
window.close()
