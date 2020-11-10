install:
	pip3 install -r requirements.txt

dev-server:
	cd app && uvicorn main:app --reload

server:
	cd app && uvicorn main:app

tests:
	pytest --cov=app app/tests