# -*- coding: utf-8 -*-
from customtkinter import *
from customtkinter import CTkLabel
from CTkMessagebox import CTkMessagebox
from random import choice
from dict import words4, words5, words6


'''
APPLICATION THEME
'''
set_appearance_mode('dark')  # for more details check customtkinter lib
set_default_color_theme('blue')
'''
APPLICATION THEME
'''


'''
GLOBALS
'''
count_row = 0
words = {
    4: words4,
    5: words5,
    6: words6
}
number_of_letters = 0
random_word = ''
'''
GLOBALS
'''


'''
FUNCTIONS
'''
def compare_words():
    global count_row
    count_row += 1
    word1 = word_tf.get().upper()
    global random_word
    word2 = random_word
    global number_of_letters
    if len(word1) != number_of_letters:
        CTkMessagebox(title='Ошибка', message=f'В слове должно быть {number_of_letters} букв')
        return
    word_tf.delete(0, END)
    word1 = [i for i in word1]
    word2 = [i for i in word2]
    indexes_green = []
    indexes_yellow = []
    res = ''
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            indexes_green.append(i)
        elif word1[i] in word2:
            indexes_yellow.append(i)
        res += word1[i]
    compare_window.configure(state=NORMAL)
    compare_window.tag_config('center', justify='center')
    compare_window.insert(END, f'{res}\n')
    compare_window.tag_add('center', 1.0, END)
    for i in range(len(indexes_green)):
        compare_window.tag_add('green', f'{count_row}.{indexes_green[i]}')
        compare_window.tag_config('green', foreground='green')
    for i in range(len(indexes_yellow)):
        compare_window.tag_add('yellow', f'{count_row}.{indexes_yellow[i]}')
        compare_window.tag_config('yellow', foreground='yellow')
    compare_window.configure(state=DISABLED)
    if word1 == word2:
        result_window.configure(text='Отлично! Вы отгадали слово!')
        return
    if count_row == 6:
        result_window.configure(text=f'Не получилось. Слово: {random_word}')
        compare_button.configure(state='disabled')


def try_again():
    compare_window.configure(state=NORMAL)
    compare_window.delete(1.0, END)
    compare_window.configure(state=DISABLED)
    result_window.configure(text='')
    global random_word
    random_word = choice(words[number_of_letters]).upper()
    global count_row
    count_row = 0
    compare_button.configure(state='normal')


def callback(*events):
    if text.get().isdigit() or text.get().isspace():
        if text.get().isdigit():
            CTkMessagebox(title='Ошибка', message='Нельзя вводить цифры')
        text.set(text.get()[:-1])
    global number_of_letters
    if len(text.get()) > number_of_letters:
        word_tf.delete(number_of_letters, END)
        CTkMessagebox(title='Ошибка', message=f'В слове должно быть {number_of_letters} букв')


def info():
    CTkMessagebox(title='Правила игры',
                  message='В игре вам нужно отгадать слово.\n(Легко -- 4 буквы; Нормально -- 5 букв; Сложно -- 6 букв)\nУ вас есть 6 попыток. Введите ваше слово в верхнее поле для ввода\nи нажмите кнопку "Сравнить".\nЕсли какая-то буква вашего слова стоит на том же месте, что и буква загаданного слова,\nто она будет выделена зеленым. Если буква стоит не на своем месте, но она присутствует в загаданном слове,\nто она будет выделена желтым.')


def set_easy():
    global number_of_letters
    number_of_letters = 4
    start_window.pack_forget()
    info_button.pack_forget()
    frame.pack(expand=True)
    info_button.pack(side=RIGHT)
    back_button.pack(side=LEFT)
    global random_word
    random_word = choice(words4).upper()
    try_again()


def set_normal():
    global number_of_letters
    number_of_letters = 5
    start_window.pack_forget()
    info_button.pack_forget()
    frame.pack(expand=True)
    info_button.pack(side=RIGHT)
    back_button.pack(side=LEFT)
    global random_word
    random_word = choice(words5).upper()
    try_again()


def set_hard():
    global number_of_letters
    number_of_letters = 6
    start_window.pack_forget()
    info_button.pack_forget()
    frame.pack(expand=True)
    info_button.pack(side=RIGHT)
    back_button.pack(side=LEFT)
    global random_word
    random_word = choice(words6).upper()
    try_again()


def back():
    frame.pack_forget()
    back_button.pack_forget()
    info_button.pack_forget()
    start_window.pack(expand=True)
    info_button.pack(anchor='se')
'''
FUNCTIONS
'''


'''
INITIALIZING THE APPLICATION WINDOW
'''
window = CTk()
window.title('WORDLY')
'''
INITIALIZING THE APPLICATION WINDOW
'''

'''
SETTINGS FOR BUTTONS, FIELDS AND WIDGETS
'''
start_window = CTkFrame(
    window,
    width=600,
    height=600
)
start_window.pack(expand=True)

difficulty_selection_label = CTkLabel(
    start_window,
    text='Выберите сложность',
)
difficulty_selection_label.grid(row=1, column=2)

easy_button = CTkButton(
    start_window,
    text='Легко',
    command=set_easy
)
easy_button.grid(row=3, column=1)

normal_button = CTkButton(
    start_window,
    text='Нормально',
    command=set_normal
)
normal_button.grid(row=3, column=2)

hard_button = CTkButton(
    start_window,
    text='Сложно',
    command=set_hard
)
hard_button.grid(row=3, column=3)

frame = CTkFrame(
    window,
    width=600,
    height=600
)

word_lb = CTkLabel(
    frame,
    text='Введите слово',
)
word_lb.grid(row=1, column=3)

compare_window = CTkTextbox(
    frame,
    width=400,
    height=400,
    state=DISABLED,
    font=('Verdana', 40, 'bold'),
)
compare_window.grid(row=5, column=3)

result_window = CTkLabel(
    frame,
    text='',
)
result_window.grid(row=6, column=3)

text = StringVar()
text.trace('w', callback)
word_tf = CTkEntry(
    frame,
    textvariable=text,
    border_color='blue'
)
word_tf.grid(row=2, column=3)

compare_button = CTkButton(
    frame,
    text='Сравнить',
    command=compare_words,
)
compare_button.grid(row=7, column=3)

try_again_button = CTkButton(
    frame,
    text='Попробовать заново',
    command=try_again,
)
try_again_button.grid(row=8, column=3)

info_button = CTkButton(
    window,
    text='info',
    command=info
)
info_button.pack(anchor='se')

back_button = CTkButton(
    window,
    text='Назад',
    command=back
)
'''
SETTINGS FOR BUTTONS, FIELDS AND WIDGETS
'''


window.geometry('600x600')
window.mainloop()
