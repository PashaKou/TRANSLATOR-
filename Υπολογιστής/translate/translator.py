from translate import Translator
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from translator_dict import language_dict

"""
This is a simple translator in python made in GUI
I hope it helps!
"""


def translate_f():
    try:
        given_text = entry_for_translate.get()  # get the text for translate
        written_text_lang = from_combobox.get().lower()  # get the language of the written text
        to_translate_lang = to_combobox.get().lower()  # get the language to translate
        translator = Translator(provider="mymemory", from_lang=language_dict[written_text_lang],
                                to_lang=language_dict[to_translate_lang])
        translation = translator.translate(given_text)
        var_translate.set(translation)
    except Exception as e:
        messagebox.showerror(title="ERROR", message=f"Oops something went wrong!\nFor the programmer:{e}"
                                                    f"\nplease check your inputs!")


# window init ---------------------------------------------------------------
root = Tk()
root.title("Personal Translator In GUI 🔠")
root.geometry("570x500")
root.config(background="light yellow")
root.resizable(False, False)
# Label for introduction ----------------------------------------------------
Label(root, pady=10, text="My Translator", font=("Ink free", 30), bg="light yellow",
      fg="purple").pack()
# start the design -----------------------------------------------------------
entry_for_translate = CTkEntry(root, font=("Cambria", 30),  # entry for the translation
                               fg_color="black", width=480,
                               placeholder_text="For translation..",
                               corner_radius=100, border_color="black")

entry_for_translate.place(x=40, y=90)  # place it in the root

Label(root, text="My given text is currently written in", font=("Cambria", 12), bg="light yellow").place(x=50, y=160)

from_combobox = CTkComboBox(root, values=[key.title() for key in language_dict.keys()], corner_radius=15)
from_combobox.place(x=310, y=160)
# ------------------------------------------------------------------------------------
"""
START CODING THE TRANSLATED PART DESIGN
"""
var_translate = StringVar()
entry_translated = CTkEntry(root, font=("Cambria", 30),
                            textvariable=var_translate,
                            fg_color="black", width=480,
                            corner_radius=100, border_color="black")

entry_translated.place(x=40, y=290)  # place it in the root

Label(root, text="and I want it to be translated above into", font=("Cambria", 12),
      bg="light yellow").place(x=50, y=360)

to_combobox = CTkComboBox(root, values=[key.title() for key in language_dict.keys()], corner_radius=15)
to_combobox.place(x=340, y=360)
# button for the translation command ------------------------------------------------------
button = CTkButton(root, text="Translate", corner_radius=20, fg_color="purple", command=translate_f)
button.place(x=200, y=420)
# root mainloop --------------------------------------------------------------
root.mainloop()