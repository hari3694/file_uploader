from setuptools import find_packages, setup

with open("file_uploader/README.md", "r") as f:
    long_description = f.read()

setup(
    name="file_uploader",
    version="0.0.10",
    description="A package for uploading files to S3 and GCS",
    package_dir={"": "app"},
    packages=find_packages(where="file_uploader"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Hari Sankar",
    author_email="harisankar4001@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["boto3 >= 1.26.145"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.9",
)