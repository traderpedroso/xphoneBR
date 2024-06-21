from setuptools import setup, find_packages

long_description = """XphoneBR is a portuguese transformer base grapheme-to-phoneme normalization  tool modeling library that leverages recent deep learning 
technology and is optimized for usage in production systems such as TTS. In particular, the library should
be accurate, fast, easy to use. 

DeepPhonemizerBR is compatible with Python 3.6+ and is distributed under the MIT license.

"""
# Version: 0.0.6
setup(
    name="xphonebr",
    version="0.0.6",
    author="Emerson Pedroso",
    author_email="traderpedroso@icloud.com",
    description="Grapheme to phoneme conversion and tools for tts with deep learning.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="MIT",
    install_requires=[
        "tqdm>=4.38.0",
        "deep-phonemizer==0.0.19",
        "num2words==0.5.12",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    package_data={"": ["*.yaml"]},
)
