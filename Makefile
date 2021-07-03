install:
	pip3 install -r requirements.txt

dev-server:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

server:
	uvicorn app.main:app --host 0.0.0.0 --port 80

build:
	docker build . -t python-api

prod-env:
	kubectl apply -f deployments/prod-deployments.yml

test-env:
	kubectl apply -f deployments/test-deployments.yml

dev-env:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

lint:
	pylint apps

tests: install
	pylint -j 0 --disable=R,C app
	pytest --cov=app app/tests