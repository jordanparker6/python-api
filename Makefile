install:
	pip3 install -r requirements.txt

dev-server:
	uvicorn app.main:app --reload

server: tests
	uvicorn app.main:app

lint:
	pylint app

tests:
	pylint -j 0 --disable=R,C app
	pytest --cov=app app/tests