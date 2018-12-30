import os, shutil, string, random, argparse

def generate(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

COPY_FILES = True
dir = '.'

parser = argparse.ArgumentParser(description='Input parameters for action')
parser.add_argument("-m", "--move", action = "store_true", help = 'Use -m to move files (not copy)')
parser.add_argument('-c', '--copy', action = 'store_true', help = 'Use -c to copy file (not move)')
parser.add_argument('-e', '--extended', nargs = '*', help = 'Enter file extensions')
parser.add_argument('-p', '--path', nargs = '*', help = 'Input path with files')
args = parser.parse_args()

if args.move:
    COPY_FILES = False

formats = set()
if args.extended:
    for item in args.extended:
        formats.add(item)
else:
    formats = ('.jpeg', '.jps', '.jpg', '.jpeg 2000', '.djvu', '.tiff', '.png', '.gif', '.bmp', '.flif', '.xcf', '.xpm', '.psd')

if args.path:
    dir = args.path[0]

formatsFilesTuple = tuple(formats)
print('Search for file formats: ')
print(formatsFilesTuple)

content = os.listdir(dir)
print('\nList of found files in directory {}'.format(dir))
print(content)
print('The number of files found: {}'.format(len(content)))

with open('IWantThisPicture.txt', 'r') as source:
    files = source.read().lower().split()

print('\nFiles to search for: ')
print(files)

list_of_files = [i for i in (filename.lower() for filename in content) if (os.path.isfile(i) and i.endswith(formatsFilesTuple))]
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

print('\nFound {} from {} (all files in directory)'.format(counter_of_searches, len(list_of_files)))
print('Found: {}/{} files in directory \'{}\' from text file'.format(counter_of_searches, len(files), dir))

SELECTED_PHOTOS = 'selected_photos-' + generate()
try:
    os.makedirs(SELECTED_PHOTOS)
except:
    print('An error with the action of creating a folder')

for file in list_of_files_with_found_files_by_name:  
    if COPY_FILES == True or COPY_FILES == 'True':
        print('Copy now ' + file + " to " + SELECTED_PHOTOS)  
        shutil.copy(os.path.join(dir, file), os.path.join(SELECTED_PHOTOS, file))
    else:
        print('Move now ' + file + " to " + SELECTED_PHOTOS)  
        shutil.move(os.path.join(dir, file), os.path.join(SELECTED_PHOTOS, file))

os.startfile(SELECTED_PHOTOS)

del dir
del COPY_FILES