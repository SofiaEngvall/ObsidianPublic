# Converts a .csv file to .kml
# Sofia Engvall, FixIt42, 2025-06-06

from os import path

CSV_FILE = "C:/Users/sofia/Downloads/location-services-2-points.csv"
KML_FILE = "C:/Users/sofia/Downloads/location-services-2-points.kml"

kml_out = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
kml_out += "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n"
kml_out += "  <Document>\n"
kml_out += "    <name>"+path.splitext(path.basename(CSV_FILE))[0]+"</name>\n"
kml_out += "    <description>Converted GPS coordinates with date-time labels</description>\n\n"

with open(CSV_FILE,"r",encoding="utf16") as rfile: # For other encodings, update utf16 to what you use
    for line in rfile:
        if len(line.strip()) > 1:
            # For other csv types, update the columns to match, using _ for not used columns
            longitude, latitude, name = line.split(",") #in this case we have date and time as name
            kml_out += f"    <Placemark><name>{name.strip()}</name><Point><coordinates>{latitude.strip()},{longitude.strip()},0</coordinates></Point></Placemark>\n"

kml_out += "  </Document>\n"
kml_out += "</kml>"

with open(KML_FILE,"w",encoding="latin-1") as wfile:
    wfile.write(kml_out)
