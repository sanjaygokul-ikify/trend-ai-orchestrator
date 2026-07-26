# Makefile for AI Orchestrator

all: clean build install

clean:
    rm -rf build dist

build:
    poetry build

install:
    poetry install

run:
    python orchestrator.py

test:
    python -m unittest discover tests
