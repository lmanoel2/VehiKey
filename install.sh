sudo apt install python3-pip;
sudo apt-get update;
sudo apt install pre-commit
sudo apt-get install gcc python3-dev;
sudo apt-get update;
sudo apt-get install libgl1-mesa-glx;
pip3 install virtualenv;
virtualenv -p python3 venv;
. venv/bin/activate;
pip3 install -r requirements.txt;
pre-commit install;
sudo apt-get update;