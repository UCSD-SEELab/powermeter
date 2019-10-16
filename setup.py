from setuptools import setup

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

SHORT_DESCRIPTION = (
    'Python module for HIOKI 3334 power meter in SEELab.'
)

VERSION = '2.0'

DEPENDENCIES = [
    'pyserial'
]

setup(
    name='powermeter',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=['powermeter'],
    python_requires='>=3.5.3',
    install_requires=DEPENDENCIES
)
