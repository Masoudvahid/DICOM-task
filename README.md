# DICOM-task

This is a task from the following [repository](https://github.com/batuser/recruit)

## Task description

### Input data

Located in this repository in the `src` directory

### Exercise

Link to `pydicom` documentation - https://pydicom.github.io/pydicom/stable
Perform input transformations using the `pydicom` module. You need to do the following:
* delete information stored in the key `PatientName` (anonymize files)
* using the information in the `StudyInstanceUID`, `SeriesInstanceUID`, `SOPInstanceUID` keys, convert the file storage structure to the following:
   1. at the first level `StudyInstanceUID`
   2. at the second level `SeriesInstanceUID`
   3. the file name will be the value of `SOPInstanceUID` with the extension `.dcm`

     Thus, the path to each file will look like this: `$StudyInstanceUID/$SeriesInstanceUID/$SOPInstanceUID.dcm`

* Additionally, you need to create a file in which the path to each file in the source structure is mapped to the path to the file in the target structure.

### Output

The result of the work that you need to send an archive containing inside itself:
* directory with the resulting structure;
* a file with a list of matching paths;
* script code.

Send the result to vitaliy.nekrasov@3opinion.ai with the subject line: **Name - Machine Learning Data Engineer**
