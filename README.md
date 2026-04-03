# Turtle Regulation - Anissah Nanjanee

Régulation d'une tortue TurtleSim en ROS2.

## Partie 1 : Régulation en cap

### Comportement selon Kp :

- Kp fort (ex: 8.0) : la tortue tourne très vite, 
  

- Kp faible (ex: 0.5) : la tortue tourne très lentement


- Kp choisi : 2.0 : la tortue s'oriente rapidement et précisément


## Partie 2 : Régulation en distance

### Comportement selon Kpl :

- Kpl fort (ex: 5.0) : la tortue avance très vite,
  elle peut dépasser le waypoint

- Kpl faible (ex: 0.3):  la tortue avance très lentement,
  met beaucoup de temps à arriver

- Kpl choisi : 1.5 : la tortue avance rapidement et s'arrête précisément au waypoint 
