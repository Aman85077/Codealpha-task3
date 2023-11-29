import os
import shutil

def organize_files(source_dir):
    extensions = {
        '.jpeg': 'Images', '.jpg': 'Images', '.png': 'Images', '.gif': 'Images', '.bmp': 'Images',
        '.avi': 'Videos', '.flv': 'Videos', '.wmv': 'Videos', '.mov': 'Videos', '.mp4': 'Videos',
        '.doc': 'Documents', '.docx': 'Documents', '.pdf': 'Documents', '.txt': 'Documents',
        '.xls': 'Documents', '.xlsx': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents',
        '.mp3': 'Music', '.wav': 'Music', '.flac': 'Music', '.m4a': 'Music'
    }


    source_directory_path = os.path.join(source_dir, 'files')

    organized_directory_path = os.path.join(source_dir, 'organized_files')

    if not os.path.exists(organized_directory_path):
        os.makedirs(organized_directory_path)

    for folder in set(extensions.values()):
        if not os.path.exists(os.path.join(organized_directory_path, folder)):
            os.makedirs(os.path.join(organized_directory_path, folder))

    files = [f for f in os.listdir(source_directory_path) if os.path.isfile(os.path.join(source_directory_path, f))]

    for file in files:
        extension = os.path.splitext(file)[1].lower()
        if extension in extensions:
            folder = extensions[extension]
            source_file_path = os.path.join(source_directory_path, file)
            destination_file_path = os.path.join(organized_directory_path, folder, file)
            shutil.copy(source_file_path, destination_file_path)

    print("Files organized successfully in 'organized_files' directory!")

script_directory = os.getcwd()

organize_files(script_directory)
