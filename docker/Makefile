NS = twomelons
VERSION ?= latest

INSTANCE = default


.PHONY: build
build:
	docker build  --rm -t $(NS)/base:$(VERSION) 				base
	#docker build --rm -t $(NS)/java8:$(VERSION) 				java8
	#docker build --rm -t $(NS)/mongo:$(VERSION) 			    mongo
	#docker build  --rm -t $(NS)/cassandra:$(VERSION) 			cassandra
	#docker build  --rm -t $(NS)/postgresql:$(VERSION) 			postgresql
default: build

bash:
	docker exec -it $(id) bash