import arcpy
from arcpy import env  
from arcpy.sa import *
arcpy.env.overwriteOutput = True

env.workspace = 'C:/Users/User/Desktop/Lesson1'
try:
    #создает срез по заданой высоте
    Contour('foxlake', 'C:/Users/User/Desktop/Lesson1/foxlake2.shp', 250, 0)
    arcpy.AddMessage("All done!")

except:
    arcpy.AddError("Could not draw contour lines")
    arcpy.AddMessage(arcpy.GetMessages())
