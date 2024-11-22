# Inverter :arrows_clockwise:

**Inverter** es un script desarrollado en **Python** para la inversión de filas en un documento de texto, el cual está diseñado para procesar diferentes extensiones de archivos y codificaciones, así como para manejar archivos de texto pesados.

Este **script** se ha desarrollado pensando en el campo de la **ciberseguridad**, donde a la hora de querer ejecutar un **ataque de fuerza bruta** con un determinado diccionario empezando por el final, podemos darle la vuelta fácilmente en unos segundos, automatizando este proceso.

## Pre-requisitos 📋

Se necesitan importar las siguientes librerías:

* chardet
* os

La librería **os** viene instalada en el sistema por defecto con Python, pero **chardet** es necesaria instalarla. 

Se puede instalar así:
```bash
pip install chardet
```

## Uso y Funcionamiento del script ⚙️

### Uso ⌨️

El uso es muy sencillo, simplemente debemos iniciar el script:

```shell
python Inverter.py
```

Una vez iniciado, deberemos completar dos campos:

* Introduzca el nombre del archivo con su extensión -> Deberemos introducir el nombre del archivo que queremos invertir con su **ruta completa**.
* Indique el nombre del nuevo archivo invertido con su extensión -> Deberemos introducir el nombre que queramos ponerle al nuevo archivo creado con el contenido del anterior ya invertido.

### Ejemplo de uso 📖

A continuación, tiene una imagen de ejemplo de uso del **script** donde se invierte el archivo *rockyou.txt* y se crea el nuevo archivo llamado *rockyou_invertido.txt*:

![inverter](/Captura/Inverter.png)

### Funcionamiento 🔩

1. Limpia la terminal en función del sistema operativo.

2. Recoge los inputs introducidos por el usuario, tanto el nombre del archivo elegido, como el del nuevo archivo a crear.

3. Comprueba si la extensión de los archivos son válidas.

4. Detecta la codificación del archivo seleccionado.

5. Lee el archivo seleccionado con la codificación pertinente.

6. Realiza el proceso de inversión del archivo y lo escribe en un nuevo archivo con el nombre seleccionado para él.

7. Aporta feedback al usuario acerca del proceso.

Si desea obtener más información acerca del **script**, puede consultar los **comentarios** en el código del mismo.

## Autor ✒️

* Autor del código: [Javier Chamorro Salas](https://github.com/hypnopompicman)

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles.