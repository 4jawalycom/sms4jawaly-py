from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sms4jawaly-py",
    version="1.0.2",
    author="4jawaly",
    author_email="support@4jawaly.com",
    description="Python SDK for sending SMS messages through the 4jawaly SMS Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4jawalycom/4jawaly.com_bulk_sms",
    project_urls={
        "Bug Tracker": "https://github.com/4jawalycom/4jawaly.com_bulk_sms/issues",
        "Documentation": "https://docs.4jawaly.com",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications :: Telephony",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=1.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
            "twine>=3.4",
            "build>=0.7.0",
        ],
    },
)
