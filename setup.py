import setuptools


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

REQUIRED = read_requirements('requirements.txt')
PACKAGES = setuptools.find_packages(exclude=('tests',))
PACKAGES.append('douyin_spider.utils.decryption')

setuptools.setup(
    name="douyin_spider",
    version="0.0.1",
    author="Jerry_suye",
    author_email="jerry_suye@163.com",
    description="One simple and easy to use crawler for DouYin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErisYoung/douyin_spider",
    packages=PACKAGES,
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
