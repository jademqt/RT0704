#!/bin/bash

mkdir log
touch log/log_web log/log_rest

# launch rest server
python3 rest/server/sv.py > log/log_rest 2>&1 &
echo "rest server launched"

#launch web server
python3 web/app.py > log/log_web 2>&1 &
echo "web server launched"
