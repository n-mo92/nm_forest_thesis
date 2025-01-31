:: WINDOWS BATCH FILE - CLIP

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Allows you to work with variables that are modified within a loop
setlocal enabledelayedexpansion

:: Set up working folder (for inputs and ouputs)
set "working_folder=%cd%\processing"

:: Change directory to where gdal is stored
cd thesis_env_conda\Library\bin

:: Create shapefile for clipping - based on CORINE footprint 
::gdal_footprint.exe -overwrite -max_points unlimited %working_folder%\U2018_CLC2018_V2020_3035_DE_5m.tif %working_folder%\clipper.shp

:: Set up the new shapefile for clipping
set "shapefile=%working_folder%\clipper.shp"

:: Iterate through rasters in the working folder which include "_reclass" in the file name
for %%F in ("%working_folder%\*_reclass.tif") do (
    :: Extract the filename without extension
    set "filename=%%~nF"

    :: Set up the output filename
    set "output_file=%working_folder%\!filename!_clipped.tif"

    :: Run gdalwarp with cutline 
    gdalwarp.exe -crop_to_cutline -cutline %shapefile% -dstnodata -9999 -ot Int16 -co COMPRESS=LZW -co BIGTIFF=YES %%F !output_file!

    :: Run gdaladdo to generate overviews (so that the data can be opened faster in QGIS)
    ::gdaladdo.exe -r nearest -ro !output_file!
) 