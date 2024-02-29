pip3 install virtualenv
virtualenv -p python3 venv;
. venv/Bin/activate;
pip3 install -r requirements.txt;
pre-commit install;