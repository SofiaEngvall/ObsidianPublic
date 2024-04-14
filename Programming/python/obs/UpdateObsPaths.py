import os
import json
from tkinter import filedialog

# Put your OBS directory here:
obs_directory = "C:\\VIDEO\\obs-studio"

portable = False
for file_name in os.listdir(obs_directory):
    if "portable" in file_name and "mode" in file_name:
        portable = True

if portable:
    scenes_config_path = "config\\obs-studio\\basic\\scenes"
    dir_path = os.path.join(obs_directory, scenes_config_path)
else:
    scenes_config_path = "obs-studio\\basic\\scenes"
    app_data = os.getenv('APPDATA')
    dir_path = os.path.join(app_data, scenes_config_path)

if os.path.exists(dir_path):
    for file_name in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_name)):
            if not ".bak" in file_name:
                print(file_name)
                with open(os.path.join(dir_path, file_name), "r+") as file:
                    data = json.load(file)
                    file_path = ""

                    for item in data["modules"]["scripts-tool"]:
                        if not os.path.exists(item['path']):
                            print(f"    Path needs to be updated:")
                            print(f"        Old file path: {item['path']}")

                            if file_path == "":
                                file_path = filedialog.askdirectory()

                            new_file_name = file_path + "/" + \
                                os.path.basename(item['path'])

                            print(f"        New file path: {new_file_name}")

                            if os.path.isfile(new_file_name):
                                print("            File exists for new file path")
                                item['path'] = new_file_name
                            else:
                                print(
                                    "            The script can't be found in your selected directory!")

                    file.seek(0)
                    json.dump(data, file)
                    print("Json saved to file.")
