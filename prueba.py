import pydicom
import sys
def inspect_dicom_file(file_path):
    try:
        # Leer el archivo DICOM
        dicom_file = pydicom.dcmread(file_path)

        # Mostrar información general del archivo DICOM
        
        # Mostrar todos los tags disponibles
        print("\nDICOM Tags:")
        for tag in dicom_file.keys():
            try:
                value = dicom_file.get(tag)
                print(f"{tag}: {value}")
            except Exception as e:
                print(f"Error reading tag {tag}: {e}")

    except Exception as e:
        print(f"Error reading DICOM file: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    file_path = sys.argv[1] # Reemplaza con la ruta a tu archivo DICOM
    inspect_dicom_file(file_path)