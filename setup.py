from setuptools import setup, find_packages

def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version_string']

setup(
    name="plantuml",
    version=get_version('plantuml.py'),
    description="",
    long_description=open('README.rst').read(),
    url="https://github.com/dougn/python-plantuml/",
    author=plantuml.__author__,
    author_email=plantuml.__email__,
    license="BSD",
    py_modules=['plantuml'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['httplib2',],
    keywords=["plantuml", "uml"],
)
