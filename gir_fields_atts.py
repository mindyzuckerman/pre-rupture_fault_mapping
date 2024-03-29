#Function 1 creates fields and fills in attributes in a folder of point
#shapefiles of GIR features in one mapping area.

#Function 2 iterates through shapefiles in the folder and adds the fields.
#Code also selects each shapefile from the folder and fills the fields
#with data given in student_info

#Use only one folder per location with all student shp files.

import os
import numpy

folder = r'C:\Users\...filepath.to.folder.with.files'

#Attributes that will be fill in fields
#Fields are location, student ID number, student level, project number, location experience, map grade
student_info = [['EMC', 1, 'Grad', 2, 'No', 0],
    ['EMC', 2, 'Grad', 2, 'No', 0],
    ['EMC', 3, 'Undergrad', 1, 'No', 0],
    ['EMC', 4, 'PostDoc', 2, 'No', 0],
    ['EMC', 6, 'Grad', 1, 'No', 0],
    ['EMC', 5, 'PostDoc', 1, 'No', 0],
    ['EMC', 7, 'Grad', 1, 'No', 0],
    ['EMC', 8, 'Grad', 1, 'No', 0],
    ['EMC', 10, 'Undergrad', 2, 'No', 0],
    ['EMC', 11, 'Grad', 1, 'No', 0],
    ['EMC', 12, 'Grad', 1, 'No', 0],
    ['EMC', 13, 'Undergrad', 2, 'No', 0],
    ['EMC', 14, 'Grad', 2, 'No', 0],
    ['EMC', 15, 'Grad', 1, 'No', 0],
    ['EMC', 16, 'Grad', 1, 'No', 0],
    ['EMC', 20, 'Undergrad', 1, 'No', 0],
    ['EMC', 21, 'Grad', 1, 'No', 0]
    ]
#no student 6 for BP or RC

stud_len = (len(student_info)) #returns the number of items

#numbers match student ID numbers in shp file name
file_list = [21,20,16,15,14,13,12,11,10,8,7,6,5,4,3,2,1]
count = stud_len-1;

##Function 1##
for file_num in file_list:
    path = folder+'\\'+str(file_num)+"_EMC_GIR.shp" #change file name to match yours
#    shp_paths.append(path)
## use next line to edit shapefile without adding to map
#    layer = QgsVectorLayer(path,'',"ogr")
## use next line to edit shapefile AND add to map
    layer = iface.addVectorLayer(path, '', 'ogr')
##to delete attributes comment out addAttributes lines. Make sure updateFields is uncommented.
#    pv = layer.dataProvider().deleteAttributes([4,5,6,7,8,9])
    pv = layer.dataProvider().addAttributes([QgsField('Location', QVariant.String),
            QgsField('Student', QVariant.Int),
            QgsField('Level', QVariant.String),
            QgsField('Proj_Num', QVariant.Int),
            QgsField('Fault_Exp', QVariant.String),
            QgsField('Grade', QVariant.Int)])
    layer.updateFields()

##Function 2##
    student_row = student_info[count]
    count = count-1;
    with edit(layer):
        for f in layer.getFeatures():
            f['Location'] = student_row[0]
            f['Student'] = student_row[1]
            f['Level'] = student_row[2]
            f['Proj_Num'] = student_row[3]
            f['Fault_Exp'] = student_row[4]
            f['Grade'] = student_row[5]
            layer.updateFeature(f)
        
        layer.updateFeature(f)
