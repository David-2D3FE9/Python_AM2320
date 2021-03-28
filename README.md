
This forked repo get values from a AM2320 temperature and humidity sensor.  
A bug is corrected for negative values.  
It works on a I2C bus with Python3

Various examples added goes from simple `print()` to `sqlite3` record beside with cpu temperature.  

My personnal purpose of this repo is to monitor an outdoor rapsberry server in a case witch is supposed to stay watertight.  
I took some minutes to make the crontab working with a python script.  
The trick was to make a cd before the command and not trying to call everyrhing with the full path  

`*/1 * * * * cd /home/username/Python_AM2320 && /usr/bin/python3 ./Example_sqlite_complex.py`

Ce fork permet de lire les valeurs de température et d'humidité d'un capteur AM2320.  
Le bug pour les températures négatives est corrigé.  

Divers exemples on été ajoutés en lien avec mon application.  
Application qui vise à monitorer le taux d'humitidé dans le boitier d'un serveur raspberry installé en extérieur.

Le script est appelé par le crontab (ici toutes les minutes pour l'exemple).
