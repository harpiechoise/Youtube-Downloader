#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pafy
import os
def obtenerAudio(video='', link='', playlist=False):
    if playlist == False:
        video = pafy.new(link)
    
    audio = video.audiostreams
    for i in audio:
        if i.extension == 'm4a':
            f = i.download()
            return f
    
def convertirAMp3(f):
    path = os.getcwd()
    inAudio = os.path.join(path, f)
    outAudio = os.path.join(path, 'output' ,f.split('.')[0] + '.mp3')
    os.system('clear')
    print('''ffmpeg -i {} {}'''.format(inAudio, outAudio))
    os.system('''ffmpeg -i "{}" "{}"'''.format(inAudio, outAudio))
    os.remove(inAudio)

def descargarLista(link):
    playlist = pafy.get_playlist(link)
    for video in playlist['items']:
        file_name = obtenerAudio(video=video['pafy'], playlist=True)
        convertirAMp3(file_name)


def cli():
    print('Que deseas Hacer?\n1 .Descargar Video\n2. Descargar Playlist')
    op = input('Ingrese La Opcion [1-2]: ')
    if op == "1":
        link = input('Pegue la url de un video: ')
        print(link)
        file_name = obtenerAudio(link=link)
        convertirAMp3(file_name)
    if op == "2":
        link = input('Pegue la url de una playlist: ')
        descargarLista(link)

if __name__ == '__main__':
    cli()