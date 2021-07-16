#importamos la libreria
from music import *

s1_n = [Do, Re, ReS, Re, ReS, Sol, Re, Sol, Do, LaS, Do, ReS, LaS, Sol, SolS, ReS, Re, ReS]
s1_o = [5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 4, 4, 5, 5, 5]
s1_d = [B, B, dot(W), B, W, W, dot(R), W, dot(W), B, W, W, dot(R), W, W, B, W, W]

feed = [i for i in zip(s1_n, s1_o, s1_d)]

#iniciamos la fuente, 
#el primer argumento es una tupla que reprecenta el tempo, (figura, BPM)
#el segundo es una lista de listas, donde cada una tiene 3 valores, la nota, la octava, y la figura (duración)
s1 = MusicSource((B, 200), feed)


#iniciamos el reproductor
player = MusicPlayer()

#agregamos la fuente al reproductor
player.add_source(s1)

#reproduce todas las fuentes en conjunto
player.play()

