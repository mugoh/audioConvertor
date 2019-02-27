# audioConvertor

audioConvertor is a multifile media format convertor command line tool. It allows conversion of files to various media types, the most emphasised on, being from video to audio.

#### Interacting with the application
##### Usage
1. Convert a video file to audio.
- Required Options

  - `--input_file -i` Path to video file
  

    `audio3 convert -i /path/to/video/file/`


2. Convert mulitple video files from multiple directories

  ``` shell
  $ audio3 convert -i /path/to/root/directory/ -o /path/to/save/output/ -r
  ```


