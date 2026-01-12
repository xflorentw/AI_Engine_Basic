#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#
# ------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------
import os
import vfs
import numpy as np
from fxpmath import Fxp
import varray
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt


# Initialize the AIE graph
myaiefft = vfs.aieGraph(vfs_build_dir = "./vfs/")

# ------------------------------------------------------------
# Generate Simulus I/O
# ------------------------------------------------------------
#Parameters
Iterations = 1
Input_shift = 15;
N_Taps = 1024
F1_MHz = 50
F2_MHz = 150
Fs_MHz = 400

# Number of sample points
N_Samp = N_Taps * Iterations
# sample spacing
T = 1.0 / Fs_MHz
A1 = 0.2
A2 = 0.4;

# Generate Input Signal
x = np.linspace(0.0, N_Samp*T, N_Samp, endpoint=False)
tone1 = A1 * np.exp( 1.j * 2.0*np.pi*F1_MHz*x)
tone2 = A2 * np.exp( 1.j * 2.0*np.pi*F2_MHz*x)
sig_i = tone1 + tone2;

sig_i_cplx = Fxp(sig_i, dtype='S1.15')
sig_i_cplx = sig_i_cplx.astype(complex)

# ------------------------------------------------------------
# FFT
# ------------------------------------------------------------
# Set outputs
python_data = np.zeros(N_Taps * Iterations, dtype=complex)
aie_data = np.zeros(N_Taps * Iterations, dtype=complex)

# Process each frame with AI Engine X86 Simulation and Python
for i in range(0, Iterations):
    input_data = sig_i_cplx[i*1024:(i+1)*1024]

    # Run AIE graph processing
    y_aie = myaiefft.run(varray.array(input_data*2**Input_shift, varray.cint16))
    aie_data[i*1024:(i+1)*1024] = np.array(y_aie)
    
    # Run Pyton FFT
    python_data[i*1024:(i+1)*1024] = fft(input_data)

# ------------------------------------------------------------
# Error Check AIE vs Golden
# ------------------------------------------------------------
error_threshold = 1/2**4
error = 0

python_data = Fxp(python_data, dtype='S10.6')
aie_data = Fxp(aie_data/2**5, dtype='S10.6')

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
    print('AI Engine FFT matches the Python FFT within 2 LSB')
else:
    print('Test Failed')
    print('Nb errors : %d' % (error))

# ------------------------------------------------------------
# Plot signals
# ------------------------------------------------------------
xf = fftfreq(N_Taps, T)
xf = fftshift(xf)   
yplot = fftshift(python_data[0:N_Taps].astype(complex))
yplot_aie = fftshift(aie_data[0:N_Taps].astype(complex))
    

fig, (ax1, ax2,ax3) = plt.subplots(3, 1)
fig.suptitle('Input / Output signals')
ax1.plot(x, sig_i.real)
ax1.set_xlabel('Sample Index')
ax1.set_ylabel('Real part')
ax1.set_title('Input signal')
ax2.plot(xf, np.absolute(yplot))
ax2.set_xlabel('Frequency (MHz)')
ax2.set_ylabel('Magnitude')
ax2.set_title('Output FFT (Python)')
ax3.plot(xf, np.absolute(yplot_aie))
ax3.set_xlabel('Frequency (MHz)')
ax3.set_ylabel('Magnitude')
ax3.set_title('Output FFT (AIE)')
fig.tight_layout()
plt.show()