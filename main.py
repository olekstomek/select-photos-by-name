import shutil, os, string, random

def generate(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

SELECTED_PHOTOS = 'selected_photos-' + generate()
root = r'%s' % os.getcwd().replace('\\','/')
print(root)

with open('IWantThisPicture.txt', 'r') as source:
    files = source.read().split()
source.close()

try:
    os.makedirs(SELECTED_PHOTOS)
except:
    print('An error with the action of creating a folder')

for f in files:
    path = root + '/' + f
    print('Selected file: ' + path)
    shutil.copy(f + '.PNG', SELECTED_PHOTOS)
