import arcpy
arcpy.env.overwriteOutput = True
featureClass = arcpy.GetParameterAsText(0)
populationField = 'amenity'
amenities = ['school','hospital','place_of_worship']
field = ('source','GID','id')
Layer = arcpy.GetParameterAsText(1)
state = arcpy.GetParameterAsText(2)
nameField = "NAME"
value = 'Open street map'
value1 = 'GID'

arcpy.MakeFeatureLayer_management(Layer, "SelectionStateLayer", '"' + str(nameField) + '" =' + "'" + str(state) + "'")



for amenity in amenities:
    arcpy.MakeFeatureLayer_management(featureClass,amenity , '"amenity" = ' + "'" + amenity + "'")
    arcpy.SelectLayerByLocation_management(amenity,"WITHIN","SelectionStateLayer")
    arcpy.CopyFeatures_management(amenity,"D:\\p3\\"+amenity)
    print "File named "+str(amenity)+ " was created"
    arcpy.AddField_management("D:\\p3\\" + amenity + ".shp", "source", "TEXT")
    arcpy.AddField_management("D:\\p3\\" + amenity + ".shp", "GID", "DOUBLE")
    print "Fields "+str(value)+' and '+str(value1)+' was added'
    print "preapering to update line's in "+str(amenity)+'.shp'
    with arcpy.da.UpdateCursor("D:\\p3\\" + amenity + ".shp", (field)) as cursor:
        for row in cursor:
            row[0]= value
            row[1] = row[2]
            cursor.updateRow(row)
    print "line's updated"

 
