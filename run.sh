#!/bin/bash

echo "launching REST server..."
# launch rest server
python3 rest/server/sv.py > log/log_rest 2>&1 &
pid1=$!

echo "launching web server..."
#launch web server
python3 web/app.py > log/log_web 2>&1 &
pid2=$!


trap "echo killing servers...; kill ${pid1} ${pid2}; echo done.; exit" SIGINT SIGQUIT

echo "press [Ctrl+C] to stop..."
wait
