from setuptools import setup


dependence = [
    'opencv-python',
    'pyautogui',
    'pyperclip',
    'selenium',
    'easyocr',
]

desc = 'pyrpa lets Python control the Chrome browser, mouse and keyboard to automatic do jobs.'

long_desc = '''pyrpa let Python control the Chrome browser, mouse and keyboard to automatic do jobs.
pyrpa is combine PyAutoGUI, pyperclip, selenium, OpenCV-Python to do the RPA jobs.

* PyAutoGUI and pyperclip: control clipboard, mouse and keyboard operations.
* selenium: control Chrome browser.
* OpenCV-Python: provide graphic based operation.
'''

version = '1.0.0'

setup(
    name='pyrpa',
    version=version,
    url='https://github.com/blacktear23/pyrpa',
    author='blacktear23',
    author_email='blacktear23@gmail.com',
    description=desc,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    license='BSD',
    packages=['pyrpa'],
    test_suite='tests',
    install_requires=dependence,
    keywords="automation rpa",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
