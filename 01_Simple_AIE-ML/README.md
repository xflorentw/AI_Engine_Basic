# Simple AIE-ML Component

You can use this project to replicate the steps from the following articles:<br />
<a href="https://www.hackster.io/florent-werbrouck/07-introduction-to-amd-ai-engine-programming-9dbdd3">07 Introduction to AMD AI Engine Programming</a><br />
<a href="https://www.hackster.io/florent-werbrouck/08-introduction-to-amd-ai-engine-compile-sim-tools-289cc6">08 Introduction to AMD AI Engine Compile/Sim Tools</a><br />
<a href="https://www.hackster.io/florent-werbrouck/09-analysis-of-the-latency-and-of-an-ai-engine-graph-7e1028">09 Analysis of the latency and of an AI Engine graph</a><br />
<a href="https://www.hackster.io/florent-werbrouck/10-improving-amd-ai-engine-graph-latency-and-throughput-83ff1b">10 Improving AMD AI Engine graph latency and throughput</a><br />
<a href="https://www.hackster.io/florent-werbrouck/11-ai-engine-kernel-code-performances-analysis-eb79ab">11 AI Engine Kernel Code performances analysis</a><br />
<a href="https://www.hackster.io/florent-werbrouck/12-aie-ml-kernel-vectorization-7cac6e">12 AIE-ML kernel vectorization</a><br />
<a href="https://www.hackster.io/florent-werbrouck/13-memory-alignment-in-ai-engine-5ee3c3">13 Memory alignment in AI Engine</a><br />

To rebuild the initial Vitis Workspace for tutorial 07 - 08 - 09 - 10 run the following command:
```
make all
```

To build the project after the graph optimizations from tutorial 10 (to follow tutorial 11 and 12), run the following command:
```
make all VERSION=2
```

To build the project after the kernel optimization from tutorial 12, run the following command:
```
make all VERSION=3
```

To build the project for tutorial 13, run the following command:
```
make all VERSION=4
```

<p class="sphinxhide" align="center"><sub>Copyright © 2025 Florent Werbrouck</sub></p>