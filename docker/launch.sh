# run dockers
docker run -dp 8000:8000 --ip 172.17.0.2 --name restsv restsv-t
docker run -dp 80:8001 --name websv websv-t
