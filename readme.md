# LB 324

## Aufgabe 2

Der Programmierer muss zwingend sicherstellen das er "pip install pre-commit" ausgeführt hat und so pre-commit auf seinem System hat. Dann muss er "pre-commit install" ausführen, damit der pre-commit wirklich funktioniert.

## Aufgabe 4

Ich habe auf Docker Hub ein Image hochgeladen, welches dauerhaft aktualisiert wird:
https://hub.docker.com/repository/docker/marticigor646464/marticigorlb-324/general

Um meine ENV variable auf docker zu übertragen brauch ich nur diese Zeile im Dockerfile:
ENV PASSWORD="einSehrGeheimesPasswort"
