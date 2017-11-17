from shutil import copyfile

file = input('Archive name:')
y = int(input('Times to be copied:'))
ext = file[-4] + file[-3] + file[-2] + file[-1] # wont work in webm
z = y + 1

def copy(file):
        name = '%d' % (x)
        full = str(name) + ext
        copyfile(file,full)

for x in range(1, z):
    copy(file)

quit()
