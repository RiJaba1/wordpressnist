Ejecutar la aplicacion mediante Docker

* Creamos la imagen local en el equipo

docker build -t wordpressnist:latest container/.

* Copiamos el diccionario a usar a la carpeta montada en el container
* Si queremos usar el diccionario completo descargamos el fichero raw (no HTML)

wget https://raw.githubusercontent.com/hypn/custom-wordlists/refs/heads/master/wordpress-popular-plugins.txt -O app/diccionario.txt

* Podemos recortar el diccionario para pruebas rapidas mediante el comando sed

sed -i '51,$ d' app/diccionario.txt

* Ejecutamos el container con los parametros necesarios

```
docker run \
 --rm \
 -it \
 --name wpvulnapp \
 --mount type=bind,source="$(pwd)"/app,target=/usr/src/app \
 wordpressnist \
 -w diccionario.txt -u https://delicioushack.com
```

* El resultado se exporta a un fichero CSV en la carpeta /app con el nombre del dominio y el timestamp de la ejecucion
