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

#Get Vitis Version
XILINX_VITIS = os.environ.get("XILINX_VITIS")
XILINX_VITIS = XILINX_VITIS.split("/")
Vitis_Version = XILINX_VITIS[len(XILINX_VITIS)-2]

app_path= os.getcwd()

client = vitis.create_client()
client.set_workspace(path=workspace)

#Get DSP Library path
DSPLIB = os.environ.get("DSPLIB_ROOT")
if (DSPLIB == None):
    print("DSPLIB_ROOT environment not set. Please download the Vitis_Libraries repository and point to the dsp folder \n")
    print("https://github.com/Xilinx/Vitis_Libraries\n")
    sys.exit()
else:
    print("Using DSPLIB from DSPLIB_ROOT environment variable\n")

# Create AIE-ML component
print("\n-----------------------------------------------------")
print("Creating AIE-ML empty component\n")
comp = client.create_aie_component(name="fft_1024", part = part, template = "empty_aie_component")
comp = client.get_component(name="fft_1024")
print("Importing AIE-ML source files\n")
status = comp.import_files(from_loc=app_path+"/aie/src/14/", files=["graph_FFT_1024.h","graph_FFT_1024.cpp"], dest_dir_in_cmp = "src")

# Set top level file
status = comp.update_top_level_file(top_level_file=app_path+"/"+workspace+"/fft_1024/src/graph_FFT_1024.cpp")

# Edit AIE-ML component configuration to add DSP Lib in include directories
print("Adding DSP Lib to Include Directories\n")
cfg = client.get_config_file(app_path+'/'+workspace+'/fft_1024/aiecompiler.cfg')
cfg.add_values(key='include', values=[DSPLIB+"/L2/include/aie",DSPLIB+"/L1/include/aie", DSPLIB+"/L1/src/aie"])

print("Building AIE-ML component\n")
comp.build(target="hw")
    
vitis.dispose()
