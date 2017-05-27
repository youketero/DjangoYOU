import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True
env.workspace = r"C:\Users\User\Desktop\Progr_GIS_s2"
inDem = "C:/Users/User/Desktop/Progr_GIS_s2/elevation"
featureClass = "rec_sites.shp"
#���������� ���� � ������� ����� �������� �������� �����
arcpy.AddField_management("rec_sites.shp", "HEIGTH", "DOUBLE")
#�������� ������� Descibe ��� ������ � ��������� �����
desc = arcpy.Describe(inDem)
ref = desc.spatialReference
dsc = arcpy.Describe(featureClass)
dsc1 = dsc.spatialReference
r = []
C = 0
#�������� ���������� ���������������� ��������
if dsc1.name == ref.name:
    print 'spatial reference is right'
    #�������� ������� ��� ������������� �� ����������� �������� ����� ��� ������ ����� � ���������� ����������� � �������
    with arcpy.da.SearchCursor(featureClass, ["SHAPE@XY",]) as cursor:
        for row in cursor:        
            x, y = row[0]
            result=arcpy.GetCellValue_management("C:/Users/User/Desktop/Progr_GIS_s2/elevation", str(x)+ " " + str(y))
            r.append(result.getOutput(0))
    #�������� ������� ��� ���������� � ����� ���� �������� ����� ���������� �� ������
    with arcpy.da.UpdateCursor(featureClass, ["HEIGTH",]) as cursor:
        for row in cursor:
            row[0]= r[C]
            cursor.updateRow(row)
            C +=1
        print "line's updated"
    #�������� ������ ����� � ����� ����� ����� ��� �����
    arcpy.CopyFeatures_management(featureClass,"C:\\Users\\User\\Desktop\\Progr_GIS_s2\\Results\\"+'res_sites_with_heigth'+'.shp')


else:
    print "Wrong"
