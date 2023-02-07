import os
import sys

# Link to the folder that you want to rename
folder = r'' + sys.argv[1] + '//'

# Count increase by 1 in each iteration
count = int(sys.argv[2])

# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder +  str(count) + ".jpg"
    # if you have the trouble duplicate name
    # please change detination = folder +  str(count) + "xxx.jpg"
    # and start again

    # Renaming the file
    os.rename(source, destination)
    count += 1

print('All Files Renamed')
print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)

