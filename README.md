# control_robot_raspi
Control de un robot por medio de Raspiberry con Python

Comandos para la instalacion

sudo su - 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install rpi-update

wget http://downloads.sourceforge.net/project/raspberry-gpio-python/RPi.GPIO-0.6.5.tar.gz
tar zxvf RPi.GPIO-0.6.5.tar.gz
cd RPi.GPIO-0.6.5/
sudo apt-get install python-dev
sudo python setup.py install

https://github.com/caloloc2/control_robot_raspi
cd control_robot_raspi
sudo python control.py (para ejecutar el programa)