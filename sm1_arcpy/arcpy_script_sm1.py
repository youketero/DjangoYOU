import arcpy

arcpy.env.overwriteOutput = True
Field = 'COLLEGE'
arcpy.env.workspace = r"C:\Users\User\Desktop\Progr_GIS_s1"
path = "C:\\Users\\User\\Desktop\\Progr_GIS_s1\\Results\\"
Feature = arcpy.GetParameterAsText(0)
sel = arcpy.GetParameterAsText(1)
ds = 'facilities_Distance_3000'
searchedField = ["SDE_FACILI","PERIMETER","FAC_","D_OCT92_","D_OCT92_ID",'D_OCT92_S','TYPE','SECTORS_','JURIS_']
featureClassList = arcpy.ListFeatureClasses()
featureClass = "facilities_Distance_3000"
field = ['ColName','FAC_ID']
if featureClass not in featureClassList:    
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureClass, "POINT", "facilities.shp", "DISABLED", "DISABLED", "facilities.shp")
arcpy.MakeFeatureLayer_management(sel, "SelectionStateLayer" )
arcpy.MakeFeatureLayer_management(Feature ,'menity' , '"FACILITY" = ' + "'" + Field + "'")
arcpy.SelectLayerByLocation_management('menity',"WITHIN_A_DISTANCE","SelectionStateLayer", '5000 Meter')
arcpy.CopyFeatures_management('menity',"C:\\Users\\User\\Desktop\\Progr_GIS_s1\\Results\\"+'facilities_Distance_3000'+'.shp')
print str(ds)+'.shp'+' was created'
arcpy.DeleteField_management(path+'facilities_Distance_3000'+'.shp', searchedField )
print 'field' in str(ds)+'.shp'+" was deleted"
arcpy.AddField_management(path+'facilities_Distance_3000'+'.shp',"ColName","DOUBLE")
with arcpy.da.UpdateCursor(path+'facilities_Distance_3000'+'.shp', (field)) as cursor:
        for row in cursor:
            row[0]= row[1]
            cursor.updateRow(row)
            arcpy.AddMessage("cursor updating")
arcpy.AddMessage("all done")
