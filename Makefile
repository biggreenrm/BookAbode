run:
	@docker-compose -f docker-compose.yml up

run_local:
	@poetry run flask run

build:
	@docker-compose -f docker-compose.yml build app

clean:
	@docker-compose -f docker-compose.yml down --remove-orphans
