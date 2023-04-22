from .gui import *
from .images import *
from .utils import *
from .chrome import start_chrome, switch_to_tab, create_new_tab


# Browser
def chrome(profile_dir=None, socks5_proxy=None, size=(1266, 800), position=(0, 0)):
    return start_chrome(profile_dir, socks5_proxy, size, position)


def switch_tab(driver, idx=None, name='', url='', mode='contains'):
    switch_to_tab(driver, idx, name, url, mode)


def new_tab(driver, url=''):
    create_new_tab(driver, url)


__all__ = [
    'init', 'wait', 'wait_input', 'os_name', 'is_windows', 'is_linux', 'is_macos',
    'alert', 'confirm', 'clip', 'snap', 'write', 'hotkey', 'paste',
    'move', 'click', 'dclick', 'rclick', 'mdown', 'mup', 'scroll', 'click_and_input',
    'find_image_element', 'find_image_element2', 'scale_find_image',
    'click_image', 'click_image2', 'exists_image', 'exists_image2',
    'wait_untile_exists', 'wait_untile_exists2',
    'chrome', 'switch_tab', 'new_tab',
]
