import os
# get the full list of filenames
res = []
for dir_path, dir_names, file_names in os.walk(os.getcwd()):
    print(dir_path, dir_names, file_names)
    res.extend(file_names)

# work on those starting with 'j'
for file in res:
    if "j" in file.split('_')[0]:
        ext = file.split('.')[1:]
        if len(ext) > 1: # if the extension is '.md.py'                    
            pre = file.split('.')[0]
        elif ext[-1] == 'py': # if the extension is '.py'
            pre = file.split('.')[0]
        else:
            continue
        os.rename(file, pre + '.md')

# check if renaming completed. 
res = []
for dir_path, dir_names, file_names in os.walk(os.getcwd()):
    print(dir_path, dir_names, file_names)
    res.extend(file_names)

for file in res:
    print(file)    
        
