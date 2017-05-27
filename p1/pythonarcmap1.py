import arcpy
from arcpy import env  
from arcpy.sa import *
arcpy.env.overwriteOutput = True
#������� ������� ������
env.workspace = 'C:/Users/User/Desktop/Lesson1'
#�����������
OutIDW = Idw('Precip2008Readings.shp','RASTERVALU', '' , 2,)
#��������������
outReclass1 = Reclassify(OutIDW,"Value", RemapRange([[0,30000,1],[30000,60000,2],[60000,90000,3],[90000,120000,4]]),'NODATA')
#����������� �� ������ � ��������
arcpy.RasterToPolygon_conversion(outReclass1, "C:/Users/User/Desktop/Lesson1/zones1.shp", "NO_SIMPLIFY",
                                  "VALUE")
#��������� ��������� �� ����� ��������
arcpy.Clip_analysis("zones1.shp", "Nebraska.shp", "C:/Users/User/Desktop/Lesson1/finaly.shp")
