import arcpy
arcpy.env.overwriteOutput = True
featureClass = r"D:\p3\OSMpoints.shp"
populationField = 'amenity'
amenities = ['school','hospital','place_of_worship']
field = ('source','GID','id')
Layer = r"D:\p3\CentralAmerica.shp"
state = "El Salvador"
nameField = "NAME"
value = 'Open street map'

arcpy.MakeFeatureLayer_management(Layer, "SelectionStateLayer", '"' + str(nameField) + '" =' + "'" + str(state) + "'")



for amenity in amenities:
    arcpy.MakeFeatureLayer_management(featureClass,amenity , '"amenity" = ' + "'" + amenity + "'")
    arcpy.SelectLayerByLocation_management(amenity,"WITHIN","SelectionStateLayer")
    arcpy.CopyFeatures_management(amenity,"D:\\p3\\"+amenity)
    arcpy.AddField_management("D:\\p3\\" + amenity + ".shp", "source", "TEXT")
    arcpy.AddField_management("D:\\p3\\" + amenity + ".shp", "GID", "DOUBLE")
    with arcpy.da.UpdateCursor("D:\\p3\\" + amenity + ".shp", (field)) as cursor:
        for row in cursor:
            row[0]= value
            row[1] = row[2]
            cursor.updateRow(row)


 
