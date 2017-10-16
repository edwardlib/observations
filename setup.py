from setuptools import setup

# import ``__version__`` from code base
exec(open('observations/version.py').read())

setup(
    name='observations',
    version=__version__,
    description='Tools for loading standard data sets in machine learning',
    author='Dustin Tran',
    author_email="dustin@cs.columbia.edu",
    packages=['observations', observations.r],
    install_requires=['numpy>=1.7',
                      'six>=1.10.0'],
    extras_require={
        'data frames': ['pandas'],
        'networks': ['networkx<=1.9.1'],
        'miscellaneous': ['scipy', 'requests', 'tqdm']},
    url='https://github.com/edwardlib/observations',
    keywords='machine learning statistics data science deep education',
    license='Apache License 2.0',
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: POSIX :: Linux',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4'],
)
