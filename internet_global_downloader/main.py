from tkinter import Button, font
from tkinter.constants import NONE, TRUE
from tkinter.font import Font
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import ColorChooserButton, Input, Window, theme_text_color
from pytube import YouTube
from time import sleep, time

def IGD():  #tela inicial
    sg.theme('DarkBrown4')
    layout = [
        [sg.Text('Youtube Downloader', font='Courier 16')],
        [sg.InputText(text_color='orange')],
        [sg.Button('Download')]
    ]
    return sg.Window('IGD', layout=layout, finalize=TRUE, element_justification='c')

def download_video_yt_720p():   #baixar video em 720p
    video = YouTube(link_yt)
    video.streams.get_by_itag(22).download()

janela1, janela2 = IGD(), None

while True:
    window, event, values = sg.read_all_windows()
    link_yt = (values[0])
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    else:
        download_video_yt_720p()
        sg.popup('Download Concluido!')
window.close()
