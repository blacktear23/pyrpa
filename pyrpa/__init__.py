from .gui import alert, confirm, prompt, clip, snap, write, hotkey, paste, move, click, dclick, rclick, mdown, mup, scroll, click_and_input, click_and_type
from .images import init_img, find_image_element, find_image_element2, scale_find_image, click_image, click_image2, exists_image, exists_image2, wait_untile_exists, wait_untile_exists2
from .utils import wait, wait_input, os_name, is_windows, is_linux, is_macos
from .chrome import start_chrome, switch_to_tab, create_new_tab, list_tabs, scroll_page, snap_page, WINDOWS_UA, LINUX_UA, MACOS_UA
from .ocr import init_ocr, find_ocr_element


# Initialize
def init(screen_ratio=(1, 1), enable_ocr=False, ocr_langs=['en'], enable_gpu=False):
    init_img(screen_ratio)
    if enable_ocr:
        init_ocr(ocr_langs, enable_gpu)


# Browser
def chrome(profile_dir=None, socks5_proxy=None, proxy=None, size=(1266, 800), position=(0, 0), user_agent=None, mobile_emulation=None):
    return start_chrome(profile_dir, socks5_proxy, proxy, size, position, user_agent, mobile_emulation)


def switch_tab(driver, idx=None, name='', url='', mode='contains'):
    switch_to_tab(driver, idx, name, url, mode)


def new_tab(driver, url=''):
    create_new_tab(driver, url)


def tabs(driver):
    return list_tabs(driver)


def get_new_tabs(driver, origin_tabs):
    new_tabs = list_tabs(driver)
    if len(new_tabs) <= len(origin_tabs):
        return []

    origin_ids = [item.get('targetId', '') for item in origin_tabs]

    ret = []
    for tab in new_tabs:
        if tab['targetId'] not in origin_ids:
            ret.append(tab)
    return ret


__all__ = [
    'init', 'init_img', 'init_ocr',
    'wait', 'wait_input', 'os_name', 'is_windows', 'is_linux', 'is_macos',
    'alert', 'confirm', 'prompt', 'clip', 'snap', 'write', 'hotkey', 'paste',
    'move', 'click', 'dclick', 'rclick', 'mdown', 'mup', 'scroll', 'click_and_input', 'click_and_type',
    'find_image_element', 'find_image_element2', 'scale_find_image',
    'click_image', 'click_image2', 'exists_image', 'exists_image2',
    'wait_untile_exists', 'wait_untile_exists2',
    'chrome', 'switch_tab', 'new_tab', 'tabs', 'get_new_tabs', 'scroll_page', 'snap_page', 'WINDOWS_UA', 'LINUX_UA', 'MACOS_UA',
    'find_ocr_element',
]
