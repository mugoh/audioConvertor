import click


def check_is_video(file_name):
    formats = ['flv', 'mp4', 'avi']

    return [extension for extension in
            formats if file_name.endswith(extension)]
