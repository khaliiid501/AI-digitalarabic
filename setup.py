#!/usr/bin/env python3
"""Setup configuration for AI-digitalarabic package."""

from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-digitalarabic",
    version="0.1.0",
    author="Khalid",
    author_email="khaliiid501@users.noreply.github.com",
    description="AI-powered Arabic language processing and digital transformation platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khaliiid501/AI-digitalarabic",
    project_urls={
        "Bug Tracker": "https://github.com/khaliiid501/AI-digitalarabic/issues",
        "Documentation": "https://github.com/khaliiid501/AI-digitalarabic/docs",
        "Source Code": "https://github.com/khaliiid501/AI-digitalarabic",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "Natural Language :: Arabic",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-digitalarabic=ai_digitalarabic.cli:main",
        ],
    },
    keywords="arabic nlp ai machine-learning text-processing",
    include_package_data=True,
    zip_safe=False,
)