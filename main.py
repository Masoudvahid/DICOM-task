import os
import pydicom

def anonymize_file(file_path, output_path):
    # Load the DICOM file
    ds = pydicom.dcmread(file_path)

    # Delete the PatientName information
    ds.PatientName = ""
    
    # Save the anonymized DICOM file
    ds.save_as(output_path)

def transform_structure(src_dir, dst_dir):
    # Create a dictionary to map the source path to the destination path
    path_map = {}
    
    # Iterate through the files in the source directory
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            ds = pydicom.dcmread(file_path)
            
            # Get the values of the keys StudyInstanceUID, SeriesInstanceUID, and SOPInstanceUID
            study_uid = ds.StudyInstanceUID
            series_uid = ds.SeriesInstanceUID
            instance_uid = ds.SOPInstanceUID
            
            # Construct the path to the destination file
            dst_path = os.path.join(dst_dir, study_uid, series_uid, instance_uid + ".dcm")
            
            # Create the destination directory if it doesn't exist
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            
            # Anonymize the file and save it to the destination path
            anonymize_file(file_path, dst_path)
            
            # Add the mapping of the source path to the destination path to the dictionary
            path_map[file_path] = dst_path
    
    # Save the path mapping to a file
    with open("path_map.txt", "w") as f:
        for src_path, dst_path in path_map.items():
            f.write("{} -> {}\n".format(src_path, dst_path))

# Example usage
src_dir = "input"
dst_dir = "output"
transform_structure(src_dir, dst_dir)
