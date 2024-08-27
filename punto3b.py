import json
import sys
import os
import logging
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor
from pydantic import BaseModel

# Define the data model with Pydantic
class DataItem(BaseModel):
  id: str
  data: List[str]
  deviceName: str

def read_and_validate_json(json_file_path: str) -> Dict[str, DataItem]:
  """Read and validate JSON file, returning a dictionary of DataItem objects."""
  with open(json_file_path, 'r') as f:
    data = json.load(f)

  validated_data = {}
  for key, value in data.items():
    validated_data[key] = DataItem(**value)  # Validate using Pydantic
  return validated_data

# Configure logging for thread-safe operations
def setup_logging(log_file_path: str):
  """Set up logging to both file and console."""
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(message)s',
    handlers=[
      logging.FileHandler(log_file_path),
      logging.StreamHandler()
    ]
  )

def process_data_item(data_item: DataItem):
  """Process each DataItem: normalize data, calculate and log statistics."""
  logging.info(f"Processing ID: {data_item.id}")

  # Convert data strings to lists of integers
  data_values = []
  for line in data_item.data:
    data_values.extend(map(int, line.split()))

  # Calculate the average before normalization
  average_before = sum(data_values) / len(data_values)
  logging.info(f"Average before normalization for ID {data_item.id}: {average_before}")

  # Normalize the data
  max_value = max(data_values)
  normalized_data = [x / max_value for x in data_values]

  # Calculate the average after normalization
  average_after = sum(normalized_data) / len(normalized_data)
  logging.info(f"Average after normalization for ID {data_item.id}: {average_after}")

  # Size of the data
  data_size = len(data_values)
  logging.info(f"Data size for ID {data_item.id}: {data_size}")

def main(path: str):
  """Main function to process the JSON file and manage threading."""
  json_file_path = path
  log_file_path = os.path.join('.', 'processing.log')

  # Set up logging
  setup_logging(log_file_path)

  # Read and validate the JSON file
  data_items = read_and_validate_json(json_file_path)

  # Create a ThreadPoolExecutor with a maximum of 4 threads
  with ThreadPoolExecutor(max_workers=4) as executor:
    futures = []
    for key, item in data_items.items():
      # Submit each task to the executor
      futures.append(executor.submit(process_data_item, item))

    # Wait for all threads to complete
    for future in futures:
      future.result()

  logging.info("All threads have finished processing.")

if __name__ == '__main__':
  path = sys.argv[1]
  main(path)
