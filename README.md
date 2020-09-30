# kpindex-influxdb
logs kp index to influxdb

## How to run
```
docker run -d \
 -e INFLUXDB_HOST="influxdb" \
 -e INFLUXDB_DATABASE="solar" \
 --name "kpindex-influxdb" \
kpindex
```