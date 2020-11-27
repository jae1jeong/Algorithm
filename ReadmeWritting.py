import os
from pathlib import Path

filewrite = open("./files.txt","w")

# files =  os.listdir("./Programmers")
# for file in files:
#     f.write(f'+ {file[:-3]}\n')
# f.close()

list_path = ["./Programmers","./Baekjun"]

for file in list_path:
    if file == "./Baekjun":
        files = file.oslistdir(file)
        for fl in files:

            ispath = Path(fl).is_dir()
            if ispath:
                f = file.oslistdir(fl)
                for underdirfile in f:
                    if underdirfile[-3:] == ".py":
                        filewrite = 

                
            
    else:    
        f = file.oslistdir(file)
        f.write(f'+{file[:-3]}\n')