from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="befunge-interpreter",
    version="0.1.0",
    author="lxweb102",
    author_email="lxweb102@gmail.com",
    description="Un intérprete para el lenguaje de programación esotérico Befunge-93",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lxweb102/Befunge-Interpreter",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
    ],
    keywords="befunge esoteric interpreter programming-language",
)
