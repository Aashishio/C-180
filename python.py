from tkinter import *
from tkinter import ttk
from googletrans import Translator

translator = Translator()

root = Tk()
root.geometry('1000x600')
root.title('Language Translator')
root.config(background='black')

LANGUAGES = [
    'afrikaans','albanian','amharic','arabic','armenian','azerbaijani','basque','belarusian','bengali','bosnian','bulgarian','catalan','cebuano','chichewa','chinese (simplified)','chinese (traditional)','corsican','croatian','czech','danish','dutch','english','esperanto','estonian','filipino','finnish','french','frisian','galician','georgian','german','greek','gujarati','haitian creole','hausa','hawaiian','hebrew','hebrew','hindi','hmong','hungarian','icelandic','igbo','indonesian','irish','italian','japanese','javanese','kannada','kazakh','khmer','korean','kurdish (kurmanji)','kyrgyz','lao','latin','latvian','lithuanian','luxembourgish','macedonian','malagasy','malay','malayalam','maltese','maori','marathi','mongolian','myanmar (burmese)','nepali','norwegian','odia','pashto','persian','polish','portuguese','punjabi','romanian','russian','samoan','scots gaelic','serbian','sesotho',
    'shona','sindhi','sinhala','slovak','slovenian',
    'somali','spanish','sundanese',
    'swahili','swedish','tajik','tamil','telugu','thai','turkish','ukrainian','urdu','uyghur','uzbek','vietnamese','welsh','xhosa','yiddish','yoruba','zulu']

lbl_head = Label(root, text='Language Translator', font=('Helventica', 30, 'bold'), fg='white', bg='black')
lbl_head.place(relx=.5, rely=.2, anchor=CENTER)

lbl_ent = Label(root, text='Entry', fg='#FFF', bg='black', font=('Helventica', 18, 'bold'))
lbl_ent.place(relx=0.13, rely=.35, anchor=CENTER)

drp_ent = ttk.Combobox(root, values=LANGUAGES)
drp_ent.place(relx=.25, rely=.35, anchor=CENTER)

area = Text(root, height=10, width=20, font=('Courier', 14, 'bold'), bg='#fff', fg='#000')
area.place(relx=.1, rely=.6, anchor=W)

div = Label(root, text=':', font=('Arial', 40, 'bold'), bg='black', fg='#fff')
div.place(relx=.5, rely=.6, anchor=CENTER)

lbl_output = Label(root, text='Output', fg='#fff', bg='#000', font=('Helventica', 18, 'bold'))
lbl_output.place(relx=.73, rely=.35, anchor=CENTER)

drp_out = ttk.Combobox(root, values=LANGUAGES)
drp_out.place(relx=.85, rely=.35, anchor=CENTER)

area_out = Text(root, state='disabled', height=10, width=20, font=('Courier', 14, 'bold'))
area_out.place(relx=.7, rely=.6, anchor=W)

input_ent = translator.translate(area.get(), dest=drp_ent.get())
area.delete(0, END)
area.insert(END, input_ent)

def trans():
    output = translator.translate(area.get(), dest=drp_out.get())
    area_out.delete(0, END)
    area_out.insert(END, output)

btn = Button(root, text='Translate', font=('Arial', 18, 'bold'), fg='black', bg='white', command=trans)
btn.place(relx=.5, rely=.8, anchor=CENTER)

root.mainloop()