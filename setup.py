from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf8')
setup(
    name='myminixform',
    version='1.0.0',
    url="https://github.com/Mr-KAM/myminixform",
    homepage="https://github.com/Mr-KAM/myminixform",
    author='La centrale cognitive',
    author_email='lacentrale.cognitive@gmail.com',
    description='Un package python pour creer un formulaire XLSFORM à partir d\'un fichier .yaml',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires='>=3.6',
    install_requires=['pandas', 'openpyxl','humre','PyYAML'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)