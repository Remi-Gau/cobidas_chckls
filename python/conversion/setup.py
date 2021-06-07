from setuptools import setup, find_packages


def readfile(filename):
    with open(filename, "r+") as f:
        return f.read()


setup(
    name="conversion",
    version="2021.06.05",
    description="",
    packages=find_packages(),
    long_description=readfile("README.md"),
    author="Rémi Gau",
    author_email="remi.gau@gmail.com",
    url="",
    py_modules=["conversion"],
    license=readfile("LICENSE"),
    entry_points="""
        [console_scripts]
        ecobidas_convert=cli:convert
        ecobidas_responses=create_response_options:create_response_options
    """,
)
