#!make

export PYTHON=python

default: run_api

run_api:
	$(PYTHON) teste

build_api_c:
	DOCKER_BUILDKIT=1 docker image build --tag python_sample_project_api:latest --build-arg SOURCE_FOLDER=api --no-cache -f Dockerfile .

run_api_c:
	docker run --name api_container -e SOURCE_FOLDER=api -e HTTP_PORT=8000 -e ORDERS_API=http://localhost:8001 -e INVOICES_API=http://localhost:8002 -p 8000:8000  python_sample_project_api:latest

stop_api_c:
	docker rm --force api_container