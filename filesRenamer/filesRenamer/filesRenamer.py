import os
for filename in os.listdir("."):
    if not filename.endswith(".py"):
        os.rename(filename,"renamed_"+filename)