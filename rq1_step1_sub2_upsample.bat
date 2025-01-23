:: WINDOWS BATCH FILE - UPSAMPLE

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Upsample ESA layer (300m) to 5m without interpolation
gdal_translate.exe -tr 5.0 5.0 -a_nodata 0.0 -ot Float32 -of GTiff -co COMPRESS=LZW -co BIGTIFF=YES %~dp0\processing\esa_lccs_class_3035_DE.tif %~dp0\processing\esa_lccs_class_3035_DE_5m.tif

:: Upsample JAXA layer (25m) to 5m without interpolation
gdal_translate.exe -tr 5.0 5.0 -a_nodata 0.0 -ot Float32 -of GTiff -co COMPRESS=LZW %~dp0\processing\jaxa_FNF_3035_DE.tif %~dp0\processing\jaxa_FNF_3035_DE_5m.tif


:: ADD HANSEN LATER


:: Note: %~dp0 refers to the main directory in which this batch script is stored
