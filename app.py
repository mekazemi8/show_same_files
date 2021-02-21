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
            print('|____ ' + full_name, end="\n\n")

        count -= 1


dir_count = 0
path = os.getcwd()
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

# print(tekrari)
for k in range(len(tekrari)):
    strr = '======\n' + tekrari[k][0] + '\n\t' + tekrari[k][1] + '\n\t' + tekrari[k][2] + '\n==='
    print(strr)

print('COUNT OF FILES:            ' + str(len(file_names)))
print('|---> OF REPEATED FILES:   ' + str(len(tekrari)))
print('|---> OF DIRECTORIES:      ' + str(dir_count))

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
import os

for item in tekrari:
	i = 0
	while i not in [3, 4, 5, 6]:
		print(b.format(item[0], item[1], item[2]))

		i = int(input('CHOOSE ONE: '))
		if i == 1:
			os.startfile(item[1])
		elif i == 2:
			os.startfile(item[2])
		elif i == 3:
			os.remove(item[1])
		elif i == 4:
			os.remove(item[2])
		elif i == 5:
			os.remove(item[1])
			os.remove(item[2])
		elif i == 6:
			break
		elif i == 7:
			exit()