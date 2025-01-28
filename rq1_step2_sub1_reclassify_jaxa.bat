:: WINDOWS BATCH FILE - RECLASSIFY JAXA

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Set up input & output files
set "input_file=%cd%\processing\jaxa_FNF_3035_DE_clipped.tif"
set "ouput_file=%cd%\outputs\jaxa_FNF_3035_DE_finalFNF.tif"

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Reclassify JAXA (0 stays 0; 1 stays 1; 2 becomes 1; 3 or more becomes 0)
gdal_calc.exe -A %input_file% --outfile=%output_file% --calc="0*(A==0)+1*(A==1)+1*(A==2)+0*(A>=3)" 