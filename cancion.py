from music import *

s1_n = [Do, Re, ReS, Re, ReS, Sol, Re, Sol, Do, LaS, Do, ReS, LaS, Sol, SolS, ReS, Re, ReS]
s1_o = [5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 4, 4, 4, 5, 5, 5]
s1_d = [B, B, dot(W), B, W, W, dot(R), W, dot(W), B, W, W, dot(R), W, W, B, W, W]

feed = [i for i in zip(s1_n, s1_o, s1_d)]


s1 = MusicSource((B, 200), feed)



player = MusicPlayer()

player.add_source(s1)





player.play()

