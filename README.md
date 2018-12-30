# select-photos-by-name
A script that selects photos from a folder by photo names
The idea of the script was created when selecting wedding photos for the album. The script copies or moves photos from the selected folder to a folder with a random name in the same place as the script location.
The script looks for files by the file names given in **IWantThisPicture.txt** (the file must be in the same path as the script by default). The file name is irrelevant, i.e. for the *Images1* and *iMaGeS1* or *Imag* names, the file will be searched for without distinction in case of the letter and will be found in part of the name.

## How run script
You can run the script without parameters:
```
py. \main.py
```

In this case, by default, the script accepts copying files from the directory in which the script is. Looks for raster graphics formats:
```'.jpeg', '.jps', '.jpg', '.jpeg 2000', '. djvu', '.tiff', '.png', '.gif', '.bmp', '.flif' , '.xcf', '.xpm', '.psd'```

To run a script that will move * *.bmp* files from the *photos* folder you can use:
```py .\main.py -m -p .\photos\ -e bmp```

You will receive the same result if you use:
```py .\main.py --move --path .\photos\ --extended bmp``` 
or
```py .\main.py --move -p .\photos\ -e bmp``` (mixed short and long form)

* -m responds --move
* -p responds --path
* -e matches --extends

The order of the argument does not matter, it means that the result will be the same if you use:
```py .\main.py --extended bmp --move --path .\photos\```
or:
```py .\main.py --extended bmp --path .\photos\ --move```
or:
```py .\main.py --path .\photos\ --move --extended bmp```
and so on.


You can only use part of the arguments, for example:
```py .\main.py -e png -m```
The folder path was not provided. By default, the script accepts the folder in which it is located and moves the files.

```py .\main.py -e png```
The folder path and the option of copying or moving files were not given. By default, the copy option is accepted, so ```-c``` or ```--copy``` is not mandatory.

py ```.\main.py -m```
Given only the transfer option, the script looks for files in the folder in which it is located after the raster image file extensions (given above).

After completing the process, script will open a folder with found photos. Example usage:

```
py .\main.py -m --path .\photos\ --extended bmp png
Search for file formats:
('bmp', 'png')

List of found files in directory .\photos\
['photo1.bmp', 'photo2.png', 'photo3.png', 'photo4.png']
The number of files found: 4

Files to search for:
['photo1', 'photo2', 'photo3', 'photo4']
List of found files with searched extensions:
['photo1.bmp', 'photo2.png', 'photo3.png', 'photo4.png']
The number of files found with searched extensions: 4

Found photo1.bmp
Found photo2.png
Found photo3.png
Found photo4.png

Found 4 from 4 (all files in directory)
Found: 4/4 files in directory '.\photos\' from text file
Move now photo1.bmp to selected_photos-XF1TSTZ5O
Move now photo2.png to selected_photos-XF1TSTZ5O
Move now photo3.png to selected_photos-XF1TSTZ5O
Move now photo4.png to selected_photos-XF1TSTZ5O
```
