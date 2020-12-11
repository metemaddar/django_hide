import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-hide", # Replace with your own username
    version="0.0.2",
    author="Mohammad Etemaddar",
    author_email="mohammad.etemaddar@gmail.com",
    description="Django Hide, hides django from wappalizer by encrypting csrf_token.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metemaddar/django_hide",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)