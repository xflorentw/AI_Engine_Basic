# AMD DSPLib 1024-point FFT on AIE-ML

This project is a simple AIE-ML graph implementing a 1024-point FFT using the AMD DSP Library

You can use this project to replicate the steps from the following articles:<br />
<a href="https://www.hackster.io/florent-werbrouck/14-building-an-fft-on-amd-aie-ml-using-the-dsp-library-a14307">14 Building an FFT on AMD AIE-ML using the DSP Library</a><br />
<a href="https://www.hackster.io/florent-werbrouck/15-generating-input-txt-files-stimuli-for-aie-ml-from-python-358b9a">15 Generating input txt files stimuli for AIE-ML from Python</a><br />
<a href="https://www.hackster.io/florent-werbrouck/16-simulate-ai-engine-graphs-from-python-fb171f">16 Simulate AI Engine graphs from Python</a><br />
<a href="https://www.hackster.io/florent-werbrouck/17-simulate-ai-engine-graphs-from-matlab-bcb16c">17 Simulate AI Engine graphs from MATLAB</a><br />

Before running the command to rebuild the project you will need to clone the <a href="https://github.com/Xilinx/Vitis_Libraries">Vitis_Libraries repository</a> and set an environment variable DSPLIB_ROOT pointing to Vitis_Libraries/dsp

## AMD Vitis Workspace

To rebuild the final Vitis Workspace after tutorial 14 run the following command:
```
make all
```

To rebuild the worspace with the input data file generated from the Python script as per tutorial 15, run the following command:
```
make all VERSION=2
```

## Vitis Functional Simulation (VFS)
The AIE-ML graph can be simulated directly from a Python or MATLAB script using the AMD Vitis Functional Simulation (VFS) feature as described in the tutorials 16 and 17. 
To run the VFS simulation using Python3:
```
cd vfs/python
python3 fft1024_dsplib_vfs.py
```

To run the VFS simulation using MATLAB:
```
cd vfs/matlab
matlab -nojvm -r "fft1024_dsplib_vfs"
```
Note that you will need to have the Vitis environment set to run the VFS simulation.

<p class="sphinxhide" align="center"><sub>Copyright © 2025 Florent Werbrouck</sub></p>