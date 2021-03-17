import os
import shutil
import subprocess
from tkinter import *
from tkinter import filedialog, simpledialog
from tkinter import messagebox as mb

import easygui

my_filetypes = [('all files', '.*'), ('text files', '.txt')]


def gui_manager_opener():
    read = easygui.fileopenbox()
    return read


def open_file():
    try:
        file_name = gui_manager_opener()
        if sys.platform == "win32":
            os.startfile(file_name)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            if opener and file_name:
                subprocess.call([opener, file_name])
    except:
        mb.showerror('Упс', "Файл не найден!")


def copy_file():
    started = gui_manager_opener()
    destination = filedialog.askdirectory()
    shutil.copy(started, destination)
    mb.showinfo('Успешно', "Файл скопирован !")


def delete_file():
    del_file = gui_manager_opener()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showerror('Упс', "Файл не найден !")


def rename_file():
    chosen_file = gui_manager_opener()
    cur_path = os.path.dirname(chosen_file)
    extension = os.path.splitext(chosen_file)[1]
    new_name = simpledialog.askstring("Input", "Введите новое название для файла: ",
                                      parent=root)
    if new_name:
        path = os.path.join(cur_path, new_name + extension)
        os.rename(chosen_file, path)
        mb.showinfo('Успешно', "Файл переименован !")
    else:
        mb.showerror('Упс', "Файл не переименован !")


def move_file():
    source = gui_manager_opener()
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showwarning('Упс', "Начальная и конченая папка равны")
    else:
        shutil.move(source, destination)
        mb.showinfo('Успешно', "Файл перемещен !")


def make_folder():
    new_folder_path = filedialog.askdirectory()
    new_folder = simpledialog.askstring("Input", "Введите название папки:: ",
                                        parent=root)
    if new_folder:
        path = os.path.join(new_folder_path, new_folder)
        os.mkdir(path)
        mb.showinfo('Успешно!', "Папка создана !")
    else:
        mb.showerror('Упс', "Папка не создана !")


def remove_folder():
    del_folder = filedialog.askdirectory()
    os.rmdir(del_folder)
    mb.showinfo('Успешно', "Папка удалена !")


def list_files():
    folder_list = filedialog.askdirectory()
    sort_list = sorted(os.listdir(folder_list))
    mb.showinfo('Содержимое папки', sort_list)


def exit_program():
    exit()


# GUI
root = Tk()
root.geometry("2300x650+400+500")
root.title('File Explorer')
root.config(background="white")

label_grid = Label(root,
                   text="Файловый менеджер titovilya",
                   font=("Helvetica", 16),
                   width=100,
                   height=4)
button_open = Button(root,
                     text="Открыть файл",
                     command=open_file)
button_copy = Button(root,
                     text="Скопировать файл",
                     command=copy_file)
button_del = Button(root,
                    text="Удалить файл",
                    command=delete_file)
button_rename = Button(root,
                       text="Переименовать файл",
                       command=rename_file)
button_move = Button(root,
                     text="Переместить файл",
                     command=move_file)
button_mk_fd = Button(root,
                      text="Создать папку",
                      command=make_folder)
button_rm_fd = Button(root,
                      text="Удалить папку",
                      command=remove_folder)
button_list = Button(root,
                     text="Вывести все содержимое директории",
                     command=list_files)
button_exit = Button(root,
                     text="Выход",
                     command=exit_program)
label_grid_end = Label(root,
                       text="ver 1.0",
                       font=("Helvetica", 7),
                       width=240,
                       height=5)


label_grid.grid(column=1, row=1)
button_open.grid(column=1, row=2)
button_copy.grid(column=1, row=3)
button_del.grid(column=1, row=4)
button_rename.grid(column=1, row=5)
button_move.grid(column=1, row=6)
button_mk_fd.grid(column=1, row=7)
button_rm_fd.grid(column=1, row=8)
button_list.grid(column=1, row=9)
button_exit.grid(column=1, row=10)
label_grid_end.grid(column=1, row=11)


root.mainloop()
