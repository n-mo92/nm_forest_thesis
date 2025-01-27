:: WINDOWS BATCH FILE - CLIP

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Allows you to work with variables that are modified within a loop
setlocal enabledelayedexpansion

:: Set up working folder (for inputs and ouputs)
set "working_folder=%cd%\processing"

:: Set up the shapefile for clipping (ie German Natura 2000)
set "shapefile=%cd%\outputs\natura_DE.shp"

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Iterate through rasters in the working folder which include 5m in the file name
for %%F in ("%working_folder%\*_5m.vrt") do (
    :: Extract the filename without extension
    set "filename=%%~nF"

    :: Set up the output filename
    set "output_file=%working_folder%\!filename!_clipped.tif"

    :: Run gdalwarp with cutline 
    gdalwarp.exe -crop_to_cutline -cutline %shapefile% -dstnodata 0.0 -ot UInt16 -co COMPRESS=LZW -co BIGTIFF=YES %%F !output_file!

    :: Run gdaladdo to generate internal overviews (so that the data can be opened in QGIS)
    ::gdaladdo.exe -r nearest -ro !output_file!
)




