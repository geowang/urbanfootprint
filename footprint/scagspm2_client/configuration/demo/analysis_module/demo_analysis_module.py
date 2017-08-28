from footprint.client.configuration.fixture import AnalysisModuleFixture

__author__ = 'calthorpe'

class DemoAnalysisModuleFixture(AnalysisModuleFixture):

    def default_analysis_module_configurations(self, **kwargs):
        return []
