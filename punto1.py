import os
import sys
import csv
import pandas as pd
import logging


logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class FileOperations:
  @staticmethod
  def list_folder_contents(path):
    """lsita el contenido de una carpeta"""
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

  @staticmethod
  def read_csv_file(path,filename):
    """Lee un archivo csv y muestra información sobre columnas y datos numéricos"""
    try:
      file_path = os.path.join(path,filename)
      if os.path.exists(file_path):
        if filename.endswith('.csv'):
          df = pd.read_csv(file_path)
          print(f"Number of columns: {len(df.columns.tolist())}")
          print(f"Column names: {df.columns.tolist()}")
          numeric_columns = df.select_dtypes(include='number')
          num_rows, num_columns = df.shape
          print(f"Number of rows: {num_rows}")
          if not numeric_columns.empty:
            column_means = numeric_columns.mean()
            column_stds = numeric_columns.std()
            for col_name in numeric_columns.columns:
              mean_value = column_means[col_name]
              std_value = column_stds[col_name]
              print(f"{col_name}: Mean = {mean_value:.2f}, StdDev = {std_value:.2f}")
          else:
            logging.error("Non-numeric data encountered in the CSV file.")
        else:
          logging.error("No is the CSV file.")
      else:
        logging.error("Non exist file.")
    except Exception as e:
      logging.error(f"Error reading CSV file: {e}")


def main():
  if len(sys.argv) <3:
    print("Usage: python punto1.py <number[1-3]> <path> <filename>")
  try:
    fun = int(sys.argv[1])
    path = sys.argv[2]
    
    if fun == 1:
      FileOperations.list_folder_contents(path)
    elif fun == 2:
      filename = sys.argv[3]
      
      FileOperations.read_csv_file(path,filename)
    elif fun == 3:
      filename = sys.argv[3]
    else:
      raise Exception(f"The number is in 1 to 3.")
  except Exception as e:
    raise Exception(f"Error input folder: {e}")


if __name__ == '__main__':
  main()