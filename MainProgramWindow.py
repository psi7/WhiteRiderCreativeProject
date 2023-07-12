import PySimpleGUI as sg
import simulations

# ----------- Create the 3 layouts this Window will display -----------
icon = './media/virusapp.ico'
Virus = ['Human Papillomavirus (HPV)', 'Human Immunodeficiency Virus (HIV)',
         'Human T-lymphotropic Virus 1 (HTLV-1)', 'Human T-lymphotropic Virus 2 (HTLV-2)']
functions = ['Retrovirus Infection Simulation',
             'Virus DNA Mutation', 'Virus Protein Transcription']
ifile = "media\HPVDNA.fasta"  # Initialize the input file path
# Theme Color for the Gui Application
sg.theme('Dark')
layout1 = [[sg.Text('Welcome to Virus Simulation App!!', size=(45, 1), font=(16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           *[[sg.Radio(f' {Virus[i]}', 1, key=f'-VirusB{i+1}-', auto_size_text=True)] for i in range(len(Virus))]]

layout2 = [[sg.Text('Pick a virus simulation form the list to Begin.', size=(45, 1), font=(16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           *[[sg.Radio(f' {functions[i]}', 2, key=f'-Sim{i+1}-', auto_size_text=True)] for i in range(len(functions))]]

layout3 = [[sg.Text('Enter a new Virus Data to the Application:', size=(45, 1), font=(16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           [sg.Input(key='-IN-'), sg.Button('Submit', key='-SubmitVName-')],
           [sg.Text('Enter a new Virus Mutation Rate to the Application:', size=(45, 1), font=(
               16), background_color='white', text_color='black', justification='center', relief=sg.RELIEF_RAISED, enable_events=True)],
           [sg.Input(key='-IN2-'), sg.Button('Submit', key='-SubmitVMR-')]]


# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')],
          [sg.Submit('Choose Virus', key='-MainButton-'), sg.Button('1', auto_size_button=True), sg.Button('2', auto_size_button=True), sg.Button('3', auto_size_button=True), sg.Button('Exit', auto_size_button=True)]]

window = sg.Window('Virus Simulation Application', layout, element_justification='center', element_padding=(5, 5), resizable=True, default_element_size=(
    40, 5), icon=icon,finalize=True)

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
            if values['-Sim1-']:
                Soption = functions[0]
            elif values['-Sim2-']:
                Soption = functions[1]
            elif values['-Sim3-']:
                Soption = functions[2]
            print(Soption)
            if Soption == functions[1] and event == '-MainButton-':
                    simulations.mutation()
            if Soption == functions[2] and event == '-MainButton-':
                if option == Virus[0]:
                    simulations.Mtranslate(ifile="media\HPVDNA.fasta")
                elif option == Virus[1]:
                    simulations.Mtranslate(ifile="media\HIVDNA.fasta")
                elif option == Virus[2]:
                    simulations.Mtranslate(ifile="media\HTLV1DNA.fasta")
                elif option == Virus[3]:
                    simulations.Mtranslate(ifile="media\HTLV2DNA.fasta")
                else:
                    print("ERROR: Something unexpected happened!!")
        if values['-VirusB1-']:
            option = Virus[0]
        elif values['-VirusB2-']:
            option = Virus[1]
        elif values['-VirusB3-']:
            option = Virus[2]
        elif values['-VirusB4-']:
            option = Virus[3]
        print(option)
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
