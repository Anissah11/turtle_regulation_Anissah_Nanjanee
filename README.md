# Turtle Regulation - Anissah Nanjanee

Régulation d'une tortue TurtleSim en ROS2.

## Partie 1 : Régulation en cap

### Comportement selon Kp :

- Kp fort (ex: 8.0) : la tortue tourne très vite, 
  

- Kp faible (ex: 0.5) : la tortue tourne très lentement


- Kp choisi : 4.0 : la tortue s'oriente rapidement et précisément


## Partie 2 : Régulation en distance

### Comportement selon Kpl :

- Kpl fort (ex: 5.0) : la tortue avance très vite,
  elle peut dépasser le waypoint

- Kpl faible (ex: 0.1):  la tortue avance très lentement,
  met beaucoup de temps à arriver

- Kpl choisi : 0.3 : la tortue avance rapidement et s'arrête précisément au waypoint 


Lancer la simulation

Terminal 1 - TurtleSim:
bash
ros2 run turtlesim turtlesim_node


Terminal 2 - Nœud de régulation:
bash
ros2 run turtle_regulation set_way_point


Terminal 3 - Tracer un carré:
bash
ros2 run turtle_regulation square_client
