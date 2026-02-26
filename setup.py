from setuptools import setup

setup(
    name='word_counter',
    version='0.1.0',
    py_modules=['word_count'],
    entry_points={'console_scripts': ['word-count=word_count:main']},
    install_requires=[],
    author='22yo Dev',
    description='Simple word counting script',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)