bash:
	docker exec -it djangoplicity-products2 bash

test:
	docker exec -it djangoplicity-products2 coverage run --source='.' manage.py test

coverage-html:
	docker exec -it djangoplicity-products2 coverage html
	open ./htmlcov/index.html

test-python27:
	docker exec -it djangoplicity-products2 tox -e py27-django111

test-python27:
	docker exec -it djangoplicity-products2 tox -e py27-django111

migrate:
	docker exec -it djangoplicity-products2 python manage.py migrate

makemigrations:
	docker exec -it djangoplicity-products2 python manage.py makemigrations

futurize-stage1:
	docker exec -it djangoplicity-products2 futurize --stage1 -w -n .

futurize-stage2:
	docker exec -it djangoplicity-products2 futurize --stage2 --nofix=newstyle -w -n .
