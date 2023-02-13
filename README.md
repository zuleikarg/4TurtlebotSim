Projecto desarrollado por: [Zuleika María Redondo García]
# Sistema Multirobot de 4 *Turtlebots* en simulación

Repositorio de la práctica 1 de la asginatura de Sistemas Multirobot

## Requisitos
- ROS kinetic.
- [Paquetes turtlebot 2] para el uso de los turtlebots.
- [Paquetes turtlebot 2 simulación] para la simulación en gazebo.

## Instalación
- Estos códigos son **meramente visuales**.

## Ejecución de movimientos coordinados sincronizados.

1. Asegurar que está descomentado la llamada al nodo "move_sync.py" en el archivo "one_robot.launch".
2. En el terminal lanzar el siguiente comando:
```sh
roslaunch move_sync_sec main.launch
```

## Ejecución de movimientos coordinados secuenciales.

1. Asegurar que está descomentado la llamada al nodo "move_sec.py" en el archivo "one_robot.launch".
2. En el terminal lanzar el siguiente comando:
```sh
roslaunch move_sync_sec main.launch
```


[Zuleika María Redondo García]: https://github.com/zuleikarg
[Paquetes turtlebot 2]: https://github.com/turtlebot/turtlebot.git
[Paquetes turtlebot 2 simulación]: https://github.com/turtlebot/turtlebot_simulator
