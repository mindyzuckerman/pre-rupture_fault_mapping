This readme file was generated on 2022-08-17 by Mindy Zuckerman

# Repeatability_Shapefiles

## GENERAL INFORMATION

### Author Information
- Name: Malinda (Mindy) Zuckerman
- Institution: Arizona State University
- Email: mgzucker@asu.edu
- ASU Coinvestigators:
	- Chelsea Scott
	- Ramon Arrowsmith
	- Rachel Adam



## DATA & FILE OVERVIEW

- Date of data collection: 2022-03 - 2022-06
- CRS for all files - EPSG:4326 - WGS 84
- Please open the Repeatability.qgz file in QGIS for quick access to all shapefiles with correct symbology.

### File List 

We anticipate viewing our mapping point and linework on the open-source and free software QGIS (https://www.qgis.org). The shape (shp) files are likely to open in other GIS software such as ESRI, but the styles may look different than intended. 


#### Files include
- FCR folder: Fault line shapefiles
- GIR folder: Geomorphic indicator point shapefiles
- Mapping_Polygons folder: Line shp files of mapping area boundaries for each location
- Repeatability QGIS project (qgz): Contains all shp files in Repeatability_Shapefiles displayed with our symbology. Project must be opened with all files and folders in their original order.

#### The following files are located in FCR and GIR folders for each mapping location 
- Shapefiles (shp) for lines and polygon features are included in each folder for a 
given mapping area.
- Mapping styles for QGIS (qml). In the FCR folder these are needed to set the color and line thickness to display our certainty ranking (i.e., strong to concealed) and primary vs. secondary faulting. In the GIR folder these are needed to set the marker symbology to match the rankings of geomorphic features.
- Definition Files containing information about the service properties, included in 
case of data discrepancies when transitioning files.

#### Directory Structure for FCR and GIR folders (Level 1 > Level 2 > Level 3)

- Level 1 - FCR or GIR folder
- Level 2 - Location folders and shp file containing all lines or points.
- Level 3 - Individual student shp files. There are no style files associated with student shp files at level 3. Styles can be copied and pasted from higher level shp files.

Every shp file with an associated style file should be correctly symbolized automatically with the current directory structure. To open a style file manually, open the .qml for each file within the associated folder.

#### Definitions
- FCR = fault confidence ranking
- GIR = geomorphic indicator ranking
- Field definitions
	- Location = Mapping area
  - Student = Anonymized student ID number
  - Level = Academic level (undergraduate, graduate, postdoc)
  - Project_num = 1st or 2nd main mapping project
  - Fault_Exp = Did the student have prior knowledge of the fault?
  - Grade = Map grade (unused)
  
##### Support from PG&E Company

