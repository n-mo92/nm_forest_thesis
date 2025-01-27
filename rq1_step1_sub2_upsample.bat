:: WINDOWS BATCH FILE - UPSAMPLE

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Set up working folder (for inputs and ouputs)
set "working_folder=%cd%\processing"

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Upsample ESA layer (300m) to 5m without interpolation
gdal_translate.exe -tr 5.0 5.0 -a_nodata 0.0 -ot UInt16 %working_folder%\esa_lccs_class_3035_DE.tif %working_folder%\esa_lccs_class_3035_DE_5m.vrt

:: Upsample JAXA layer (25m) to 5m without interpolation
gdal_translate.exe -tr 5.0 5.0 -a_nodata 0.0 -ot UInt16 %working_folder%\jaxa_FNF_3035_DE.tif %working_folder%\jaxa_FNF_3035_DE_5m.vrt


:: ADD HANSEN LATER
