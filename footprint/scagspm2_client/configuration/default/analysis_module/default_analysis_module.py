from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.client.configuration.fixture import AnalysisModuleFixture
from footprint.main.models.geospatial.behavior import Behavior
from footprint.main.models.analysis_module.analysis_module import AnalysisModuleConfiguration
from footprint.main.models.geospatial.behavior import BehaviorKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe'

class DefaultAnalysisModule(DefaultMixin, AnalysisModuleFixture):

    def default_analysis_module_configurations(self, **kwargs):
        config_entity = self.config_entity
        uf_analysis_module = lambda module: 'footprint.main.models.analysis_module.%s' % module

        behavior_key = BehaviorKey.Fab.ricate
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return map(
            lambda configuration:
            AnalysisModuleConfiguration.analysis_module_configuration(config_entity, **configuration),
            FixtureList([]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
        )