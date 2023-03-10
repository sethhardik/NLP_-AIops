import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.1"

REPO_NAME = "NLP_-AIops"
AUTHOR_USER = "sethhardik"
SRC_REPO = "src"
AUTHOR_EMAIL = "hseth469@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER,
    author_email=AUTHOR_EMAIL,
    description="A small testing project for AIOPS understanding and DVC implementation.",
    long_description=long_description,
    long_description_content= "text/markdown",
    url=f"https://github.com/{AUTHOR_USER}/{REPO_NAME}",
    project_urls={
        "BUG Tracker": f"https://github.com/{AUTHOR_USER}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)   
