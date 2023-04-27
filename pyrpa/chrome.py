import os
import platform
from selenium import webdriver


def start_chrome(profile_dir=None, socks5_proxy=None, size=(1366, 768), position=(0, 0), user_agent=None):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', [
        'enable-automation',
        'disable-background-networking',
        'disable-default-apps',
        'disable-hang-monitor',
        'enable-blink-features',
        'no-service-autorun',
        'test-type',
        'use-mock-keychain',
    ])
    # Disable remember password feature
    opt.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
    })
    # Disable browser notification
    opt.add_argument('--disable-notifications')
    # Disable default browser check and confirm
    opt.add_argument('--no-default-browser-check')
    # Disable auto update check
    opt.add_argument("--simulate-outdated-no-au='Tue, 31 Dec 2099 23:59:59 GMT'")
    # Disable sec-ch-ua* headers for HTTP/2
    opt.add_argument('--disable-features=UserAgentClientHint')
    # If in linux and user is root just add --no-sandbox
    if platform.system() == 'Linux' and os.getlogin() == 'root':
        opt.add_argument('--no-sandbox')

    if user_agent is not None:
        opt.add_argument('--user-agent=%s' % user_agent)
    if position is not None:
        opt.add_argument('--window-position=%s,%s' % (position[0], position[1]))
    if size is not None:
        opt.add_argument('--window-size=%s,%s' % (size[0], size[1]))
    if profile_dir is not None:
        opt.add_argument('--user-data-dir=%s' % profile_dir)
    if socks5_proxy is not None:
        opt.add_argument('--proxy-server=socks5://%s' % socks5_proxy)
    c = webdriver.Chrome(options=opt)
    return c


def get(b, url):
    b.get(url)


def __check(src, dst, mode):
    print(src, dst, mode)
    if mode == 'contains':
        return dst in src
    elif mode == 'equals':
        return dst == src
    return False


# Switch to browser tab
# mode: contains, equals
def switch_to_tab(driver, idx=None, name='', url='', mode='contains'):
    hdls = driver.window_handles
    try:
        current_hdl = driver.current_window_handle
    except Exception:
        current_hdl = hdls[0]

    if idx is not None:
        if idx >= len(hdls):
            return
        driver.switch_to.window(hdls[idx])

    found = False
    if name != '':
        for hdl in hdls:
            driver.switch_to.window(hdl)
            if __check(driver.title, name, mode):
                found = True
                break

        if not found:
            driver.switch_to.window(current_hdl)
        return

    if url != '':
        for hdl in hdls:
            driver.switch_to.window(hdl)
            if __check(driver.current_url, url, mode):
                found = True
                break

        if not found:
            driver.switch_to.window(current_hdl)
        return


def create_new_tab(driver, url=''):
    driver.switch_to.new_window('tab')
    if url != '':
        driver.get(url)


if __name__ == '__main__':
    c = start_chrome(profile_dir='./profile-test')
    c.get('https://github.com')
    input('Continue?')
    c.close()
