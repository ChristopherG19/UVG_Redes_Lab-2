# UVG_Redes_Lab-2

En el presente laboratorio se trabajaron los conceptos de esquemas de detección y corrección de errores. En el reporte de este laboratorio se encuentra toda la información necesaria para comprender los algoritmos implementados, los resultados obtenidos y tanto la discusión como las conclusiones de lo resultante. En este readme encontrarás los pasos necesarios para ejecutar ambos algoritmos.

Ambos programas siguen el modelo de: emisor escrito en java y receptor escrito en python. Para generar las cadenas provenientes del emisor se debe correr el archivo llamado:
```
Principal.java
```
Este se encarga de la generación de los .txt que almacenan las cadenas resultantes y que serán leídas en el receptor correspondiente.

Código de Hamming:
- Para este código se trabajó con el archivo:
  ```
  mainHam.py
  ```
  Este archivo lee el archivo generado por el emisor con la cadena resultante, la procesa, determina si hay errores o no y de haberlos retorna el bit que dio flip y corrige el mensaje retornando la trama correcta.

Algoritmo CRC-32:
- Para este algoritmo se trabajó con el archivo:
  ```
  mainCRC.py
  ```
  Este archivo al igual que el anterior, lee el archivo generado por el emisor con la cadena resultante, la procesa, determina si hay errores o no y de haberlos retorna el bit que dio flip y corrige el mensaje retornando la trama correcta.

Al correr el emisor se solicitará una cadena de ceros y unos, de no ser correcta no me permite correr los algoritmos y espera la cadena correcta y en caso contrario procede a crear los .txt y procesar todo con las clases emisor. Posteriormente si se corren los main de los receptores únicamente se pide correr el programa como tal y se procesa todo de forma automática.
