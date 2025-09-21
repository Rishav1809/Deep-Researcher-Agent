import os

class FileLoader:
    @staticmethod
    def load_files(folder_path):
        files_data = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                filepath = os.path.join(folder_path, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                files_data.append({'filename': filename, 'text': content})
        return files_data
