import arcpy
from arcpy import env  
from arcpy.sa import *
arcpy.env.overwriteOutput = True
env.workspace = 'C:/Users/User/Desktop/Lesson1'

inPath = arcpy.GetParameterAsText(0)
outPath = arcpy.GetParameterAsText(1)
power = arcpy.GetParameterAsText(2)
reclass = arcpy.GetParameterAsText(3)

OutIDW = Idw(inPath,'RASTERVALU', '' , power,)
arcpy.AddMessage("points are interpolated")
outReclass1 = Reclassify(OutIDW,"Value", RemapRange(reclass),'NODATA')
arcpy.AddMessage("reclassified")
arcpy.RasterToPolygon_conversion(outReclass1, "C:/Users/User/Desktop/Lesson1/zones.shp", "NO_SIMPLIFY",
                                  "VALUE")
arcpy.AddMessage("convert from raster to polygon")
arcpy.Clip_analysis("zones1.shp", "Nebraska.shp", outPath)

arcpy.AddMessage("polygons are clipped")
arcpy.AddMessage("All done!")
