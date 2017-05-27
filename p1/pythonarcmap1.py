import arcpy
from arcpy import env  
from arcpy.sa import *
arcpy.env.overwriteOutput = True
#текущая рабочая обасть
env.workspace = 'C:/Users/User/Desktop/Lesson1'
#инерполяция
OutIDW = Idw('Precip2008Readings.shp','RASTERVALU', '' , 2,)
#рекласификация
outReclass1 = Reclassify(OutIDW,"Value", RemapRange([[0,30000,1],[30000,60000,2],[60000,90000,3],[90000,120000,4]]),'NODATA')
#конвертация из растра в полигоны
arcpy.RasterToPolygon_conversion(outReclass1, "C:/Users/User/Desktop/Lesson1/zones1.shp", "NO_SIMPLIFY",
                                  "VALUE")
#вырезание полигонов по Штату Небраска
arcpy.Clip_analysis("zones1.shp", "Nebraska.shp", "C:/Users/User/Desktop/Lesson1/finaly.shp")
