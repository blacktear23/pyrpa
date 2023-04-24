import cv2
import pyautogui
import numpy as np
from .images import THRESHOLD, SCREEN_HRATIO, SCREEN_WRATIO


EASYOCR_READER = None
OCR_ENGINE = 'easyocr'
TESSERACT_CONFIG = ''


def init_ocr(langs=['en'], enable_gpu=False, engine='easyocr', tesseract_config=''):
    global OCR_ENGINE
    if engine == 'easyocr':
        import easyocr
        global EASYOCR_READER
        OCR_ENGINE = 'easyocr'
        EASYOCR_READER = easyocr.Reader(langs, gpu=enable_gpu)
    elif engine == 'tesseract':
        import pytesseract
        global TESSERACT_CONFIG
        OCR_ENGINE = 'tesseract'
        tlangs = []
        for lang in langs:
            if lang == 'en':
                tlangs.append('eng')
            else:
                tlangs.append(lang)
        TESSERACT_CONFIG = '-l %s --oem 1 --psm 7' % ('+'.join(tlangs))
        if tesseract_config != '':
            TESSERACT_CONFIG += ' %s' % tesseract_config
    else:
        print('Alert: unknown OCR engine: %s' % engine)


def find_ocr_element(text, pmode='center', debug=True, threshold=None):
    if OCR_ENGINE == 'easyocr':
        return find_ocr_element_easyocr(text, pmode, debug, threshold)
    elif OCR_ENGINE == 'tesseract':
        return find_ocr_element_tesseract(text, pmode, debug, threshold)

    print('Alert: unknown OCR engine: %s' % OCR_ENGINE)
    return False, 0, 0


def find_ocr_element_easyocr(text, pmode='center', debug=True, threshold=None):
    if EASYOCR_READER is None:
        print('Alert: OCR system not initialized')
        return False, 0, 0

    if threshold is None:
        threshold = THRESHOLD

    pil_screen_img = pyautogui.screenshot()
    screen_np = np.array(pil_screen_img)
    screen_img = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
    result = EASYOCR_READER.readtext(screen_np)
    founds = []
    confi_max = 0
    found_max = None
    for line in result:
        box, rtext, confi = line[0], line[1], line[2]

        if len(box) < 4 or confi < threshold:
            continue

        if text in rtext:
            x, y = box[0][0], box[0][1]
            x2, y2 = box[-2][0], box[-2][1]
            w = int(x2 - x)
            h = int(y2 - y)
            item = [(int(x), int(y), w, h), rtext, confi]
            founds.append(item)
            if confi > confi_max:
                confi_max = confi
                found_max = item

    if debug:
        for f in founds:
            x, y, w, h = f[0]
            print('DEBUG: x = %s, y = %s, confidence = %s, text = %s' % (x, y, f[2], f[1]))
            cv2.rectangle(screen_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite('debug.png', screen_img)

    if found_max is None:
        return False, 0, 0

    x, y, w, h = found_max[0]
    if pmode == 'center':
        x = x / SCREEN_WRATIO + w / 2 / SCREEN_WRATIO
        y = y / SCREEN_HRATIO + h / 2 / SCREEN_HRATIO
    elif pmode == 'topleft':
        x = x / SCREEN_WRATIO
        y = y / SCREEN_HRATIO
    return True, int(x), int(y)


def find_ocr_element_tesseract(text, pmode='center', debug=True, threshold=None):
    import pytesseract
    if TESSERACT_CONFIG == '':
        print('Alert: OCR system not initialized')
        return False, 0, 0

    if threshold is None:
        threshold = THRESHOLD

    pil_screen_img = pyautogui.screenshot()
    screen_img = np.array(pil_screen_img)
    g_screen_img = cv2.cvtColor(screen_img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(g_screen_img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    founds = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = screen_img[y:y + h, x:x + w]
        rtext = pytesseract.image_to_string(cropped, config=TESSERACT_CONFIG)
        found_text = text.strip().replace(' ', '')
        if text in found_text:
            item = [(x, y, w, h), found_text, 0]
            founds.append(item)

    if debug:
        for f in founds:
            x, y, w, h = f[0]
            print('DEBUG: x = %s, y = %s, confidence = %s, text = %s' % (x, y, f[2], f[1]))
            cv2.rectangle(screen_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite('debug.png', screen_img)

    if len(founds) == 0:
        return False, 0, 0

    f = founds[0]
    x, y, w, h = f[0]
    if pmode == 'center':
        x = x / SCREEN_WRATIO + w / 2 / SCREEN_WRATIO
        y = y / SCREEN_HRATIO + h / 2 / SCREEN_HRATIO
    elif pmode == 'topleft':
        x = x / SCREEN_WRATIO
        y = y / SCREEN_HRATIO
    return True, int(x), int(y)
