# Pre-rupture fault mapping
> We wrote some code to edit the attribute tables in shp files. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Students created pre-rupture fault maps in QGIS. They mapped faults and points on their maps and turned in the shp files. However, the files had no identifying data in the attribute tables
- With this code, we added fields and filled the field attributes with student information.
- Fields = Columns, Attributes = Data in field columns.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- QGIS
- PyQGIS

## Setup
- The code needs to be run in the Python console in QGIS. 
- Add all shapefiles you wish to change into one folder. 

## Usage
- Change folder variable to go to your directory with your shp files.
- Change information in student_info to what you want to be filled into the fields
- Shp file name begins with student ID number
- Option to delete fields included.


## Project Status
Project is: _complete_



## Acknowledgements
I used these two resources to create this code: 
- [Anita Graser's PyQGIS 101 documentation](https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis101-creating-editing-a-new-vector-layer/)
- [OpenSourceOptions guide to creating vector layer fields in PyQGIS](https://opensourceoptions.com/blog/pyqgis-adding-and-deleting-vector-layer-fields/)

Many, many thanks to Chelsea Scott and Maddie Schwarz for their help!!


## Contact
Created by [@mindyzuckerman](https://github.com/mindyzuckerman) - feel free to contact me.


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
