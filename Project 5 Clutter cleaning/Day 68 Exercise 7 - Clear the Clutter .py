# Exercise 7 - Clear the Clutter

# Rules:
# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png




import os

files = os.listdir("Project 4 Clutter cleaning")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"Project 4 Clutter cleaning/{file}", f"Project 4 Clutter cleaning/{i}.png")
    i = i + 1






# renaming a png/or any file
# os.rename("images.png","renamed.png")