from customtkinter import *
from customtkinter import CTkLabel
from CTkMessagebox import CTkMessagebox
from random import choice
from dict import words

set_appearance_mode('dark')
set_default_color_theme('blue')

count_row = 0
random_word = choice(words).upper()


def compare_words():
    global count_row
    count_row += 1
    word1 = word_tf.get()
    word_tf.delete(0, END)
    global random_word
    word2 = random_word
    if len(word1) != 5:
        CTkMessagebox(title='Ошибка', message='В слове должно быть 5 букв')
        return
    else:
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
    random_word = choice(words).upper()
    global count_row
    count_row = 0
    compare_button.configure(state='normal')


def callback(*events):
    if not text.get().isupper() or text.get().isdigit() or text.get().isspace():
        if text.get().isdigit():
            CTkMessagebox(title='Ошибка', message='Нельзя вводить цифры')
        text.set(text.get()[:-1])


def info():
    CTkMessagebox(title='Правила игры',
                  message='В игре вам нужно отгадать слово.\nУ вас есть 6 попыток. Введите ваше слово в верхнее поле для ввода\nи нажмите кнопку "Сравнить".\nЕсли какая-то буква вашего слова стоит на том же месте, что и буква загаданного слова,\nто она будет выделена зеленым. Если буква стоит не на своем месте, но она присутствует в загаданном слове,\nто она будет выделена желтым.')


window = CTk()
window.title('WORDLY')
text = StringVar()
text.trace('w', callback)

frame = CTkFrame(
    window,
    width=600,
    height=600
)
frame.pack(expand=True)

word_lb = CTkLabel(
    frame,
    text='Введите слово (поддерживается только CAPS)',
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

word_tf = CTkEntry(
    frame,
    textvariable=text,
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
info_button.pack(anchor='nw')

window.geometry('600x600')
window.mainloop()
