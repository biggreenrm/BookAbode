run:
	@docker-compose -f docker-compose.yml up

run_local:
	@poetry run flask run

build:
	@docker-compose -f docker-compose.yml build app db

clean:
	@docker-compose -f docker-compose.yml down --remove-orphans

psql:
	@docker-compose -f docker-compose.yml exec db psql --username=bookabode --dbname=bookabode
