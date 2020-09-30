while :
do
    #echo "--- Start Call API"
    python3 kpindex.py
    RET=$?
    date
    #echo "Sleep 1 min"
    sleep 60
done