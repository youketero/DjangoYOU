import arcpy

arcpy.env.workspace = r"D:\Lesson2"
fcList = arcpy.ListFeatureClasses()
rootName = ""
sr = arcpy.SpatialReference("NAD 1983 UTM Zone 11N")
for fc in fcList:
    #создание обьекта Describe
    dsc = arcpy.Describe(fc)
    #получение пространственной привязки файла
    coord_sys = dsc.spatialReference
    #проверка совпадения пространственной привязки
    if coord_sys.name != sr:
        #при несовпадении привязок перепривязка в нужную систему координат
        if fc.endswith(".shp"):
            rootName = fc[:-4]
            arcpy.Project_management(fc, rootName + '_projected'+'.shp', sr)
            
              


