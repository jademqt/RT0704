#!/bin/bash

needed_dirs=("log" "web" "rest" "rest/api" "rest/api/persons" "rest/api/movies" "rest/api/vlib")

check_dir () {
	if [[ -d ${1} ]]
	then
		echo "directory ${1} OK"
	else
		echo "creating directory ${1}"
		mkdir ${1}
	fi
}

config_ip () {
	ip=`ip a | grep eth0 | tail -1 | cut -c 10-19`
	sed -r "s/10.11.[0-9]+.[0-9]+/${ip}/" config.json | tee config2.json 1>/dev/null
	mv config2.json config.json
}

for i in "${needed_dirs[@]}"
do
	check_dir "${i}"
done

touch log/log_web log/log_rest

config_ip

# launch rest server
python3 rest/server/sv.py > log/log_rest 2>&1 &
pid1=$!
echo "REST server running on port 8000, pid ${pid1}"

#launch web server
python3 web/app.py > log/log_web 2>&1 &
pid2=$!
echo "Web server running on port 8001, pid ${pid2}"

trap "echo Killing servers...; kill ${pid1} ${pid2}; echo Done.; exit" SIGINT SIGQUIT

echo "Press [Ctrl+C] to stop..."
wait
