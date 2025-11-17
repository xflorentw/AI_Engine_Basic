#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#
# ------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------
import os
import sys
import numpy as np

cmd_args=len(sys.argv)
if cmd_args>1:
    target=sys.argv[1]
else:
    target = "hw"

# ------------------------------------------------------------
#Parameters
# ------------------------------------------------------------
Iterations = 1
N_Taps = 1024

if(target=="x86sim"):
    aiesim_out = "../workspace/fft_1024/build/x86sim/x86simulator_output/data/output.txt"
else:
    aiesim_out = "../workspace/fft_1024/build/hw/aiesimulator_output/data/output.txt"
    
golden_fft = "../aie/data/output_ref.txt"

if not os.path.exists(aiesim_out):
    print(f"The file '{aiesim_out}' does not exist.\n")
    print(f"Please run the AI Engine simulator and run the script again")
    sys.exit()

if not os.path.exists(golden_fft):
    print(f"The file '{golden_fft}' does not exist.\n")
    print(f"Please run fft_gen.py and run the script again")
    sys.exit()
    
# ------------------------------------------------------------
# Load and compare the data
# ------------------------------------------------------------
i = 0
aie_data = np.zeros(N_Taps * Iterations, dtype=int)
with open(aiesim_out) as f:
    for x in f:
        if(x[0]!='T'):
            x = x.split(' ')
            aie_data[i:i+3] = x[0]
            i +=4

i = 0
python_data = np.zeros(N_Taps * Iterations, dtype=int)
with open(golden_fft) as f:
    for x in f:
        x = x.split(' ')
        python_data[i:i+3] = x[0]
        i +=4

error_threshold = 1;
error = 0

for i in range(0, aie_data.size):
    if aie_data[i] != python_data[i]:
        if(abs(aie_data[i] - python_data[i])> error_threshold):
            print('Error in sample %d', (i+1))
            print('Golden:') 
            print(python_data[i])
            print('AIE ouput = ')
            print(aie_data[i])
            error += 1

if (error<1):
    print('AI Engine FFT matches the Python FFT within 1 LSB')
else:
    print('Test Failed')
    print('Nb errors : %d' % (error))