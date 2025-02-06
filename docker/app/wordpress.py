# -*- coding: utf-8 -*-

# Autor: RiJaba1
# Bajo Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional

import argparse
import sys
import requests
import re
import nvdlib
import pandas as pd
from tqdm import tqdm
import os.path
import time

# Argumentos del script
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", help="Especificar el diccionario a usar.", action="store", required=True)
parser.add_argument("-u", "--url", help="Especificar la URL del WordPress a escanear.", action="store", required=True)
args = parser.parse_args()

dominio = args.url.rstrip('/') if args.url.endswith('/') else args.url
dominio = dominio.replace("https://", "")
dominio = dominio.replace(".", "_")
timestr = time.strftime("%Y%m%d%H%M%S")
report = dominio + '_' + timestr + '.csv'

# Comprobar que la URL termina con una
base_url = args.url if args.url.endswith('/') else args.url + '/'

# Abrir el archivo con los plugins para su posterior tratamiento
try:
    with open(args.wordlist, "r", encoding="utf-8") as plugins_file:
        plugin_list = plugins_file.read().splitlines()
except:
    print("\nERROR: No se ha podido cargar el diccionario indicado -> " + args.wordlist)
    sys.exit(1)

# Mostrar información ingresada por el usuario
print("Diccionario: " + args.wordlist)
print("URL: " + args.url)

# Generación de endpoints
endpoints = [base_url + "wp-content/plugins/" + plugin for plugin in plugin_list]
plugins_validos = []

# Patrón que se usará para filtrar el plugin de la URL
pattern = r"/([^/]+)/?$"

# Comprobación de plugins existentes en la web
print("\nEscaneando plugins en los endpoints...")
for endpoint in tqdm(endpoints, desc="Comprobando plugins", unit="endpoint"):
    r = requests.get(endpoint)
    if r.status_code != 404:
        match = re.search(pattern, endpoint)
        if match:
            plugins_validos.append(match.group(1))

print("\nLista de plugins encontrados:", plugins_validos)

# Comprobación de los CVE de los plugin encontrados
print("\nBuscando vulnerabilidades para los plugins válidos en la API del NIST...")
print("\t[?] Nota: cada petición se realiza con 6 segundos de margen para evitar el Rate Limit")
vulnerabilities = {}
for plugin_valido in tqdm(plugins_validos, desc="Buscando CVEs", unit="plugin"):
    extraccion = nvdlib.searchCVE(keywordSearch=plugin_valido)
    todas_extracciones = []
    for eachCVE in extraccion:
        datito = (eachCVE.id, eachCVE.score[1] if eachCVE.score else None)
        todas_extracciones.append(datito)
    vulnerabilities[plugin_valido] = todas_extracciones
    time.sleep(6)

# Exportar el diccionario con las vulnerabilidades a un archivo Excel
def exportar_a_excel(vulnerabilities, archivo_excel):
    # Crear una lista de diccionarios para el DataFrame
    filas = []
    for plugin, cves in vulnerabilities.items():
        for cve_id, score in cves:
            filas.append({'Plugin': plugin, 'CVE ID': cve_id, 'Puntuación': score})
    # Crear el DataFrame
    df = pd.DataFrame(filas)
    # Exportar a Excel
    df.to_csv(archivo_excel, index=False)

# Llamar a la función para exportar los datos
#exportar_a_excel(vulnerabilities, args.export)
exportar_a_excel(vulnerabilities, report)

print("\nEl escaneo ha terminado. Los datos están disponibles en el archivo:", report)

sys.exit(0)
