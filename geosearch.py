import arcpy, urllib, urllib2, json, os

arcpy.env.overwriteOutput = True

inputAddress = arcpy.GetParameterAsText(0)
outputName = arcpy.GetParameterAsText(1)

geocode_URL = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find?f=pjson&text=" + urllib.quote(inputAddress)+"&maxLocations=5&outSR=102100&outFields=Match_addr"
geocode_request = urllib2.Request(geocode_URL)
geocode_response = urllib2.urlopen(geocode_request)

j = json.loads(geocode_response.read())
wkid = j['spatialReference']['wkid']
sr = arcpy.SpatialReference(wkid)

matchCandidates = []
for candidate in j['locations']:
    info = []
    info.append(candidate['feature']['geometry']['x'])
    info.append(candidate['feature']['geometry']['y'])
    info.append(candidate['feature']['attributes']['Match_addr'])
    matchCandidates.append(info)
    info = []

point = arcpy.Point()
ptGeometryList = []

point.X = matchCandidates[0][0]
point.Y = matchCandidates[0][1]

pointGeometry = arcpy.PointGeometry(point,sr)
ptGeometryList.append(pointGeometry)
outFC = os.path.join("in_memory","matchedAddress")
arcpy.CopyFeatures_management(ptGeometryList, outFC)
arcpy.AddField_management(outFC, "MatchAddress","Text")
ucursor = arcpy.UpdateCursor(outFC,"","","MatchAddress")
for record in ucursor:
    record.setValue("MatchAddress", matchCandidates[0][2])
    ucursor.updateRow(record)
output = arcpy.MakeFeatureLayer_management(outFC, outputName)
arcpy.SetParameter(2, output)
