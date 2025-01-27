:: WINDOWS BATCH FILE - RASTERISE

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Set up working folder (for inputs and ouputs)
set "working_folder=%cd%\processing"

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Rasterise the CLC18 column for the GER LULC Class 3 data to 5m 
gdal_rasterize.exe -l clc5_class3xx_3035_DE_int -a CLC18 -tr 5.0 5.0 -a_nodata 0.0 -ot UInt16 -of GTiff -co COMPRESS=LZW %working_folder%\clc5_class3xx_3035_DE_int.shp %working_folder%\clc5_class3xx_3035_DE_5m.tif

:: Rasterise the Code_18 column for the CORINE data to 5m
gdal_rasterize.exe -l U2018_CLC2018_V2020_DE -a Code_18 -tr 5.0 5.0 -a_nodata 0.0 -ot UInt16 -of GTiff -co COMPRESS=LZW %working_folder%\U2018_CLC2018_V2020_DE.shp %working_folder%\U2018_CLC2018_V2020_3035_DE_5m.tif
