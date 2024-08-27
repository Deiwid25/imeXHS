import logging
import pydicom
from pydantic import BaseModel , condecimal, conint, field_validator
from typing import Optional
import sys
import re


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PatientRecord(BaseModel):
  name: Optional[str] = None
  age: Optional[conint(ge=0, le=120)] = None # type: ignore
  birth_date: Optional[str] = None
  sex: Optional[str] = None
  weight: Optional[condecimal(gt=0, decimal_places=2)] = None # type: ignore
  patient_id: Optional[str] = None
  patient_id_type: Optional[str] = None


  # Validador personalizado para asegurar que birth_date tenga el formato correcto si se proporciona
  @field_validator('birth_date')
  def validate_birth_date(cls, v):
    if v is not None:
      # Puedes agregar validaciones más robustas aquí, como verificar si la fecha es válida
      assert re.match(r'\d{4}-\d{2}-\d{2}', v), 'Fecha de nacimiento inválida'
    return v


  def get_patient_info(self):
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
  diagnosis: Optional[str] = None

  def update_diagnosis(self, new_diagnosis: str):
    old_diagnosis = self.diagnosis
    self.diagnosis = new_diagnosis
    logging.info(f"Diagnosis updated from '{old_diagnosis}' to '{new_diagnosis}'")

class StudyRecord(PatientRecord):
  modality: Optional[str] = None
  study_date: Optional[str] = None
  study_time: Optional[str] = None
  study_instance_uid: Optional[str] = None
  series_number: Optional[int] = None
  number_of_frames: Optional[int] = None

  def get_study_info(self):
    return {
      "Modality": self.modality,
      "Study Date": self.study_date,
      "Study Time": self.study_time,
      "Study Instance UID": self.study_instance_uid,
      "Series Number": self.series_number,
      "Number of Frames": self.number_of_frames
    }

  def set_study_info(self, modality=None, study_date=None, study_time=None, study_instance_uid=None, series_number=None, number_of_frames=None):
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
    super().__init__(**kwargs)

  def load_from_dicom(self, dicom_file_path: str):
    try:
      dicom_file = pydicom.dcmread(dicom_file_path)
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
      logging.error(f"Error loading DICOM file: {e}")

  def __str__(self):
    patient_info = self.get_patient_info()
    study_info = self.get_study_info()
    combined_info = {**patient_info, **study_info}
    info_str = "\n".join([f"{key}: {value}" for key, value in combined_info.items()])
    return info_str

def main():

  path = sys.argv[1]
  # Crear una instancia de DICOMStudyLoader
  dicom_loader = DICOMStudyLoader()
  
  # Cargar detalles del estudio desde un archivo DICOM
  dicom_loader.load_from_dicom(path)

  print(dicom_loader)

  #diagnostic


if __name__ == '__main__':
  main()