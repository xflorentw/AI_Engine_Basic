%
% Copyright (C) 2025, Florent Werbrouck. All rights reserved.
% SPDX-License-Identifier: MIT
%
clear all;

% Get DSP Library path
DSPLIB = getenv("DSPLIB_ROOT");

if isempty(DSPLIB)
    disp('DSPLIB_ROOT environment not set. Please download the Vitis_Libraries repository and point to the dsp folder')
    disp('https://github.com/Xilinx/Vitis_Libraries')
    return;
else
    disp('Using DSPLIB from DSPLIB_ROOT environment variable')
end

% ------------------------------------------------------------
% Initialize the AIE graph
% ------------------------------------------------------------
myaiefft = vfs.aieGraph(input_file="../../aie/src/14/graph_FFT_1024.cpp",...
                       part = 'xcve2302-sfva784-1LP-e-S',...
                       include_paths = {"../../aie/src/14/",...
                       strcat(DSPLIB,"/L2/include/aie/"),...
                       strcat(DSPLIB,"/L1/include/aie/"),...
                       strcat(DSPLIB,"/L1/src/aie/")});

% ------------------------------------------------------------
% Generate Simulus I/O
% ------------------------------------------------------------
%Parameters
Iterations = 1;
Input_shift = 15;
N_Taps = 1024;
F1_MHz = 50;
F2_MHz = 150;
Fs_MHz = 400;

% Number of sample points
N_Samp = N_Taps * Iterations;
% sample spacing
T = 1.0 / Fs_MHz;
A1 = 0.2;
A2 = 0.4;

% Generate Input Signal
tone1 = A1 * exp(1i*2*pi*F1_MHz/Fs_MHz*[0:N_Samp-1]);
tone2 = A2 * exp(1i*2*pi*F2_MHz/Fs_MHz*[0:N_Samp-1]);
sig_i = tone1 + tone2;

% Quantize:
sig_i_cplx = fi(sig_i,1,16,15,'RoundingMethod','Nearest','OverflowAction','Saturate');
sig_i_cplx = double(sig_i_cplx);

% ------------------------------------------------------------
% FFT
% -----------------------------------------------------------
% Process each frame with AI Engine X86 Simulation and Python
for i = 0 : 1 : Iterations-1
    input_data = sig_i_cplx(i*1024+1:(i+1)*1024);

    % Run AIE graph processing
    y_aie = myaiefft.run(varray.cint16(input_data*2^Input_shift));
    aie_data(i*1024+1:(i+1)*1024) = double(y_aie);

    % Run MATLAB fft
    matlab_data(i*1024+1:(i+1)*1024) = fft(input_data);
end

% ------------------------------------------------------------
% Error Check AIE vs Golden
% ------------------------------------------------------------
error_threshold = 1/2^4;
error = 0;

matlab_data = fi(matlab_data,1,16,6,'RoundingMethod','Nearest','OverflowAction','Saturate');
aie_data = fi(aie_data/2^5,1,16,6,'RoundingMethod','Nearest','OverflowAction','Saturate');

for i = 1 : 1 : size(aie_data,2)
    if aie_data(i) ~= matlab_data(i)
        if abs(aie_data(i) - matlab_data(i)) > error_threshold
            fprintf("Error in sample %d\n", i)
            fprintf("Golden %f +i%f\n", real(matlab_data(i)), imag(matlab_data(i)))
            fprintf("AIE Output %f +i %f\n", real(aie_data(i)),imag(aie_data(i)))
            error = error+ 1;
        end
    end
end

if(error<1)
    disp('AI Engine FFT matches the Python FFT within 2 LSB')
else
    disp('Test Failed')
    fprintf('Nb errors : %d\n',error)
end

% Plot outputs
xf = Fs_MHz/N_Taps*(0:N_Taps-1);

subplot(3,1,1); plot((0:1023), real(sig_i(1:1024))); title("Input Signal");
subplot(3,1,2); plot(xf, abs(matlab_data(1:1024))); title("Output FFT (Matlab)");
subplot(3,1,3); plot(xf, abs(aie_data(1:1024))); title("Output FFT (AIE)");