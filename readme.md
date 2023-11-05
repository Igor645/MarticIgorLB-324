# LB 324

## Aufgabe 2

Der Programmierer muss zwingend sicherstellen das er "pip install pre-commit" ausgeführt hat und so pre-commit auf seinem System hat. Dann muss er "pre-commit install" in seinem lokalen Git Repository ausführen, damit der pre-commit wirklich funktioniert.

## Aufgabe 4

Ich habe ein Docker Image auf Docker Hub hochgeladen auf diesem Repository:
https://hub.docker.com/repository/docker/marticigor646464/marticigorlb-324/general

Dieses Image konnte ich dann mithilfe von Render.com hosten. Die Seite ist unter dieser URL zu finden:
https://marticigorlb-324.onrender.com

mit dieser Zeile habe ich die .env variable mitgegeben:
ENV PASSWORD="einSehrGeheimesPasswort"
genau so hätte ich aber auch eine Environment Variable in Render.com erstellen können, was sehr wahrscheinlich die sicherere Variante wäre, da man mit dem weg, nicht das Passwort aus dem Code lesen kann.
