:: WINDOWS BATCH FILE - RASTERISE

:: When echo is turned off, the command prompt doesn't appear in the Command Prompt window.
@echo off

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Rasterise the CLC18 column for the GER LULC Class 3 data to 5m 
 gdal_rasterize.exe -l clc5_class3xx_3035_DE_int -a CLC18 -tr 5.0 5.0 -a_nodata 0.0 -ot Float32 -of GTiff -co COMPRESS=LZW %~dp0\processing\clc5_class3xx_3035_DE_int.shp %~dp0\processing\clc5_class3xx_3035_DE_5m.tif

:: Rasterise the Code_18 column for the CORINE data to 5m
gdal_rasterize.exe -l U2018_CLC2018_V2020_20u1 -a Code_18 -tr 5.0 5.0 -a_nodata 0.0 -ot Float32 -of GTiff -co COMPRESS=LZW %~dp0\processing\U2018_CLC2018_V2020_20u1.shp %~dp0processing\U2018_CLC2018_V2020_20u1_3035_DE_5m.tif




:: Note: %~dp0 refers to the main directory in which this batch script is stored