SHELL := /bin/bash

.PHONY: all test generate fmt

all: test

generate:
	INPUT_DIR=tools/aop/api/biz OUTPUT=api/biz/registry_static.go \
	python3 tools/generate.py

test:
	go test ./...

fmt:
	gofmt -w .

