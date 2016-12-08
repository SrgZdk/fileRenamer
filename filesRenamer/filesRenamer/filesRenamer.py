import os
os.chdir("C:\\Users\\szavodko.DEV\\Desktop\\renamer\\")
for filename in os.listdir("."):
    if not filename.endswith(".py"):
        os.rename(filename,"renamed_"+filename)