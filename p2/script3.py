import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)

arcpy.env.overwriteOutput = True

try:
    fcList = arcpy.ListFeatureClasses()
    rootName = ""
    sr = arcpy.SpatialReference("NAD 1983 UTM Zone 11N")
    for fc in fcList:
        dsc = arcpy.Describe(fc)
        coord_sys = dsc.spatialReference
        if coord_sys.name != sr:
            if fc.endswith(".shp"):
                rootName = fc[:-4]
                arcpy.Project_management(fc, rootName + '_projected'+'.shp', sr)
                arcpy.AddMessage("reproject")
    arcpy.AddMessage("ALL DONE")

except:
    
    arcpy.AddError("Could not conect to folder")
