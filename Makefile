install:
	pip3 install -r requirements.txt

dev-server: install
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

server: tests
	uvicorn app.main:app --host 0.0.0.0 --port 80

dev-env:
	docker-compose up

lint:
	pylint apps

tests: install
	pylint -j 0 --disable=R,C app
	pytest --cov=app app/tests