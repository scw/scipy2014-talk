# run_maxent.py

import os, csv

# could easily import ArcPy here to add a mixed model, executing ArcGIS-specific functions alongside your other Python code.


# location of maxent runtime
maxent_jar = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'maxent.jar')

def main(csv_input=None, climate_dir=None, output_dir=None, output_format='Logistic', 
        response_curves=False, prediction_pictures=False, jackknife=False):
   
    output_prefix = os.path.splitext(os.path.basename(csv_input))[0]
    output_dir = os.path.join(output_prefix, output_prefix)

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    cmd = "java -mx512m -jar {} -e {} -s {} -o {} outputformat={}".format(
            maxent_jar, climate_dir, output_dir, output_format)
    
    os.system(cmd)
