
import os
import random
import string

from secrets import details

class Sorterizer:

    def __init__(self, sorter):


        self.folder_path = sorter


        list_files = os.listdir(self.folder_path)

        random_names = [''.join(random.choices(string.ascii_lowercase, k=3)) for _ in list_files]
        # creates a random 3 letter string for each file in the folder

        counter = 1

        for file, random_name in zip(sorted(list_files), random_names):

            file_path = os.path.join(self.folder_path, file)

            random_name = f"{random_name}{os.path.splitext(file)[1]}"
            print(random_name)

        # file is first renamed something random so that the file isnt given
        # the same name twice which can lead to the file being corrupted and deleted

            os.rename(file_path, os.path.join(self.folder_path, random_name))

        list_files2 = os.listdir(self.folder_path)
        # relist the files after they have been renamed

        for file2 in sorted(list_files2):

            filepath2 = os.path.join(self.folder_path, file2)

            new_name = f"{counter}{os.path.splitext(file2)[1]}"

            os.rename(filepath2, os.path.join(self.folder_path, new_name))

            print(new_name)

            counter += 1

tha_boat = Sorterizer(details()[4])

