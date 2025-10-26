TRAP := trap 'docker compose --profile "*" down --remove-orphans' EXIT INT TERM
DC := $(TRAP); DEV=$(DEV) docker compose run --rm
DC_BENCH := $(TRAP); DEV=$(DEV) docker compose --profile bench run --rm

build:
	docker compose build

test:
	$(DC) test

app:
	$(DC) app

bench:
	$(DC_BENCH) bench
	$(MAKE) plot

plot:
	$(DC) test python3 /app/scripts/plot.py

dist: clean test
	$(DC) test python -m build

pubtest:
	$(DC) test twine upload --verbose -r testpypi dist/*

publish:
	$(DC) test twine upload dist/*

clean:
	$(DC) test rm -rf ./dist *.egg-info/
