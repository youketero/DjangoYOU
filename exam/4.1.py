# This script reads a GPS track in CSV format and writes geometries from the list of coordinate pairs



import csv
import arcpy
import os
from arcpy import env
from datetime import datetime, date, time
arcpy.env.overwriteOutput = True
env.workspace = r"C:\Users\User\Desktop\Lesson3"
feature = 'tracklines.shp'
# Set up input and output variables for the script
gpsTrack = open(r"C:\Users\User\Desktop\Lesson3\gps_track.txt", "r")
polylineFC = r"C:/Users/User/Desktop/Lesson3/tracklines.shp"
if not os.path.isfile(polylineFC):
    from arcpy import env
    env.workspace = r"C:\Users\User\Desktop\Lesson3"
    arcpy.CreateFeatureclass_management(env.workspace, "tracklines.shp", "POLYLINE", "", "DISABLED", "DISABLED", r"C:/Users/User/Desktop/Lesson3/counties.shp")
desc = arcpy.Describe(feature)
ref = desc.spatialReference
# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack)
header = csvReader.next()
latIndex = header.index("lat")
lonIndex = header.index("long")
new_seg = header.index("new_seg")
timeIndex = header.index('time')
ltimeIndex = header.index('ltime')
# Create an empty array object
vertexArray = arcpy.Array()
# Loop through the lines in the file and get each coordinate
arcpy.AddField_management("tracklines.shp", "timest", "TEXT")
arcpy.AddField_management("tracklines.shp", "timef", "TEXT")
with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",'timest','timef')) as cursor:
    # Create an empty array object
    vertexArray = arcpy.Array()
    # Loop through the lines in the file and get each coordinate
    for row in csvReader:       
        isNew = row[new_seg].upper()
        # If about to start a new line, add the completed line to the
        #  feature class
        if isNew == "TRUE":
            if vertexArray.count > 0:
                addPolyline(cursor, vertexArray, ref)
        # Get the lat/lon values of the current GPS reading
        lat = float(row[latIndex])
        lon = float(row[lonIndex])
        timeIndex =datetime.time((row[timeIndex]))
        ltimeIndex = datetime.time(float(row[ltimeIndex]))
        # Make a point from the coordinate and add it to the array
        vertex = arcpy.Point(lon,lat)
        vertexArray.add(vertex)
 
    # Add the final polyline to the shapefile
    polyline = arcpy.Polyline(vertexArray, ref)
    cursor.insertRow((polyline,timeIndex,ltimeIndex))
    vertexArray.removeAll()

print "All done!"

