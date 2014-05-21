import arcpy

class Toolbox(object):
    """ Our example toolbox which initializes a single tool."""
    
    def __init__(self):
        self.label = 'MaxEnt calculator'
        self.alias = 'maxent'
        self.tools = [calc_maxent]

class calc_maxent(object):
    """ An example tool which calculates the Maximum Entropy of point observations. """
    def __init__(self):
        self.label = u'Calculate MaxEnt'
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input_bathymetric_raster
        input_pts = arcpy.Parameter()
        input_pts.name = u'Input_points'
        input_pts.displayName = u'Input points'
        input_pts.parameterType = 'Required'
        input_pts.direction = 'Input'
        input_pts.datatype = dt.format('Feature Layer')

        output_raster = arcpy.Parameter()
        output_raster.name = u'Output_raster'
        output_raster.displayName = u'output raster'
        output_raster.parameterType = 'Required'
        output_raster.direction = 'Output'
        output_raster.datatype = dt.format('Raster Layer')

        return [input_pts, output_raster]

    def updateParameters(self, parameters):
        validator = getattr(self, 'ToolValidator', None)
        if validator:
            return validator(parameters).updateParameters()

    def updateMessages(self, parameters):
        validator = getattr(self, 'ToolValidator', None)

        if validator:
            return validator(parameters).updateMessages()

    def execute(self, parameters, messages):
        # run related python script with selected input parameters
        from scripts import maxent
        aspect.main(input_pts=parameters[0].valueAsText,
            output_raster=parameters[1].valueAsText)
