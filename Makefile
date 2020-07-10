bash:
	docker exec -it djangoplicity-products2 bash

test:
	docker exec -it djangoplicity-products2 coverage run --source='.' manage.py test

coverage-html:
	docker exec -it djangoplicity-products2 coverage html
	open ./htmlcov/index.html

test-python27:
	docker exec -it djangoplicity-products2 tox -e py27-django111
