import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True
env.workspace = r"C:\Users\User\Desktop\Progr_GIS_s2"
inDem = "C:/Users/User/Desktop/Progr_GIS_s2/elevation"
featureClass = "rec_sites.shp"
#добавление поля в который будут добалены значения высот
arcpy.AddField_management("rec_sites.shp", "HEIGTH", "DOUBLE")
#создание обьекта Descibe для растра и выбраного шейпа
desc = arcpy.Describe(inDem)
ref = desc.spatialReference
dsc = arcpy.Describe(featureClass)
dsc1 = dsc.spatialReference
r = []
C = 0
#проверка совпадения пространственной привязки
if dsc1.name == ref.name:
    print 'spatial reference is right'
    #создание курсора для идентификации по координатам значений высот для каждой точки и добавления результатов в словарь
    with arcpy.da.SearchCursor(featureClass, ["SHAPE@XY",]) as cursor:
        for row in cursor:        
            x, y = row[0]
            result=arcpy.GetCellValue_management("C:/Users/User/Desktop/Progr_GIS_s2/elevation", str(x)+ " " + str(y))
            r.append(result.getOutput(0))
    #создание курсора для добавления в новое поле значений высот полученных из растра
    with arcpy.da.UpdateCursor(featureClass, ["HEIGTH",]) as cursor:
        for row in cursor:
            row[0]= r[C]
            cursor.updateRow(row)
            C +=1
        print "line's updated"
    #создание нового файла с новым полем высот для точки
    arcpy.CopyFeatures_management(featureClass,"C:\\Users\\User\\Desktop\\Progr_GIS_s2\\Results\\"+'res_sites_with_heigth'+'.shp')


else:
    print "Wrong"
