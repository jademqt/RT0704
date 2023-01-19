# build rest container
docker build -f Dockerfile_rest . -t restsv-t

# build web container
docker build -f Dockerfile_web . -t websv-t

# run dockers
docker run -dp 8000:8000 --ip 172.17.0.2 --name restsv restsv-t
docker run -dp 80:8001 --name websv websv-t
