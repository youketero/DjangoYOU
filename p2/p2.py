import arcpy

arcpy.env.workspace = r"D:\Lesson2"
fcList = arcpy.ListFeatureClasses()
rootName = ""
sr = arcpy.SpatialReference("NAD 1983 UTM Zone 11N")
for fc in fcList:
    #�������� ������� Describe
    dsc = arcpy.Describe(fc)
    #��������� ���������������� �������� �����
    coord_sys = dsc.spatialReference
    #�������� ���������� ���������������� ��������
    if coord_sys.name != sr:
        #��� ������������ �������� ������������ � ������ ������� ���������
        if fc.endswith(".shp"):
            rootName = fc[:-4]
            arcpy.Project_management(fc, rootName + '_projected'+'.shp', sr)
            
              


