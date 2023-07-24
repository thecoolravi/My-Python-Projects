
                    # RULES

# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]

# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry





                    # CODE

# For Mac ( this only works for mac, for windows we need to use win32 API)
from os import system
names = ["Ravi","Rahul", "Nishant", "Harry"]
for name in names:
  system(f'say Shoutout to {name}') # SAY speaks the content instead of printing them like print statement BUT IT SAY IS ONLY FOR MAC


# FOR WINDOWS just google on how to use win32 API