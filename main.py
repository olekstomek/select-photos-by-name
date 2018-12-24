import os, shutil, string, random

MOVE_FILES = False

def generate(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

dir = '.'
formats = ('.jpeg', '.jps', '.jpg', '.jpeg 2000', '.djvu', '.tiff', '.png', '.gif', '.bmp', '.flif', '.xcf', '.xpm', '.psd')
print('Search for file formats: ')
print(formats)

content = os.listdir(dir)
print('\nList of found files in directory with script: ')
print(content)
print('The number of files found: {}'.format(len(content)))

with open('IWantThisPicture.txt', 'r') as source:
    files = source.read().split()

print('\nFiles to search for: ')
print(files)

list_of_files = [i for i in (filename.lower() for filename in content) if (os.path.isfile(i) and i.endswith(formats))]
print('List of found files with searched extensions: ')
print(list_of_files)
print('The number of files found with searched extensions: {}\n'.format(len(list_of_files)))

list_of_files_with_found_files_by_name = []
counter_of_searches = 0
for item in list_of_files:
    for item2 in files:
        if item2 in item:
            print('Found ' + item)
            list_of_files_with_found_files_by_name.append(item)
            counter_of_searches += 1
        else:
            continue

print('\nCopy {} from {} (all files in directory)'.format(counter_of_searches, len(list_of_files)))
print('Found: {}/{} files in directory from text file'.format(counter_of_searches, len(files)))

SELECTED_PHOTOS = 'selected_photos-' + generate()
try:
    os.makedirs(SELECTED_PHOTOS)
except:
    print('An error with the action of creating a folder')

for file in list_of_files_with_found_files_by_name:  
    if MOVE_FILES:
        print('Move now ' + file + " to " + SELECTED_PHOTOS)  
        shutil.move(os.path.join(dir, file), os.path.join(SELECTED_PHOTOS, file))
    else:
        print('Copy now ' + file + " to " + SELECTED_PHOTOS)  
        shutil.copy(os.path.join(dir, file), os.path.join(SELECTED_PHOTOS, file))

os.startfile(SELECTED_PHOTOS)