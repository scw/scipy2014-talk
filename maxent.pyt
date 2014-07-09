import arcpy

class Toolbox(object):
    """ Our example toolbox which initializes a single tool."""
    def __init__(self):
        self.label = 'Maximum Entropy'
        self.alias = 'maxent'
        self.tools = [calc_maxent]

class calc_maxent(object):
    """ An example tool which calculates the Maximum Entropy of point observations. """
    def __init__(self):
        self.label = u'Calculate MaxEnt'
        self.canRunInBackground = False

    def getParameterInfo(self):
        input_csv = arcpy.Parameter()
        input_csv.name = u'Species Occurence CSV'
        input_csv.displayName = u'Species Occurence CSV'
        input_csv.parameterType = 'Required'
        input_csv.direction = 'Input'
        input_csv.datatype = 'Feature Layer'

        climate_dir = arcpy.Parameter()
        climate_dir.name = 'Climate Data Directory'
        climate_dir.displayName = 'Climate Data Directory'
        climate_dir.parameterType = 'Required'
        climate_dir.direction = 'Input'
        climate_dir.datatype = 'Folder'

        model_type = arcpy.Parameter()
        model_type.name = 'Model Type'
        model_type.displayName = 'Model Type'
        model_type.direction = 'Input'
        model_type.datatype = 'String'
        model_type.value = 'Logistic'
        model_type.filter.list = ['Logistic', 'Cumulative', 'Raw']

        output_format = arcpy.Parameter()
        output_format.name = 'Output Format'
        output_format.displayName = 'Output Format'
        output_format.direction = 'Input'
        output_format.datatype = 'String'
        output_format.value = 'ASCII'
        output_format.filter.list = ['ASCII', 'MXE', 'BIL', 'GRD']

        jacknife = arcpy.Parameter()
        jacknife.name = 'Perform Jacknifing?'
        jacknife.displayName = 'Perform Jacknifing?'
        jacknife.direction = 'Input'
        jacknife.parameterType = 'Required'
        jacknife.datatype = 'Boolean'

        output_dir= arcpy.Parameter()
        output_dir.name = u'Output_directory'
        output_dir.displayName = u'output directory'
        output_dir.parameterType = 'Required'
        output_dir.direction = 'Output'
        output_dir.datatype = 'Folder'

        return [input_csv, climate_dir, model_type, output_format, jacknife, output_dir]

    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
            return validator(parameters).updateParameters()

    def execute(self, parameters, messages):
        # run related python script with selected input parameters
        import run_maxent
        
        run_maxent.main(input_csv=parameters[0].valueAsText, climate_dir=parameters[1].valueAsText,
                model_type=parameters[2].valueAsText, output_format=parameters[3].valueAsText,
                jacknife=parameters[4].valueAsText)
