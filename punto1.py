import os
import sys
import pandas as pd
import logging
import pydicom

# Configure logging to show errors with timestamps and log level
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class FileOperations:
  @staticmethod
  def list_folder_contents(path):
    """List the contents of a directory"""
    try:
      # Check if the given path is a directory
      if os.path.isdir(path):
        # List all items in the directory
        contents = os.listdir(path)
        print(f"Number of elements in '{path}': {len(contents)}")
        print("Contents:")
        # Print each item in the directory
        for item in contents:
          print(f"- {item}")
      else:
        # Raise an error if the path is not a directory
        raise NotADirectoryError(f"The path '{path}' is not a directory.")
    except Exception as e:
      # Print an error message if something goes wrong
      print(f"Error listing folder contents: {e}")

  @staticmethod
  def read_csv_file(path, filename):
    """Read a CSV file and display information about columns and numeric data"""
    try:
      # Construct the full file path
      file_path = os.path.join(path, filename)
      # Check if the file exists
      if os.path.exists(file_path):
        # Check if the file has a .csv extension
        if filename.endswith('.csv'):
          # Read the CSV file into a DataFrame
          df = pd.read_csv(file_path)
          # Print number of columns and column names
          print(f"Number of columns: {len(df.columns.tolist())}")
          print(f"Column names: {df.columns.tolist()}")
          # Select only numeric columns
          numeric_columns = df.select_dtypes(include='number')
          num_rows, num_columns = df.shape
          # Print number of rows
          print(f"Number of rows: {num_rows}")
          # If there are numeric columns, calculate and print statistics
          if not numeric_columns.empty:
            column_means = numeric_columns.mean()
            column_stds = numeric_columns.std()
            for col_name in numeric_columns.columns:
              mean_value = column_means[col_name]
              std_value = column_stds[col_name]
              print(f"{col_name}: Mean = {mean_value:.2f}, StdDev = {std_value:.2f}")
          else:
            # Log an error if no numeric data is found
            logging.error("Non-numeric data encountered in the CSV file.")
        else:
          # Log an error if the file is not a CSV file
          logging.error("The file is not a CSV file.")
      else:
        # Log an error if the file does not exist
        logging.error("File does not exist.")
    except Exception as e:
      # Log an error if something goes wrong while reading the file
      logging.error(f"Error reading CSV file: {e}")

  @staticmethod
  def read_dicom_file(path, filename, *tags):
    """Read a DICOM file and display metadata"""
    try:
      # Construct the full file path
      file_path = os.path.join(path, filename)
      # Check if the file exists
      if os.path.exists(file_path):
        # Check if the file has a .dcm extension
        if filename.endswith('.dcm'):
          # Read the DICOM file
          dicom_file = pydicom.dcmread(file_path)
          # Print patient name, study date, and modality
          print(f"Patient's Name: {dicom_file.PatientName}")
          print(f"Study Date: {dicom_file.StudyDate}")
          print(f"Modality: {dicom_file.Modality}")
          # Print values for specified DICOM tags
          for tag in tags:
            try:
              print(f"Tag {tag}: {dicom_file[tag].value}")
            except KeyError:
              # Log an error if the tag is not found in the DICOM file
              logging.error(f"Tag {tag} not found in the DICOM file.")
        else:
          # Log an error if the file is not a DICOM file
          logging.error("The file is not a DICOM file.")
      else:
        # Log an error if the file does not exist
        logging.error("File not found.")
    except Exception as e:
      # Log an error if something goes wrong while reading the file
      logging.error(f"Error reading DICOM file: {e}")

def main():
  # Print usage instructions
  print("")
  print("")
  print("")
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("Usage: python script_name.py <number[1-3]> <path> <filename> [<tag> ...]")
  print("Options:")
  print("  1: List the contents of a directory.")
  print("  2: Read a CSV file and show column details and statistics.")
  print("  3: Read a DICOM file and show metadata. Optionally, specify DICOM tags to display.")
  print("Examples:")
  print("  python punto1.py 1 /path/to/directory")
  print("  python punto1.py 2 /path/to/directory data.csv")
  print("  python punto1.py 3 /path/to/directory image.dcm (tag1 tag2 ...)")
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")
  print("")
  print("")
  
  # Check if there are enough command-line arguments
  if len(sys.argv) > 2:
    try:
      # Parse the function number and path from command-line arguments
      fun = int(sys.argv[1])
      path = sys.argv[2]
      # Execute the corresponding function based on the provided number
      if fun == 1:
        FileOperations.list_folder_contents(path)
      elif fun == 2:
        filename = sys.argv[3]
        FileOperations.read_csv_file(path, filename)
      elif fun == 3:
        filename = sys.argv[3]
        if len(sys.argv) < 5:
          FileOperations.read_dicom_file(path, filename)
        else:
          tags = sys.argv[4:]
          FileOperations.read_dicom_file(path, filename, tags)
      else:
        # Raise an error if the function number is not between 1 and 3
        raise ValueError("The number must be between 1 and 3.")
    except Exception as e:
      # Log an error if something goes wrong while processing input
      logging.error(f"Error processing input: {e}")
  else:
    # Print an error message if there are not enough arguments
    print("Error: Missing arguments.")
    print("Usage: python script_name.py <number[1-3]> <path> <filename> <tag> ...")

if __name__ == '__main__':
  main()
