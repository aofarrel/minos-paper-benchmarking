from setuptools import setup, find_packages


with open("requirements.txt") as f:
    install_requires = [x.rstrip() for x in f]

setup(
    name="minospb",
    version="0.1.0",
    description="Code for minos publication benchmarking",
    packages=find_packages(),
    author="Martin Hunt",
    author_email="mhunt@ebi.ac.uk",
    url="https://github.com/iqbal-lab-org/minos-paper-benchmarking",
    tests_require=["pytest"],
    entry_points={"console_scripts": ["minospb = minospb.__main__:main"]},
    install_requires=install_requires,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
)
