import os
import sys


class FileOperations:
  @staticmethod
  def list_folder_contents(path):
    """lsitar el contenido de una carpeta"""
    try:
      if os.path.isdir(path):
        contents = os.listdir(path)
        print(f"number of elements in '{path}': {len(contents)}")
        print("contents:")
        for item in contents:
          print(f"- {item}")
      else:
        raise NotADirectoryError(f"The path '{path}' is not a directory.")
    except Exception as e:
      print((f"Error listing folder contents: {e}"))

if __name__ == '__main__':
  try:
    path = sys.argv[1]
    FileOperations.list_folder_contents(path)
  except Exception as e:
    print((f"Error input folder: {e}"))