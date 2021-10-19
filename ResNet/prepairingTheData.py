import os
import shutil
import re

base_dir = "PetImages/"

# Create training folder
files = os.listdir(base_dir)

# Moves all training cat images to cats folder, training dog images to dogs folder
def train_maker(name):
  train_dir = f"{base_dir}/train/{name}"
  for f in files:
        search_object = re.search(name, f)
        if search_object:
          shutil.move(f'{base_dir}/{name}', train_dir)

train_maker("Cat")
train_maker("Dog")

# Make the validation directories
try:
    os.makedirs("val/Cat")
    os.makedirs("val/Dog")
except OSError:
    print ("Creation of the directory %s failed")
else:
    print ("Successfully created the directory %s ")

# Create validation folder

cat_train = base_dir + "train/Cat/"
cat_val = base_dir + "val/Cat/"
dog_train = base_dir + "train/Dog/"
dog_val = base_dir + "val/Dog/"

try:
    os.makedirs(cat_train)
except Exception as e:
    print(e)

try:
    os.makedirs(cat_val)
except Exception as e:
    print(e)

try:
    os.makedirs(dog_train)
except Exception as e:
    print(e)

try:
    os.makedirs(dog_val)
except Exception as e:
    print(e)

cat_files = os.listdir(cat_train)
dog_files = os.listdir(dog_train)

print(os.listdir("PetImages/train/"))
print(dog_files)

# This will put 1000 images from the two training folders
# into their respective validation folders

print("c")
for f in cat_files:
    print("a")
    validationCatsSearchObj = re.search("5\d\d\d", f)
    if validationCatsSearchObj:
        print("b")
        shutil.move(f'{cat_train}/{f}', cat_val)

for f in dog_files:
    validationCatsSearchObj = re.search("5\d\d\d", f)
    if validationCatsSearchObj:
        shutil.move(f'{dog_train}/{f}', dog_val)