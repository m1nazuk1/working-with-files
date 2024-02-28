import os
import shutil

print("Поиск в папке Test файлов, содержащих в названии введенное слово")
string = input("Введите слово: ")
path = '/Users/nizamialekperov/Desktop/Test'
res = []
for current_dir, dirs, files in os.walk(path):
    for i in files:
        if i.find(string) != -1:
            res.append(i)

with open("Task_1.txt", "w") as f:
    f.write('\n'.join(res))

print("Искомые файлы:")
print('\n'.join(res))

shutil.make_archive("Test", 'zip', path)
