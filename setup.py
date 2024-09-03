import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-hide",
    version="0.0.4",
    author="Mohammad Etemaddar",
    author_email="mohammad.etemaddar@gmail.com",
    description="A Django package to obscure Django applications from detection tools like Wappalyzer by encrypting the CSRF token.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metemaddar/django_hide",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",  # Ensure compatibility with Django versions
    ],
    keywords="django security wappalyzer hide csrf",
    project_urls={
        "Documentation": "https://github.com/metemaddar/django_hide/blob/main/README.md",
        "Source": "https://github.com/metemaddar/django_hide",
        "Tracker": "https://github.com/metemaddar/django_hide/issues",
    },
)
