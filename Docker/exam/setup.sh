# remove log if exists

cd authentication
docker image build . -t authentication:latest

cd ../authorization
docker image build . -t authorization:latest

cd ../content
docker image build . -t content:latest

cd ..
docker compose up
