# pyrpa

pyrpa lets Python control the Chrome browser, mouse and keyboard to automatic do jobs.

## Install

Before install package you should make sure OpenCV and python-tk is installed. Then install package by:

```
python3 setup.py install
```


### MacOS

You should install OpenCV and make sure python-tk is installed (for message box support).


Install OpenCV

```
brew install opencv
```

Install python-tk, for example your python version is 3.11:

```
brew install python@3.11 python-tk@3.11
```

### Ubuntu

You can just install python3-opencv to make sure OpenCV installed and then you should install scrot, xclip, xsel to support clipboard operation

```
sudo apt-get install -y python3-opencv python3-tk scrot xclip xsel
```

## System Design

pyrpa combines PyAutoGUI, pyperclip, selenium, OpenCV-Python, EasyOCR to do the RPA jobs.

* PyAutoGUI and pyperclip: control clipboard, mouse and keyboard operations.
* selenium: control Chrome browser.
* OpenCV-Python: provide graphic based operation.
* EasyOCR: provide OCR text position find feature.

## API

### Image related functions

| Function | Returns | Description |
| -------- | ------- |----------- |
| init\_img(element\_ratio=(1, 1)) | None | Initialize image identification base parameters. element\_ratio is define the element image resize ratio (width, height) |
| snap(fname=None) | None or Image object | Create screen snapshot. If fname setted will save screen snapshot to file. |
| find\_image\_element(element, pmode='center', debug=True, threshold=None) | found: bool, x: int, y: int | Find element image position at screen, return whether founded and position. pmode: position mode, `'center'` means return center position of element image, `'topleft'` means top left position; threshold: confidence threshold for image find, None means use system default (0.8). |
| find\_image\_element2(location, element, pmode='center', debug=True, threshold=None) | found: bool, x: int, y: int | Find element image position at screen with bigger location image found at screen, return whether founded and position. pmode: position mode; threshold: confidence threshold for image find. |
| scale\_find\_image(element, ratio\_from=0.2, ratio\_to=4, step=0.1, pmode='center', debug=True, threshold=None) | found: bool, x: int, y: int | Find element image with multi scale mode, return whether founded and position. ratio\_from: start scale ratio; ratio\_to: end scale ratio; step: ratio increase ratio; pmode: position mode; threshold: confidence threshold for image find.|
| click\_image(element, debug=True, threshold=None) | None | If element image founded in screen click it. Click position see `find_image_element` |
| click\_image2(location, element, debug=True, threshold=None) | None | If element image founded in screen click it. Click position see `find_image_element2` |
| exists\_image(element, debug=True, threshold=None) | found: bool | Return element image founded in screen. |
| exists\_image2(location, element, debug=True, threshold=None) | found: bool | Return element image founded in screen. |
| wait\_untile\_exists(element, next_op=None, max_wait=20, duration=1, debug=True, threshold=None) | None | Wait the element image exists in screen. next_op: operation that after element image founded, `None`: do nothing, `'click'`: click element, `'hover'`: move mouse over it, `'click_paste'`: click element and paste clipboard content; max\_wait: Check element image exists cycles; duration: if not found how many seconds it will wait; threshold: confidence threshold for image find. |
| wait\_untile\_exists2(location, element, next_op=None, max_wait=20, duration=1, debug=True, threshold=None) | None |  Wait the element image exists in screen. next_op: operation that after element image founded, `None`: do nothing, `'click'`: click element, `'hover'`: move mouse over it, `'click_paste'`: click element and paste clipboard content; max\_wait: Check element image exists cycles; duration: if not found how many seconds it will wait; threshold: confidence threshold for image find. |

### GUI related functions

| Function | Return | Description |
| -------- | ------ | ----------- |
| alert(text, title='Alert') | None | Show dialog with `OK` button and text content |
| confirm(text, title='Confirm') | bool | Show dialog with `OK` and `Cancel` button and text content, Return `True` if `OK` button clicked |
| clip(text) | None | Set clipboard content with text |
| write(text) | None | Type text |
| hotkey(*args) | None | Send combine key pressed. For example `Ctrl` + `V` is `hotkey('ctrl', 'v')` |
| paste() | None | Shot cuts with `Ctrl` + `V` |
| move(x, y) | None | Move mouse to position |
| click(x=None, y=None, clicks=1) | None | Perform mouse left button click, if `x` and `y` is setted, it will move the mouse to the position and then click; clicks: how many times button clicked, if double click just set it to `2`. |
| dclick(x=None, y=None) | None | Perform double click, if `x` and `y` is setted, it will move the mouse to the position first |
| rclick(x=None, y=None, clicks=1) | None | Perform mouse right button click, if `x` and `y` is setted,  it will move the mouse to the position and then click; clicks: how many times button clicked, if double click just set it to `2`. |
| mdown(x=None, y=None) | None | Press mouse left button, if `x` and `y` is setted it will move the mouse to the position first and then press the left button. |
| mup(x=None, y=None) | None | Release mouse left button, if `x` and `y` is setted it will move the mouse to the position first and then release the left button. |
| scroll(steps) | None | Scroll mouse wheel with steps |
| click\_and\_input(x, y, text) | None | Set the text to clipboard and then click the position and then perform `Ctrl` + `V`. |

### Chrome related functions
| Function | Return | Description |
| -------- | ------ | ----------- |
| chrome(profile\_dir=None, socks5\_proxy=None, size=(1266, 800), position=(0, 0), user\_agent=None) | Driver Object | Start Chrome browser and return Selenium driver object. profile\_dir: Chrome user data path; socks5\_proxy: socks5 proxy address; size: window size; position: window position; user\_agent: set User-Agent header. |
| switch\_tab(driver, idx=None, name='', url='', mode='contains') | None | Switch current tab. driver: Selenium driver object; idx: tab index; name: page title query; url: page url query; mode: query match mode, `contains` means name or url contains query, `equals` means name or url equals query. |
| new\_tab(driver, url='') | None | Create new tab and switch it to current. url: URL for new tab, empty means new blank tab. |
| tabs(driver) | List | List Chrome tabs info list |
| get\_new\_tabs(driver, origin\_tabs\_info) | List | Calculate new opened tabs different from `origin_tabs_info` |

> You can use `chrome` function returned driver object to perform more operations. For more details please read Selenium documents.
>
> `user_agent` can accept string or dict. There has 3 pre-defined User-Agent configuration `WINDOWS_UA`, `LINUX_UA`, `MACOS_UA`.
>
> The `user_agent` parameter dict fields:
>
> * user\_agent: string, required, user agent string
> * platform: string, required, `sec-ch-ua-platform` os name
> * version: string, optional, `sec-ch-ua-platform-version` os version
> * model: string, optional, `sec-ch-ua-model` information about device
> * mobile: boolean, optional, `sec-ch-ua-mobile` is mobile device

### OCR functions
| Function | Return | Description |
| -------- | ------ | ----------- |
| init\_ocr(langs=['en'], enable_gpu=False) | None | Initialize OCR system, setup languages and set whether enable CUDA |
| find\_ocr\_element(text, pmode='center', debug=True, threshold=None) | found: bool, x: int, y: int | Find `text` position at screen, return whether founded and position. pmode: position mode, `'center'` means return center position of text, `'topleft'` means top left position; threshold: confidence threshold for image find, None means use system default (0.8). |

### Misc functions
| Function | Return | Description |
| -------- | ------ | ----------- |
| init(screen\_ratio=(1, 1), enable\_ocr=False, ocr\_langs=['en'], enable\_gpu=False) | None | Initialize image and OCR system. screen\_ratio: define the element image resize ratio (width, height), see `init_img`; enable\_ocr: enable OCR system; ocr\_langs: OCR language; enable\_gpu: enable GPU for OCR system. |
| wait(secs=1) | None | Wait secs seconds |
| wait\_input(prompt='Input: ') | str | Wait console input |
| os_name() | str | Return OS name: `Linux`, `Darwin`, `Windows` |
| is_windows() | bool | Return is Windows |
| is_linux() | bool | Return is Linux |
| is_macos() | bool | Return is MacOS |

## Tips

* Input text: If some character cannot input by just type keyboard, please use clipboard to copy and paste to input box. For example, you can use `click_and_input` function.
* If button image will present more than one at screen, you can use `find_image_element2` to locate bigger image at screen and then find your element image in location image.
