# audioConvertor

audioConvertor is a multifile media format convertor command line tool. It allows conversion of files to various media types, the most emphasised on, being from video to audio.
The tool is a guide detailed out on [this blog post](https://medium.com/@mugoh.ks/python-click-building-your-first-command-line-interface-application-6947d5319ef7)

### Setup
1. Access a cloned copy of the repo
```shell
  $ git clone https://github.com/hogum/audioConvertor

```
2. Change to the repo directory
```shell
  $ cd audioConvertor
```
3. Optionally install ffmpeg. You can skip this step.

    Running the application for the first time will prompt for the installation.
```shell
    $ apt-get install ffmpeg
```

### Dependecies

1. Ensure to have pipenv installed
```shell
  $ apt install pipenv
```
2. Install the project dependencies by running
```shell
  $ pipenv install
```
- Alternatively, you can use a virtual environment with dependencies present by running
```shell
  $ pipenv shell
```

### Interacting with the application

#### Basic Usage
The usage options are accesible on the help menu. This can be displayed by running:

 ```shell
    $ python convertor/cli.py --help
 ```
    
1. Convert a video file to audio.
- Required Options

  - `--input_file -i` Path to video file
  

    ```shell
    $ python convertor/cli.py -i /path/to/video/file/ -o /save/path/
    ```


2. Convert mulitple video files from multiple directories

  ``` shell
  $ python convert -i /path/to/root/directory/ -o /path/to/save/output/ --recursive
  ```


### Testing
1. Spawn a virtual environment

```shell
  $ pipenv shell
```

2. Run tests
```shell
  $ pytest
```
