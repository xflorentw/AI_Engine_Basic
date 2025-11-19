#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#
# ------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------
import numpy as np
from fxpmath import Fxp
from scipy.fft import fft, fftfreq, fftshift
import os

os.makedirs("../aie/data", exist_ok=True)

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

sig_i_cplx16 = sig_i_cplx*2**Input_shift

# Write the input to a file
with open("../aie/data/input.txt", "w") as f:
    for i in range(0,int(N_Samp),2):
        f.write(str(int(sig_i_cplx16[i].real))+" "+str(int(sig_i_cplx16[i].imag))+" "+str(int(sig_i_cplx16[i+1].real))+" "+str(int(sig_i_cplx16[i+1].imag))+"\n")

# Set outputs
golden_fft_out = np.zeros(N_Taps * Iterations, dtype=complex)

# ------------------------------------------------------------
# FFT
# ------------------------------------------------------------

# Process each frame with Python
for i in range(0, Iterations):
    input_data = sig_i_cplx[i*1024:(i+1)*1024]
    
    # Run Pyton FFT
    golden_fft_out[i*1024:(i+1)*1024] = fft(input_data)

golden_fft_out = Fxp(golden_fft_out, dtype='S10.5')
golden_fft_out = golden_fft_out.astype(complex)
golden_fft_out = golden_fft_out*2**5

# Write the output reference to a file
with open("../aie/data/output_ref.txt", "w") as f:
    for i in range(0,int(N_Samp),2):
        f.write(str(int(golden_fft_out[i].real))+" "+str(int(golden_fft_out[i].imag))+" "+str(int(golden_fft_out[i+1].real))+" "+str(int(golden_fft_out[i+1].imag))+"\n")