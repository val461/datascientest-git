# ? mkdir some folders, e.g. log

# dans le dossier de l'image
docker image build . -t authentication:latest

# dans le dossier avec docker-compose.yml
docker compose up
