docker network create client-net || true
docker run -e PYTHONUNBUFFERED=1 --network=client-net -d --name demo_server demo_server