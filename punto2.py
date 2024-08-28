import logging
import pydicom
from pydantic import BaseModel, condecimal, conint, field_validator
from typing import Optional
import sys
import re

# Set up logging configuration to show info level messages with timestamps
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PatientRecord(BaseModel):
  # Define patient attributes with optional fields and specific validation rules
  name: Optional[str] = None
  age: Optional[conint(ge=0, le=120)] = None  # type: ignore # Age must be between 0 and 120
  birth_date: Optional[str] = None
  sex: Optional[str] = None
  weight: Optional[condecimal(gt=0, decimal_places=2)] = None  # type: ignore # Weight must be positive with up to 2 decimal places
  patient_id: Optional[str] = None
  patient_id_type: Optional[str] = None

  # Custom validator to ensure birth_date has the correct format if provided
  @field_validator('birth_date')
  def validate_birth_date(cls, v):
    if v is not None:
      # Validate that birth_date matches the YYYY-MM-DD format
      assert re.match(r'\d{4}-\d{2}-\d{2}', v), 'Invalid birth date'
    return v

  def get_patient_info(self):
    """Return a dictionary of patient information."""
    return {
      "Name": self.name,
      "Age": self.age,
      "Birth Date": self.birth_date,
      "Sex": self.sex,
      "Weight": self.weight,
      "Patient Id": self.patient_id,
      "Patient Id Type": self.patient_id_type
    }

  def set_patient_info(self, name=None, age=None, birth_date=None, sex=None, weight=None, patient_id=None, patient_id_type=None):
    """Set patient information attributes."""
    if name is not None:
      self.name = name
    if age is not None:
      self.age = age
    if birth_date is not None:
      self.birth_date = birth_date
    if sex is not None:
      self.sex = sex
    if weight is not None:
      self.weight = weight
    if patient_id is not None:
      self.patient_id = patient_id
    if patient_id_type is not None:
      self.patient_id_type = patient_id_type

class Diagnosis(PatientRecord):
  # Inherit from PatientRecord and add an optional diagnosis field
  diagnosis: Optional[str] = None

  def update_diagnosis(self, new_diagnosis: str):
    """Update the diagnosis and log the change."""
    old_diagnosis = self.diagnosis
    self.diagnosis = new_diagnosis
    logging.info(f"Diagnosis updated from '{old_diagnosis}' to '{new_diagnosis}'")

class StudyRecord(PatientRecord):
  # Add study-specific attributes
  modality: Optional[str] = None
  study_date: Optional[str] = None
  study_time: Optional[str] = None
  study_instance_uid: Optional[str] = None
  series_number: Optional[int] = None
  number_of_frames: Optional[int] = None

  def get_study_info(self):
    """Return a dictionary of study information."""
    return {
      "Modality": self.modality,
      "Study Date": self.study_date,
      "Study Time": self.study_time,
      "Study Instance UID": self.study_instance_uid,
      "Series Number": self.series_number,
      "Number of Frames": self.number_of_frames
    }

  def set_study_info(self, modality=None, study_date=None, study_time=None, study_instance_uid=None, series_number=None, number_of_frames=None):
    """Set study information attributes."""
    if modality is not None:
      self.modality = modality
    if study_date is not None:
      self.study_date = study_date
    if study_time is not None:
      self.study_time = study_time
    if study_instance_uid is not None:
      self.study_instance_uid = study_instance_uid
    if series_number is not None:
      self.series_number = series_number
    if number_of_frames is not None:
      self.number_of_frames = number_of_frames

class DICOMStudyLoader(StudyRecord):
  def __init__(self, **kwargs):
    # Initialize the parent class (StudyRecord) with provided keyword arguments
    super().__init__(**kwargs)

  def load_from_dicom(self, dicom_file_path: str):
    """Load study details from a DICOM file."""
    try:
      # Read the DICOM file
      dicom_file = pydicom.dcmread(dicom_file_path)
      # Extract and assign values from the DICOM file to the attributes
      self.name = dicom_file.PatientName if hasattr(dicom_file, 'PatientName') else None
      self.patient_id = dicom_file.PatientID if hasattr(dicom_file, 'PatientID') else None
      self.birth_date = dicom_file.PatientBirthDate if hasattr(dicom_file, 'PatientBirthDate') else None
      self.sex = dicom_file.PatientSex if hasattr(dicom_file, 'PatientSex') else None
      self.study_date = dicom_file.StudyDate
      self.study_time = dicom_file.StudyTime
      self.modality = dicom_file.Modality
      self.study_instance_uid = dicom_file.StudyInstanceUID
      self.series_number = dicom_file.SeriesNumber
      self.number_of_frames = dicom_file.NumberOfFrames if 'NumberOfFrames' in dicom_file else None
    except Exception as e:
      # Log an error if there is an issue reading the DICOM file
      logging.error(f"Error loading DICOM file: {e}")

  def __str__(self):
    """Return a string representation of the patient and study information."""
    patient_info = self.get_patient_info()
    study_info = self.get_study_info()
    # Combine patient and study information into a single dictionary
    combined_info = {**patient_info, **study_info}
    # Format the information into a string for display
    info_str = "\n".join([f"{key}: {value}" for key, value in combined_info.items()])
    return info_str

def main():
  """Main function to load a DICOM file and print the information."""
  # Get the path to the DICOM file from command-line arguments
  path = sys.argv[1]
  # Create an instance of DICOMStudyLoader
  dicom_loader = DICOMStudyLoader()

  # Load study details from the specified DICOM file
  dicom_loader.load_from_dicom(path)

  # Print the information about the patient and study
  print(dicom_loader)

if __name__ == '__main__':
  # Run the main function if this script is executed directly
  main()
