#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#

import vitis
import sys
import os


part=sys.argv[1]
version=int(sys.argv[2])
workspace="workspace"

app_path= os.getcwd()

client = vitis.create_client()
client.set_workspace(path=workspace)

# Create AIE-ML component
print ("\n-----------------------------------------------------")
print ("Creating AIE-ML component from Simple template\n")
comp = client.create_aie_component(name="aie-ml_component_simple", part = part, template = "installed_aie_examples/simple")
comp = client.get_component(name="aie-ml_component_simple")

if version == 2:
    os.remove(app_path+"/"+workspace+"/aie-ml_component_simple/src/project.h")
    status = comp.import_files(from_loc=app_path+"/src/10/", files=["project.h"], dest_dir_in_cmp = "src")
    status = comp.import_files(from_loc=app_path+"/src/10/", files=["input_64.txt"], dest_dir_in_cmp = "data")



vitis.dispose()