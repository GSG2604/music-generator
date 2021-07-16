# music-generator
Un script para hacer musica

Este script te permite "generar" música utilizando **pyaudio** y **numpy**

Para usarlo basta seguir el ejemplo que dejé (example.py)

##Limitaciones:
Antes de usar pyaudio estaba usando audiostream en android con la app pydroid, por lo que hice que la configuración de uno y otro fueran compatibles asi que de seguro no está bien optimizada.

##Por hacer:
* Permitir el ajuste del volumen de cada fuente.
* Generar mas de una nota al mismo tiempo en la misma fuente.
* Agregar soporte para los silencios.
* Guardar en archivos de audio.

##Funcionamiento:
De forma simple se puede decir que el script genera ondas sinusoidales de determinada frecuencia las cuales luego son emitidas por la salida de audio de tu pc. 
