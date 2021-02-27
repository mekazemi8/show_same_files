import os

full_file_names = []
file_names = []
dir_list = []
tekrari = []


def get_list_content(path):
    global dir_con
    dir_con = os.listdir(path)
    return dir_con


def update_list(path):
    global file_names, dir_con, full_file_names, dir_list, tekrari

    c = len(dir_con)
    i = 0
    count = c
    while count != 0:
        full_name = path + '\\' + dir_con[i]
        diris = os.path.isdir(full_name)
        if diris:
            i += 1
            dir_list.append(full_name)
        else:
            for j in range(len(file_names)):
                if dir_con[i] == file_names[j]:
                    tuplee = (dir_con[i], full_name, full_file_names[j])
                    tekrari.append(tuplee)

            file_names.append(dir_con.pop(i))
            full_file_names.append(full_name)
            print('|____ ' + full_name + "\n\n")

        count -= 1


def run():
    global tekrari_list, index, ff, sf
    global p

    path = p.get()

    dir_count = 0
    dir_con = get_list_content(path)
    update_list(path)

    a = '''
    ____________________
    |
    |    FILES:       {}
    |    REPEATED:    {}
    |    DIRECTORIES: {}
    |___________________
    '''

    while dir_list != []:
        p = dir_list.pop(0)

        print(p)
        print(a.format(len(file_names), len(tekrari), dir_count))

        get_list_content(p)
        update_list(p)
        dir_count += 1

    # Don't need
    # for k in range(len(tekrari)):
    #     strr = '======\n' + tekrari[k][0] + '\n\t' + tekrari[k][1] + '\n\t' + tekrari[k][2] + '\n==='
    #     print(strr)

    clabel.configure(text='Files:    {}'.format(len(file_names)))
    rlabel.configure(text='Repeated: {}'.format(len(tekrari)))
    dlabel.configure(text='Dirs:     {}'.format(str(dir_count)))

    # Show List Box
    rep = Label(win, text="Repeated\nFiles", bg='#333', fg='#fff').grid(row=4, column=0)

    tekrari_list = Listbox(win, width=80, height=5 ,bg='#545454', fg='#fff')
    tekrari_list.bind('<<ListboxSelect>>',CurSelet)
    tekrari_list.grid(row=4, column=2)

    c = 0
    for i in tekrari:
        txt = str(c) +' *-* ' + i[0] + ' *-* ' + i[1] + ' *-* ' + i[2]
        tekrari_list.insert(END, txt)
        c += 1
    
    Label(win, text="File Name", bg='#333', fg='#fff').grid(row=5, column=0, pady=10)
    fn = Label(win, text=tekrari[index][0], bg='#333', fg='#fff')
    fn.grid(row=5, column=2)

    Label(win, text="First File", bg='#333', fg='#fff').grid(row=6, column=0)
    ff = Label(win, text=tekrari[index][1], bg='#333', fg='#3bdeff')
    ff.grid(row=6, column=2)

    Label(win, text="Second File", bg='#333', fg='#fff').grid(row=7, column=0)
    sf = Label(win, text=tekrari[index][2], bg='#333', fg='#ff3be5')
    sf.grid(row=7, column=2)

    rb1 = Button(win,text="RUN", bg="#3bdeff", fg='#333', width=10, command=run_first)
    rb1.grid(row=6, column=3)

    db1 = Button(win,text="DELETE", bg="#bf0013", fg='white', width=10, command=delete_first)
    db1.grid(row=6, column=4)

    rb2 = Button(win,text="RUN", bg="#ff3be5", fg='#333', width=10, command=run_second)
    rb2.grid(row=7, column=3, pady=5)

    db2 = Button(win,text="DELETE", bg="#bf0013", fg='white', width=10, command=delete_second)
    db2.grid(row=7, column=4)

    next = Button(win, text="Next", bg="#bf0013", fg='white', width=10, command=go_next).grid(row=8, column=3, pady=10)

    b = '''
    Name: 	{}
    First:  {}
    Second: {}
    --
    1. See FIRST file   2. See SECOND file
    3. DELETE First     4. DELETE Second
              5. DELETE BOTH
    6. Go Next          7. EXIT
    '''
    # import os

    # for item in tekrari:
    #     i = 0
    #     while i not in [3, 4, 5, 6]:
    #         print(b.format(item[0], item[1], item[2]))

    #         i = int(input('CHOOSE ONE: '))
    #         if i == 1:
    #             os.startfile(item[1])
    #         elif i == 2:
    #             os.startfile(item[2])
    #         elif i == 3:
    #             os.remove(item[1])
    #         elif i == 4:
    #             os.remove(item[2])
    #         elif i == 5:
    #             os.remove(item[1])
    #             os.remove(item[2])
    #         elif i == 6:
    #             break
    #         elif i == 7:
    #             exit()
def CurSelet(evt):
    global tekrari_list
    value=str(tekrari_list.get(tekrari_list.curselection()))
    print(value)

def run_first():
    global ff
    print(ff['text'])

def delete_first():
    pass

def run_second():
    pass

def delete_second():
    pass

def go_next():
    pass
#############################################
from tkinter import *
index = 0

win = Tk()
win.title("Find Duplicate Files | M.E_Kazemi")
win.geometry("800x500")
win.configure(background="#333333")

info = Label(win, text="This program shows you the same file names\nin a directory and you can decide for them", bg="#333", fg="#fff")
info.grid(row=0, column=2)

lpath = Label(win, text="Enter Path   ", bg="#333", fg="#fff")
lpath.grid(column=0, row=1)

p = StringVar()
path_entry = Entry(win, width=80, textvariable=p)
path_entry.grid(row=1, column=2)

run_button = Button(win, text="CHECK", bg="yellow", fg='#333', width=10, command=run)
run_button.grid(row=1, column=3, padx=3)

# show information Labels
clabel = Label(win, text="", bg='#333', fg='#fff', font="consolas")
clabel.grid(row=0, column=4)

rlabel = Label(win, text="", bg='#333', fg='#fff', font="consolas")
rlabel.grid(row=1, column=4)

dlabel = Label(win, text="", bg='#333', fg='#fff', font="consolas")
dlabel.grid(row=2, column=4)



win.mainloop()
exit()
#############################################