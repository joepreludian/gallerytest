PYTHON=env/bin/python
PIP=env/bin/pip

clean:
	find . -name "*.pyc" -delete

deps:
	virtualenv env;
	$(PIP) install -r requirements.pip;

setup: clean deps
	rm -rf *.sqlite3;
	@echo "Instalando banco de dados...";
	$(PYTHON) manage.py syncdb --noinput;
	$(PYTHON) manage.py migrate;
	
	@echo "Criando um usuario do administrativo...";
	@$(PYTHON) manage.py createsuperuser \
		--email "joepreludian@gmail.com";
	@echo "Setup finalizado. Para rodar o projeto, digite \"make run\""
run:
	$(PYTHON) manage.py test;
	$(PYTHON) manage.py runserver 0.0.0.0:8000;




