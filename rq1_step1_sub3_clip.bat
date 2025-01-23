:: WINDOWS BATCH FILE - UPSAMPLE

:: When echo is turned off, the command prompt doesn't appear in the output
@echo off

:: Allows you to work with variables that are modified within a loop
setlocal enabledelayedexpansion

:: Set up working folder (for inputs and ouputs)
set "working_folder=%cd%\processing"

:: Set up the shapefile for clipping (ie German Natura 2000)
set "shapefile=%cd%\outputs\natura_DE.shp"

echo Working folder : %working_folder
echo Shapefile : %shapefile%

