# Comprobación de plugins de Wordpress en el NIST

Esta herramienta permite hacer un anális de plugins en un sitio web. Además, comprueba usando [la API del NIST](https://nvd.nist.gov/developers/vulnerabilities) los últimos CVE asociados a estos plugins.

## Uso

```
usage: wordpress.py [-h] [-v] -w WORDLIST -u URL -o EXPORT

options:
  -h, --help            show this help message and exit
  -w, --wordlist WORDLIST
                        Especificar el diccionario a usar.
  -u, --url URL         Especificar la URL del WordPress a escanear.
  -o, --export EXPORT   Especificar el archivo a exportar con los resultados.
```
* `-w`: archivo que contiene el nombre de los plugins a probar
* `-u`: URL principal del sitio Wordpress
* `-o`: archivo donde se volcará los plugins con sus vulnerabilidades

## Diccionarios

Recomiendo el diccionario "wordpress-popular-plugins.txt" de hypn. Enlace: https://github.com/hypn/custom-wordlists/blob/master/wordpress-popular-plugins.txt

## Licencia

Este script está licenciado bajo la Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional. Para ver una copia de esta licencia, visita https://creativecommons.org/licenses/by-nc-sa/4.0/.

## Agradecimientos

Gracias a ChatGPT por ayudarme a hacer la barra de progreso (😀)
Para cualquier cosa me podéis contactar por rijaba1@protonmail.com. ¡Gracias!
