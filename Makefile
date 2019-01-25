NAME   		:= biosan/plaas
COMMIT_HASH := $(shell git log -1 --pretty=%h)
COMMIT_TAG	:= $(shell git tag -l --points-at HEAD)
TAG			:= $(if $(COMMIT_TAG),$(COMMIT_TAG),$(COMMIT_HASH))
IMG    		:= $(NAME):$(TAG)
LATEST 		:= $(NAME):latest
PORT		:= $(if $(PORT),$(PORT),8080)

build:
	docker build -t $(IMG) .
	docker tag $(IMG) $(LATEST)
 
push:
	docker push $(IMG)
	docker push $(LATEST)

test:
	docker build -t plaas-testing -f Dockerfile.testing .
	docker run plaas-testing

run: build
	docker run -e PORT=$(PORT) -p $(PORT):$(PORT) plaas