#!/bin/bash

# launch rest server
python3 rest/server/sv.py 2>log/log_rest &

#launch web server
python3 web/app.py 2>log/web_log &
