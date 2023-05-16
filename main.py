from tkinter import *
from PIL import Image, ImageTk
import math
import matplotlib.pyplot as plt

#funkcje do edycji jednego obrazu
def negacja():
    global current_image, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))
    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r = 255 - r
            g = 255 - g
            b = 255 - b
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def jasnosc():
    global current_image, history
    current_image = current_image.point(lambda piksel: piksel + 50)
    history.append(current_image.copy())
    update_image()

def ciemnosc():
    global current_image, history
    current_image = current_image.point(lambda piksel: piksel - 50)
    history.append(current_image.copy())
    update_image()

def potega():
    global current_image, history
    current_image = current_image.point(lambda piksel: piksel ** 2)
    history.append(current_image.copy())
    update_image()


def pierwiastek():
    global current_image, history
    current_image = current_image.point(lambda piksel: int(math.sqrt(piksel)) ** 2)
    history.append(current_image.copy())
    update_image()

def kontrast():
    global current_image, history
    k = 2 #stopień kontrastu
    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r = int((r / 255 - 0.5) * k * 255 + 0.5)
            g = int((g / 255 - 0.5) * k * 255 + 0.5)
            b = int((b / 255 - 0.5) * k * 255 + 0.5)
            current_image.putpixel((i, j), (r, g, b))

    history.append(current_image.copy())
    update_image()

def roberts_pionowy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    maska = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    tmp_r += r * maska[k + 1][l + 1]
                    tmp_g += g * maska[k + 1][l + 1]
                    tmp_b += b * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    history.append(current_image.copy())
    update_image()


def roberts_poziomy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    maska = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    tmp_r += r * maska[k + 1][l + 1]
                    tmp_g += g * maska[k + 1][l + 1]
                    tmp_b += b * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    history.append(current_image.copy())
    update_image()


def prewitt_pionowy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    maska = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
    w, h = current_image.size
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            r = 0
            g = 0
            b = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    re, ge, be = img.getpixel((i + k, j + l))
                    r += re * maska[k + 1][l + 1]
                    g += ge * maska[k + 1][l + 1]
                    b += be * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (r, g, b))

    history.append(current_image.copy())
    update_image()


def prewitt_poziomy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    maska = [[1, 0, (-1)], [1, 0, (-1)], [1, 0, (-1)]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for k in range((-1), 2):
                for l in range((-1), 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    tmp_r += r * maska[k + 1][l + 1]
                    tmp_g += g * maska[k + 1][l + 1]
                    tmp_b += b * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    history.append(current_image.copy())
    update_image()


def sobel_pionowy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    maska = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for k in range(-1, 2):
                for l in range((-1), 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    tmp_r += r * maska[k + 1][l + 1]
                    tmp_g += g * maska[k + 1][l + 1]
                    tmp_b += b * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    history.append(current_image.copy())
    update_image()


def sobel_poziomy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    maska = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for k in range(-1, 2):
                for l in range((-1), 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    tmp_r += r * maska[k + 1][l + 1]
                    tmp_g += g * maska[k + 1][l + 1]
                    tmp_b += b * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    history.append(current_image.copy())
    update_image()


def laplace():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    maska = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for k in range(-1, 2):
                for l in range((-1), 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    tmp_r += r * maska[k + 1][l + 1]
                    tmp_g += g * maska[k + 1][l + 1]
                    tmp_b += b * maska[k + 1][l + 1]
            current_image.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    history.append(current_image.copy())
    update_image()


def minimum():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    stopien=1
    for i in range(w):
        for j in range(h):
            min_r, min_g, min_b = 255, 255, 255
            for x in range(max(0, i - stopien), min(w, i + stopien + 1)):
                for y in range(max(0, j - stopien), min(h, j + stopien + 1)):
                    r, g, b = img.getpixel((x, y))
                    min_r = min(min_r, r)
                    min_g = min(min_g, g)
                    min_b = min(min_b, b)
            current_image.putpixel((i, j), (min_r, min_g, min_b))

    history.append(current_image.copy())
    update_image()


def maksimum():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    stopien=1
    for i in range(w):
        for j in range(h):
            max_r, max_g, max_b = 0, 0, 0
            for x in range(max(0, i - stopien), min(w, i + stopien + 1)):
                for y in range(max(0, j - stopien), min(h, j + stopien + 1)):
                    r, g, b = img.getpixel((x, y))
                    max_r = max(max_r, r)
                    max_g = max(max_g, g)
                    max_b = max(max_b, b)
            current_image.putpixel((i, j), (max_r, max_g, max_b))

    history.append(current_image.copy())
    update_image()

def medianowy():
    global current_image, history
    img = Image.open("obraz.jpg")
    current_image = Image.new('RGB', (img.width, img.height))
    w, h = current_image.size
    r=2
    for i in range(w):
        for j in range(h):
            pixels = []
            for x in range(max(0, i - r), min(w, i + r + 1)):
                for y in range(max(0, j - r), min(h, j + r + 1)):
                    pixels.append(img.getpixel((x, y)))
            pixels.sort()
            median_r, median_g, median_b = pixels[len(pixels) // 2]
            current_image.putpixel((i, j), (median_r, median_g, median_b))

    history.append(current_image.copy())
    update_image()

#funkcje mieszania dwóch obrazów
def mieszanie_suma():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = min(r + r1, 255)
            g = min(g + g1, 255)
            b = min(b + b1, 255)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_odejmowanie():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = max(r - r1, 0)
            g = max(g - g1, 0)
            b = max(b - b1, 0)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_roznica():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = abs(r - r1)
            g = abs(g - g1)
            b = abs(b - b1)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_mnozenie():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))
    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = (r * r1) // 255
            g = (g * g1) // 255
            b = (b * b1) // 255
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_mnozenie_odw():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = (255 * r) // max(r1, 1)
            g = (255 * g) // max(g1, 1)
            b = (255 * b) // max(b1, 1)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_negacja():
    global current_image, image2, history
    obraz1 = current_image.convert("RGB")
    obraz2 = image2.convert("RGB")

    piksele1 = obraz1.load()
    piksele2 = obraz2.load()

    image_result = Image.new("RGB", (current_image.width, current_image.height))
    w, h = current_image.size
    for x in range(w):
        for y in range(h):
            r, g, b = piksele1[x, y]
            r2, g2, b2 = piksele2[x, y]
            a = 1 - abs(1 - r - r2) / 255.0
            b = 1 - abs(1 - g - g2) / 255.0
            c = 1 - abs(1 - b - b2) / 255.0
            r3 = int(255 * a)
            g3 = int(255 * b)
            b3 = int(255 * c)
            image_result.putpixel((x, y), (r3, g3, b3))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_ciemniejsze():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))
    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = r if r < r1 else r1
            g = g if g < g1 else g1
            b = b if b < b1 else b1
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_jasniejsze():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))
    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = max(r, r1)
            g = max(g, g1)
            b = max(b, b1)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_wylaczenie():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = r + r1 - 2 * r * r1 // 255
            g = g + g1 - 2 * g * g1 // 255
            b = b + b1 - 2 * b * b1 // 255
            image_result.putpixel((i, j), (r, g, b))

    current_image=image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_nakladka():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))

            a = r / 255
            b = r1 / 255
            if a < 0.5:
                r3 = 2 * a * b * 255
            else:
                r3 = (1 - 2 * (1 - a) * (1 - b)) * 255

            a = g / 255
            b = g1 / 255
            if a < 0.5:
                g3 = 2 * a * b * 255
            else:
                g3 = (1 - 2 * (1 - a) * (1 - b)) * 255

            a = b / 255
            b = b1 / 255
            if a < 0.5:
                b3 = 2 * a * b * 255
            else:
                b3 = (1 - 2 * (1 - a) * (1 - b)) * 255

            image_result.putpixel((i, j), (int(r3), int(g3), int(b3)))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_ostre_swiatlo():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))

            r = r + r1 - 2 * r * r1 // 255 if r1 < 128 else 2 * r * (255 - r1) // 255
            g = g + g1 - 2 * g * g1 // 255 if g1 < 128 else 2 * g * (255 - g1) // 255
            b = b + b1 - 2 * b * b1 // 255 if b1 < 128 else 2 * b * (255 - b1) // 255

            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_lagodne_swiatlo():
    import math

    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))

            # czerwony kanał
            if r1 < 128:
                r = 2 * r * r1 // 255 + r ** 2 * (255 - 2 * r1) // (255 * 255)
            else:
                r = math.sqrt(r / 255) * (2 * r1 - 255) + (2 * r - 255) * (255 - r1) // 255

            # zielony
            if g1 < 128:
                g = 2 * g * g1 // 255 + g ** 2 * (255 - 2 * g1) // (255 * 255)
            else:
                g = math.sqrt(g / 255) * (2 * g1 - 255) + (2 * g - 255) * (255 - g1) // 255

            # niebieski
            if b1 < 128:
                b = 2 * b * b1 // 255 + b ** 2 * (255 - 2 * b1) // (255 * 255)
            else:
                b = math.sqrt(b / 255) * (2 * b1 - 255) + (2 * b - 255) * (255 - b1) // 255
            image_result.putpixel((i, j), (round(r), round(g), round(b)))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def mieszanie_rozcienczenie():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = min(int(r / max(1 - b1, 0.01)), 255)
            g = min(int(g / max(1 - b1, 0.01)), 255)
            b = min(int(b / max(1 - b1, 0.01)), 255)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()


def wypalenie():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = 255 - (255 - r1) * 255 // max(1, r)
            g = 255 - (255 - g1) * 255 // max(1, g)
            b = 255 - (255 - b1) * 255 // max(1, b)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def reflect_mode():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))

    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = min(255, r ** 2 // max(1 - b1 / 255, 0.001))
            g = min(255, g ** 2 // max(1 - b1 / 255, 0.001))
            b = min(255, b ** 2 // max(1 - b1 / 255, 0.001))
            image_result.putpixel((i, j), (round(r), round(g), round(b)))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

def przezroczystosc():
    global current_image, image2, history
    image_result = Image.new("RGB", (current_image.width, current_image.height))
    alpha = 0.5
    w, h = current_image.size
    for i in range(w):
        for j in range(h):
            r, g, b = current_image.getpixel((i, j))
            r1, g1, b1 = image2.getpixel((i, j))
            r = int((1 - alpha) * r1 + alpha * r)
            g = int((1 - alpha) * g1 + alpha * g)
            b = int((1 - alpha) * b1 + alpha * b)
            image_result.putpixel((i, j), (r, g, b))

    current_image = image_result
    history.append(current_image.copy())
    update_image()

# histogram dla obrazu
def histogram():
    # pobranie składowych R, G, B
    r, g, b = current_image.split()

    # wygenerowanie histogramów składowych R, G, B
    plt.hist(r.histogram(), bins=256, color='red', alpha=0.5)
    plt.hist(g.histogram(), bins=256, color='green', alpha=0.5)
    plt.hist(b.histogram(), bins=256, color='blue', alpha=0.5)

    # ustawienie tytułu i etykiet osi
    plt.title('Histogram RGB')
    plt.xlabel('Wartość piksela')
    plt.ylabel('Liczba pikseli')

    plt.show()

def zapisz():
    global current_image
    current_image.save("aktualny_obraz.jpg")

# funkcja do aktualizacji wyświetlanego zdjęcia
def update_image():
    global current_image, photo, canvas, history
    photo = ImageTk.PhotoImage(current_image)
    canvas.itemconfigure(canvas_image, image=photo)
    # jeśli historia ma więcej niż 1 element to umożliwiamy cofnięcie ostatniej zmiany
    if len(history) > 1:
        menu.entryconfig("Cofnij", state="normal")
    else:
        menu.entryconfig("Cofnij", state="disabled")


# funkcja do cofania ostatniej zmiany
def cofnij():
    global current_image, photo, canvas, history
    # usuwamy ostatni wpis z historii i ustawiamy bieżące zdjęcie na poprzednie
    history.pop()
    current_image = history[-1]
    update_image()

image1 = Image.open('obraz.jpg')
image2 = Image.open('obraz2.jpg')

# GUI z menu
root = Tk()
root.geometry("%dx%d" % (image1.size[0] + 200, image1.size[1]))
root.title("Edytor zdjęć")

# wyświetlenie zdjęcia jako tła menu
canvas = Canvas(root, width=image1.size[0], height=image1.size[1])
canvas.pack(side=LEFT)
photo = ImageTk.PhotoImage(image1)
canvas_image = canvas.create_image(0, 0, anchor=NW, image=photo)

# tworzenie menu
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)

edit_menu = Menu(menu)
edit_mieszanie = Menu(menu)
menu.add_cascade(label="Edytuj", menu=edit_menu)
edit_menu.add_command(label="Negacja", command=negacja)
edit_menu.add_command(label="Rozjaśnij", command=jasnosc)
edit_menu.add_command(label="Przyciemnij", command=ciemnosc)
edit_menu.add_command(label="Zmiana potęgowa (2)", command=potega)
edit_menu.add_command(label="Zmiana pierwiastkowa (2)", command=pierwiastek)
edit_menu.add_command(label="Kontrast", command=kontrast)
edit_menu.add_command(label="Filtr Robertsa pionowy", command=roberts_pionowy)
edit_menu.add_command(label="Filtr Robertsa poziomy", command=roberts_poziomy)
edit_menu.add_command(label="Filtr Prewitta pionowy", command=prewitt_pionowy)
edit_menu.add_command(label="Filtr Prewitta poziomy", command=prewitt_poziomy)
edit_menu.add_command(label="Filtr Sobela pionowy", command=sobel_pionowy)
edit_menu.add_command(label="Filtr Sobela poziomy", command=sobel_poziomy)
edit_menu.add_command(label="Filtr Laplace'a", command=laplace)
edit_menu.add_command(label="Filtr minimum", command=minimum)
edit_menu.add_command(label="Filtr maksimum", command=maksimum)
edit_menu.add_command(label="Filtr medianowy", command=medianowy)

menu.add_cascade(label="Mieszanie", menu=edit_mieszanie)
edit_mieszanie.add_command(label="Mieszanie przez dodawanie", command=mieszanie_suma)
edit_mieszanie.add_command(label="Mieszanie przez odejmowanie", command=mieszanie_odejmowanie)
edit_mieszanie.add_command(label="Mieszanie przez roznice", command=mieszanie_roznica)
edit_mieszanie.add_command(label="Mieszanie przez mnożenie", command=mieszanie_mnozenie)
edit_mieszanie.add_command(label="Mieszanie przez mnożenie odwrotności", command=mieszanie_mnozenie_odw)
edit_mieszanie.add_command(label="Mieszanie przez negacje", command=mieszanie_negacja)
edit_mieszanie.add_command(label="Mieszanie ciemniejsze", command=mieszanie_ciemniejsze)
edit_mieszanie.add_command(label="Mieszanie jaśniejsze", command=mieszanie_jasniejsze)
edit_mieszanie.add_command(label="Mieszanie przez wyłączenie", command=mieszanie_wylaczenie)
edit_mieszanie.add_command(label="Mieszanie przez nakładkę", command=mieszanie_nakladka)
edit_mieszanie.add_command(label="Mieszanie przez ostre światło", command=mieszanie_ostre_swiatlo)
edit_mieszanie.add_command(label="Mieszanie przez łagodne światło", command=mieszanie_lagodne_swiatlo)
edit_mieszanie.add_command(label="Mieszanie przez wypalenie", command=wypalenie)
edit_mieszanie.add_command(label="Mieszanie przez rozcieńczenie", command=mieszanie_rozcienczenie)
edit_mieszanie.add_command(label="Mieszanie Reflect Mode", command=reflect_mode)
edit_mieszanie.add_command(label="Mieszanie przez przezroczystość", command=przezroczystosc)

menu.add_cascade(label="Histogram", command=histogram)

menu.add_cascade(label="Cofnij", command=cofnij, state="disabled")

menu.add_cascade(label="Zapisz obraz", command=zapisz)

# wyświetlenie początkowego zdjęcia w GUI
current_image = image1
history = [current_image.copy()]
update_image()

root.mainloop()