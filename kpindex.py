import urllib.request, json, os
from influxdb import InfluxDBClient
#https://services.swpc.noaa.gov/json/planetary_k_index_1m.json


# settings from EnvionmentValue
influxhost=os.getenv('INFLUXDB_HOST', "influxdb")
influxport=os.getenv('INFLUXDB_PORT', 8086)
influxuser=os.getenv('INFLUXDB_USER', 'root')
influxpw=os.getenv('INFLUXDB_PW', 'root')
influxdb=os.getenv('INFLUXDB_DATABASE', 'solar')
debug=os.getenv('DEBUG', 'False')

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

if str2bool(debug):
  print("Influxdb Host: " + influxuser + "@" + influxhost + ":" + str(influxport))
  print("Influxdb Password: " + '*'*len(influxpw))
  print("Influxdb DB: " + influxdb)

client = InfluxDBClient(influxhost, influxport, influxuser, influxpw, influxdb)

with urllib.request.urlopen("https://services.swpc.noaa.gov/json/planetary_k_index_1m.json") as url:
    data = json.loads(url.read().decode())
    #print(data)

for row in data:
    #print(row)

    CurKPindex = [{
	"measurement": 'planetary_k_index',
    "time": row['time_tag'],
    "fields": {
        "kp_index": row['kp_index']
    }
    }]

    if str2bool(debug):
        print(CurKPindex)
    
    client.write_points(CurKPindex)