# Dynamically-changing-cache-size-and-associativity-of-L1-L2-cache

The aim of the project was to change the cache associativity and size of the L1 and L2 cache dynamically.
In order to obtain the results, changes have been made to the python file: one_core.py, SMTSIM source files: run.c and cache.c.
Python File:
I have selected applu, bzip2_source and cactusADM_06 as my benchmarks for the simulation of the project. Necessary changes have been made to the one_core.py file in order to execute 10M instructions with 10M fast forward. Files applu.py, bzip2_source.py and cactusADM_06.py that are attached, serve as input for the project.
Run.c:
The run.c file present in the src folder is altered as per the python file and the SMTSIM is built again. After successfully building the SMTSIM, python files are run and the output files are generated.
Cache.c:
I have added a print statement in the memory access and write back loop respectively.
We have 16 output files for all the three benchmarks, corresponding to 16 different configurations that we have used. Each of the output file has 1000 sampled values of IPC, which are extracted from the file using the python code that I have attached with the submission. After obtaining IPC values in text format, values are tabulated in excel sheets. Other necessary information like IPC^2 are calculated using excel itself.
Power values are obtained using CACTI 5.3. Both dynamic and leakage power are taken into consideration while assuming total power. Exact calculation is shown on Power sheet of the excel file. Target functions i.e IPC/power and IPC^2/power are then obtained using formulas on excel.
Most efficient configuration is obtained (table is traversed) in excel using MAX function for each of the configuration for all the three benchmarks. Despite IPC values being high for other configuration, the configuration with L1_size: 32KB, L1_assoc: 1-way, L2_size: 128KB, L2_assoc: 2-way was found to be the most efficient for all the three benchmarks. Graphs have been attached separately.
