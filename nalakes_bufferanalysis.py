#1.) Run a geoprocessing tool in ArcMap
import arcpy 
from arcpy import env

#2.) Create a buffer
arcpy.env.overwriteOutput = True
lakes = os.path.join(folderPath,"NA_Big_Lakes.shp")
lakesBuffer = os.path.join(folderPath,"10_km_lake_buffer.shp")
distanceField = '10 Kilometers'
arcpy.Buffer_analysis(lakes, lakesBuffer, distanceField, line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field="", method="PLANAR")

#3.) Find cities that fall within 10km of a big lake
arcpy.env.overwriteOutput = True
env.workspace = os.path.join(folderPath,"Default.gdb")
in_features = [os.path.join(folderPath,"NA_Cities.shp"), os.path.join(folderPath,"10_km_lake_buffer.shp")]
output = os.path.join(folderPath,"cities_within_10km.shp")               
arcpy.Intersect_analysis(in_features, output, join_attributes="ALL", cluster_tolerance="-1 Unknown", output_type="POINT")

#4.) Print the names of cities within 10km of a Big Lakes in North America
cities=os.path.join(folderPath,"cities_within_10km.shp")
fields = ['CITY_NAME', 'SHAPE@XY']
print 'List of North American Cities Within 10km of Big Lakes:'
with arcpy.da.SearchCursor(cities, fields) as cursor:
    for row in cursor:
        print (u'{0}, {1}'.format(row[0], row[1]))
del cursor
