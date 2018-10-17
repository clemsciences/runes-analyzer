from setuptools import setup

setup(
    name='runesanalyzer',
    version='1.0.3',
    packages=['runesanalyzer'],
    url='https://github.com/clemsciences/runes-analyzer',
    license='MIT',
    author='Clément Besnier',
    author_email='clemsciences@gmail.com',
    description='Gathers different kinds of runic inscriptions',
    install_requires=['requests', 'lxml'],
    long_description='Runic alphabets: elder futhark, younger futhark, short-twig younger futhark. '
                     'Rune representation, phonetic transcription and ',

)
