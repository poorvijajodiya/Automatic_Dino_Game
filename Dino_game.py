import pyautogui
from PIL import ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def iscollide(data):
    #draw a rectangle for a birds
    for i in range(480, 570):
        for j in range(265, 295):
            if data[i, j] < 100:
                hit("down")
                return
    # draw a rectangle for a cactus
    for i in range(480, 570):
        for j in range(295, 336):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("dino game starts")
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)

        '''for i in range(480, 570):
            for j in range(295, 336):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(480, 570):
            for j in range(265, 295):
                data[i, j] = 171

        image.show()
        break'''