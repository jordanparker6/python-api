install:
	pip3 install -r requirements.txt

dev-server:
	uvicorn app.main:app --reload

server:
	uvicorn app.main:app

tests:
	pytest --cov=app app/tests