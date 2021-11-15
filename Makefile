#!make

export PYTHON=python

default: run_api

run_api:
	./src/xpto/api/run.sh

build_api_c:
	DOCKER_BUILDKIT=1 docker image build --tag python_sample_project_api:latest --build-arg SOURCE_FOLDER=api --no-cache -f Dockerfile .

run_api_c:
	docker run --name api_container -e SOURCE_FOLDER=api -e HTTP_PORT=8000 -e ORDERS_API=http://localhost:8001 -e INVOICES_API=http://localhost:8002 -p 8000:8000  python_sample_project_api:latest

stop_api_c:
	docker rm --force api_container

run_orders:
	./src/xpto/orders/run.sh

build_orders_c:
	DOCKER_BUILDKIT=1 docker image build --tag python_sample_project_orders:latest --build-arg SOURCE_FOLDER=orders --no-cache -f Dockerfile .

run_orders_c:
	docker run --name orders_container -e SOURCE_FOLDER=orders -e mongodb_conn_string=mongodb://localhost:27020/orders -e HTTP_PORT=8000 -p 8001:8000  python_sample_project_orders:latest

stop_orders_c:
	docker rm --force orders_container

run_invoices:
	./src/xpto/invoices/run.sh

build_invoices_c:
	DOCKER_BUILDKIT=1 docker image build --tag python_sample_project_invoices:latest --build-arg SOURCE_FOLDER=invoices --no-cache -f Dockerfile .

run_invoices_c:
	docker run --name invoices_container -e SOURCE_FOLDER=invoices -e mongodb_conn_string=mongodb://localhost:27020/invoices -e HTTP_PORT=8000 -p 8002:8000  python_sample_project_invoices:latest

stop_invoices_c:
	docker rm --force invoices_container