VENV = venv
PYTHON = $(VENV)\Scripts\python
PIP = $(VENV)\Scripts\pip

run: $(VENV)\Scripts\activate 
 $(PYTHON) main.py
 $(PYTHON) flask-restapi\run.py


$(VENV)\Scripts\activate : requirements.txt
 python3 -m venv $(VENV)
 $(PIP) install -r requirements.txt


clean:
 rm -rf __pycache__
 rm -rf $(VENV)