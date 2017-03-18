# asterisk-rest
A Flask based proof concept REST API for querying an Asterisk server

Call http://server:5000/api/v1.0/calls to get last 3 month of CDR data.

If you want a local the hours in localtime, ensure you have this in your  /etc/asterisk/cdr.conf.
```
[csv]
usegmtime=no     ; log date/time in GMT.  Default is "no"
```

If your CDR isn't in /var/log/asterisk/cdr-csv/Master.csv, you should fix the path in the file

More information at (french only, sorry) : http://blog.da-rocha.net/flask/asterisk\_rest.html
