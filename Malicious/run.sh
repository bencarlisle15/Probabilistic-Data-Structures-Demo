docker network create client-net || true
docker run -e PYTHONUNBUFFERED=1 --network=client-net -d --name demo_client demo_client