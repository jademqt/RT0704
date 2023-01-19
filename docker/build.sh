# build rest container
docker build -f Dockerfile_rest . -t restsv-t

# build web container
docker build -f Dockerfile_web . -t websv-t


