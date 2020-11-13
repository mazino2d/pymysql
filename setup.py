from setuptools import setup, find_packages


if __name__ == "__main__":
    with open("requirements.txt", "r") as f:
        install_requires = map(lambda x: x.strip(), f.readlines())

    with open("README.md", "r") as f:
        long_description = f.read()

    setup(
        name="zcommon4py",
        version="1.0.0",
        license="MIT",
        author="Khoi Dang Do",
        author_email="mazino2d@gmail.com",
        url="https://github.com/mazino2d/zcommon4py",
        description="Modern utils library",
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords="utils",
        packages=find_packages(),
        install_requires=install_requires,
        python_requires=">=3.5, <4",
        entry_points={"console_scripts": ["zconfig = zcommon4py.config:main"]},
    )
