import setuptools

with open("README.md", "r") as fp:
    alt_description = fp.read()


setuptools.setup(
    name="convertor-mugoh",
    version="0.0.1",
    author="mugoh",
    description="A video to audio convertor",
    long_decsription=alt_description,
    long_decsription_content_type="text/markdown",
    url="https://github.com/hogum/audioConvertor",
    packages=['convertor']
    classifers=["Programming Language :: Python :: 3",
                "Licence :: Apache GPL 2",
                ],
)
