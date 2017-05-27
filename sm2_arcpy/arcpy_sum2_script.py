import arcpy
from arcpy import env
env.workspace = r"C:\Users\User\Desktop\Progr_GIS_s2"
inDem = arcpy.GetParameterAsText(0)
featureClass = arcpy.GetParameterAsText(1)
arcpy.AddField_management("rec_sites.shp", "HEIGTH", "DOUBLE")
desc = arcpy.Describe(inDem)
ref = desc.spatialReference
dsc = arcpy.Describe(featureClass)
dsc1 = dsc.spatialReference
r = []
C = 0
if dsc1.name == ref.name:
    arcpy.AddMessage("spatial reference is right")
    with arcpy.da.SearchCursor(featureClass, ["SHAPE@XY",]) as cursor:
        for row in cursor:        
            x, y = row[0]
            result=arcpy.GetCellValue_management("C:/Users/User/Desktop/Progr_GIS_s2/elevation", str(x)+ " " + str(y))
            r.append(result.getOutput(0))
    with arcpy.da.UpdateCursor(featureClass, ["HEIGTH",]) as cursor:
        for row in cursor:
            row[0]= r[C]
            cursor.updateRow(row)
            C +=1
            arcpy.AddMessage("line`s updating")
        arcpy.CopyFeatures_management(featureClass,"C:\\Users\\User\\Desktop\\Progr_GIS_s2\\Results\\"+'res_sites_with_heigth'+'.shp')


else:
    arcpy.AddMessage("wrong spatial reference")
