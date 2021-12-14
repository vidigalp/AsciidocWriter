from setuptools import setup

with open("README.md", "r") as fp:
    six_long_description = fp.read()

setup(
    name='asciidocwriter',
    version='0.0.1',
    packages=['AsciidocWriter'],
    url='https://github.com/vidigalp/asciidocwriter',
    license='',
    author='vidigalp',
    author_email='pedro.vidigal@instaclustr.com',
    description='Asciidoctor generator',
    long_description=six_long_description,
    long_description_content_type="text/markdown",
    install_requires = [
                           'numpy',
                           'pandas',
                           'python-dateutil',
                           'pytz',
                           'six',
                           'tqdm'
                       ],
)
