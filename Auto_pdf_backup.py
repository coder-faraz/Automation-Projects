import os, time
from datetime import datetime, timedelta

import shutil

# datetime.today() gives you today's date & timedelta(1) makes it tomorrows date
tom = datetime.today()+timedelta(1)

time.sleep(2)

# changes the path of the system to the path where directory is to be created
parent_dir = r"D:\DataBase\Last Day Backup MBD\2021\March 2021"

# joins the new path with the directory name with formatting
parent_dir_as_path_tom_as_name = os.path.join(parent_dir, tom.strftime("%d-%b"))

# if the folder with tomorrow's date is not created it will create it
if not os.path.exists(parent_dir_as_path_tom_as_name):
    os.makedirs(parent_dir_as_path_tom_as_name)

time.sleep(2)

src = r"Z:\WORKING\FINAL PDF"

dest = parent_dir_as_path_tom_as_name

# copies source directory to destination directory without creating new dirs
shutil.copytree(src, dest, dirs_exist_ok=True)
