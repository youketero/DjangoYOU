import arcpy
from arcpy import env  
from arcpy.sa import *
arcpy.env.overwriteOutput = True

inPath = arcpy.GetParameterAsText(0)
outPath = arcpy.GetParameterAsText(1)

Contour(inPath, outPath, 250, 0)
