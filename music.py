import numpy as np
import math
import pyaudio
import io

gl_mult = 1

class MusicPlayer:
    """Clase que implementa la logica del reproductor"""
    def __init__(self):
        self.sources = list()
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(channels=1, rate=22050*gl_mult, format=pyaudio.paInt16, output=True)

    def add_source(self, source):
        """Agrega un objeto MusicSource al reproductor"""
        self.sources.append(source)

    def play(self):
        """Reproduce todos los MusicSources en conjunto"""
        by = b""
        loop = True

        for source in self.sources:
            source.feed()
        
        while loop:

            datas = list()

            for source in self.sources:
                try:
                    datas.append(source.feed_data.pop(0))
                except:
                    source.feed()
                    datas.append(source.feed_data.pop(0))

            n1 = len(datas)
            n2 = 0
            
            for i in datas:
                if i == None:
                    n2 += 1

            if n1 == n2:
                loop = False


            def normalizer(n):
                if n == None:
                    return 0
                else:
                    return n

            value = sum([normalizer(x) for x in datas])


            by += round(value).to_bytes(2, "big", signed=True)
            
            if len(by) >= 2048 or loop == False:
                self.stream.write(by)
                by = b""
    



class MusicSource:
    """Clase que define una fuente para usar con un MusicPlayer
    tempo: list(figura, BPM)
    data: lista(Nota, octava, figura) """
    def __init__(self, tempo, data):
        self.tempo = self.calc_tempo(tempo[0], tempo[1])
        self.data = iter(data)
        self.feed_data = list()

    @staticmethod
    def calc_tempo(fig, BPM):
        """Calcula el tempo de la fuente"""
        ms = 60000
        time = (ms/(fig*BPM))
        return time



    @staticmethod
    def frec(nota: int, octava: int):
        """Calcula la frecuencia del sonido en base a la frecuencia y la octava"""
        expo = octava * 12 + (nota - 58)
        return int(440 * ((2 ** (1/12)) ** expo))


    def feed(self):
        """Agrega datos a la lista interna para ser consumidos por el reproductor"""
        current = next(self.data, None)

        if current == None:
            self.feed_data.append(None)
        else:
            data = self.beep(current[0], current[1], current[2])
            self.feed_data += list(data)



    
    def beep(self, nota: int, octava: int, duracion: int):
        """Calcula y retorna todos los valores que componen la onda de sonido"""
        duracion = duracion * self.tempo
                                
        framerate = 22050*gl_mult
        
        frequency = self.frec(nota, octava)
        data = list()

        data=np.sin(2 * np.pi * np.arange(framerate*(duracion/1000))*frequency/framerate)*10 #########

        return data
        




def dot(fig):
    return fig + (fig/2)


#Valores de cada sonido

Do = 1
DoS = 2
Re = 3
ReS = 4
Mi = 5
Fa = 6
FaS = 7
Sol = 8
SolS = 9
La = 10
LaS = 11
Si = 12


#Valores de cada figura

SF = .0625
F = .125
SC = .25
C = .5
B = 1
W = 2
R = 4
