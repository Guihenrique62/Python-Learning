import pygame
import time

def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Aguarde a reprodução terminar
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"Erro ao reproduzir o arquivo MP3: {e}")
    finally:
        pygame.mixer.quit()

play_mp3('audio.mp3')