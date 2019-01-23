# Builds
build-docker:
	docker build -t plaas .
build-docker-testing:
	docker build -t plaas-testing -f Dockerfile.testing .

# Tests
test:
	pipenv run pytest tests
test-docker:
	make build-docker-testing
	docker run plaas-testing

# RUN!
run-dev:
	make build-docker
	docker run -e PORT=8080 -p 8080:8080 plaas
run-port:
	make build-docker
	docker run -e PORT -p ${PORT}:${PORT} plaas
run-prod:
	make build-docker
	docker run -p 80:80 plaas