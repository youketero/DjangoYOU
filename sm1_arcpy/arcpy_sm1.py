import arcpy

arcpy.env.overwriteOutput = True
Field = 'COLLEGE'
arcpy.env.workspace = r"C:\Users\User\Desktop\Progr_GIS_s1"
path = "C:\\Users\\User\\Desktop\\Progr_GIS_s1\\Results\\"
Feature = 'facilities.shp'
sel = 'zip.shp'
ds = 'facilities_Distance_3000'
searchedField = ["SDE_FACILI","PERIMETER","FAC_","D_OCT92_","D_OCT92_ID",'D_OCT92_S','TYPE','SECTORS_','JURIS_']
featureClassList = arcpy.ListFeatureClasses()
featureClass = "facilities_Distance_3000"
field = ['ColName','FAC_ID']
if featureClass not in featureClassList:    
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureClass, "POINT", "facilities.shp", "DISABLED", "DISABLED", "facilities.shp")
#создание слоя с шейпа с полигином
arcpy.MakeFeatureLayer_management(sel, "SelectionStateLayer" )
#создание слоя с точек
arcpy.MakeFeatureLayer_management(Feature ,'menity' , '"FACILITY" = ' + "'" + Field + "'")
#создание выборки по полигону из шейпа с заданым расстоянием
arcpy.SelectLayerByLocation_management('menity',"WITHIN_A_DISTANCE","SelectionStateLayer", '5000 Meter')
#копирование обьектов в новый файл
arcpy.CopyFeatures_management('menity',"C:\\Users\\User\\Desktop\\Progr_GIS_s1\\Results\\"+'facilities_Distance_3000'+'.shp')
print str(ds)+'.shp'+' was created'
#удаление нунужных полей
arcpy.DeleteField_management(path+'facilities_Distance_3000'+'.shp', searchedField )
print 'field' in str(ds)+'.shp'+" was deleted"
#добавление нового поля
arcpy.AddField_management(path+'facilities_Distance_3000'+'.shp',"ColName","DOUBLE")
#создание курсора для в добавления в новое поле данных
with arcpy.da.UpdateCursor(path+'facilities_Distance_3000'+'.shp', (field)) as cursor:
        for row in cursor:
            row[0]= row[1]
            cursor.updateRow(row)
print 'cursor updating'
print 'all done'
