import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skyscrapers-Olena-Karaim",
    version="0.0.1",
    author="Olena Karaim",
    author_email="olena.karaim@ucu.edu.ua",
    description="Skyscrapers is a program that checks if the game board is compliant with the rules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)