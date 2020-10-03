from setuptools import setup

setup(
    name    = "c2nasm",
    version = "0.4",
    description = "paquete mamalon",
    author  = "David Gutierrez Alvarez",
    author_email = "none",
    license= "MIT",
    url     = "https://github.com/davidga1996/c2nasm",
    packages = ["c2nasm"],
    entry_points = {
        'console_scripts': [
            'nasm=c2nasm.__main__:run'
        ],
    },
)


#python setup.py sdist
#pip install .\c2nasm-0.1.tar.gz

#python setup.py install
