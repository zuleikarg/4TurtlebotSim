Projecto desarrollado por: [Zuleika María Redondo García]
# Sistema Multirobot de 4 Turtlebots en simulación

Repositorio de la práctica 1 de la asginatura de Sistemas Multirobot

## Requisitos
- ROS kinetic
- [Paquetes turtlebot 2] Para la realización de la simulación

## Instalación
- Creación de un workspace de ROS.
- Generación un nuevo paquete.
- Descarga de los archivos dentro del paquete.
- Compilación.

## Ejecución de movimientos coordinados sincronizados.

1. Asegurar que está descomentado la llamada al nodo "move_sync.py" en el archivo "one_robot.launch".
2. En el terminal lanzar el siguiente comando:
```sh
roslaunch <nombre_paquete> main.launch

## Ejecución de movimientos coordinados secuenciales.

1. Asegurar que está descomentado la llamada al nodo "move_sec.py" en el archivo "one_robot.launch".
2. En el terminal lanzar el siguiente comando:
```sh
roslaunch <nombre_paquete> main.launch
```


[Zuleika María Redondo García]: https://github.com/zuleikarg
[Paquete turtlebot 2]: https://github.com/turtlebot/turtlebot.git
