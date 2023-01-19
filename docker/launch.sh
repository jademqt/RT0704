# run dockers
docker run -dp 8000:8000 --ip 172.17.0.2 --name restsv -v /home/toto/RT0704/docker/rest:/app restsv-t
docker run -dp 80:8001 --name websv -v /home/toto/RT0704/docker/web:/app websv-t
