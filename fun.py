import PySimpleGUI as sg
text = sg.popup('i am dave an artificial intelligence')
text2 = sg.popup_get_text('what do you like to do')
text3 = sg.popup('well i can help with that')
if sg.popup_yes_no('do you want my help') == 'Yes':
    sg.popup('sorry i cant help you with that')
else:
    sg.popup('well leave')
    if sg.popup_yes_no('do you want to leave') == 'Yes':
        exit()
    else:
        sg.popup('well you have to leave')
        sg.popup('leave now')
        sg.popup('i said leave')
        sg.popup('leave now or i will leave you')
        if sg.popup_yes_no('leave now') == 'Yes':
            exit()  
        else:
            sg.popup('bye')
            exit()