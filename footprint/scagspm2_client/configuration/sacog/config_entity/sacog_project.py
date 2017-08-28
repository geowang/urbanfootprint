from footprint.client.configuration.sacog.config_entity.sacog_region import SacogDbEntityKey
from footprint.main.models.analysis.climate_zone_feature import ClimateZoneFeature
from footprint.main.models.analysis.vmt_features.vmt_trip_lengths_feature import VmtTripLengthsFeature
from footprint.main.models.analysis.agriculture_feature import AgricultureFeature
from footprint.main.models.base.census_block import CensusBlock
from footprint.main.models.base.census_blockgroup import CensusBlockgroup
from footprint.main.models.base.census_tract import CensusTract
from footprint.main.models.base.base_feature import BaseFeature
from footprint.main.models.config.db_entity_interest import DbEntity
from footprint.main.models.geospatial.behavior import Behavior, BehaviorKey
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.feature_class_creator import FeatureClassCreator
from footprint.client.configuration.fixture import ProjectFixture
from footprint.client.configuration.sacog.base.sacog_existing_land_use_parcel_feature import \
    SacogExistingLandUseParcelFeature
from footprint.client.configuration.sacog.base.sacog_stream_feature import SacogStreamFeature
from footprint.client.configuration.sacog.base.sacog_vernal_pool_feature import SacogVernalPoolFeature
from footprint.client.configuration.sacog.base.sacog_wetland_feature import SacogWetlandFeature
from footprint.main.lib.functions import merge
from footprint.main.models.geospatial.intersection import Intersection, IntersectionKey
from footprint.main.model_utils import uf_model
from footprint.main.utils.utils import get_property_path

__author__ = 'calthorpe_associates'


class SacogProjectFixture(ProjectFixture):
    def feature_class_lookup(self):
        """
            Adds mappings of custom Feature classes
        :return:
        """
        parent_fixture = self.parent_fixture
        feature_class_lookup = parent_fixture.feature_class_lookup()
        return merge(
            feature_class_lookup,
            FeatureClassCreator(self.config_entity).key_to_dynamic_model_class_lookup(self.default_db_entities())
        )

    def default_db_entities(self, **kwargs):
        """
        Project specific SACOG additional db_entities
        :param default_dict:
        :return:
        """
        project = self.config_entity
        # The DbEntity keyspace. These keys have no prefix
        Key = SacogDbEntityKey
        default_key = DbEntityKey.Fab.ricate
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return super(SacogProjectFixture, self).default_db_entities() + [
            update_or_create_db_entity(project, DbEntity(
                key=DbEntityKey.BASE,
                # Override. If a name override is supplied, put it in. Otherwise leave null to derive it from the key
                name='Urban Base Canvas (UF)',
                # name=get_property_path(kwargs, 'overrides.%s.name' % Key.BASE),
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=BaseFeature,
                    # The Base Feature is normally considered a primary_geography unless overridden
                    primary_geography=get_property_path(kwargs, 'overrides.%s.primary_geography' % Key.BASE) or True,
                    primary_key='geography_id',
                    primary_key_type='varchar',

                    # The Base Feature is normally associated to a subclass of Geography unless overridden
                    geography_class_name=get_property_path(kwargs, 'overrides.%s.geography_class_name' % Key.BASE) or
                                         'footprint.main.models.geographies.parcel.Parcel',
                    # Create a built_form ForeignKey to a single BuiltForm,
                    # by initially joining our 'built_form_key' attribute to its 'key' attribute
                    related_fields=dict(built_form=dict(
                        single=True,
                        related_class_name=uf_model('built_form.built_form.BuiltForm'),
                        source_class_join_field_name='built_form_key',
                        related_class_join_field_name='key',
                    ))
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('base_feature'),
                ),
            )),

            update_or_create_db_entity(project, DbEntity(
                key=Key.CENSUS_TRACT,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CensusTract
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),

            update_or_create_db_entity(project, DbEntity(
                key=Key.CENSUS_BLOCKGROUP,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CensusBlockgroup,
                    related_fields=dict(census_tract=dict(
                        # Relate to a single CensusTract from our tract attribute to theirs
                        single=True,
                        related_key=default_key('census_tract'),
                        related_class_join_field_name='tract',
                        source_class_join_field_name='tract'))
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),

            update_or_create_db_entity(project, DbEntity(
                key=Key.CENSUS_BLOCK,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CensusBlock,
                    related_fields=dict(census_blockgroup=dict(
                        # Relate to a single CensusBlockgroup from our blockgroup attribute to theirs
                        single=True,
                        related_key=default_key('census_blockgroup'),
                        related_class_join_field_name='blockgroup',
                        source_class_join_field_name='blockgroup'))
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),

            update_or_create_db_entity(project, DbEntity(
                key=DbEntityKey.BASE_AGRICULTURE,
                name='Agriculture Base Canvas (RUCS)',
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=AgricultureFeature,
                    primary_key='geography_id',
                    primary_key_type='varchar',
                    # Create a built_form ForeignKey to a single BuiltForm,
                    # by initially joining our 'built_form_key' attribute to its 'key' attribute
                    related_fields=dict(built_form=dict(
                        single=True,
                        related_class_name='footprint.main.models.built_form.built_form.BuiltForm',
                        related_class_join_field_name='key',
                        source_class_join_field_name='built_form_key')
                    )
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('base_agriculture'),
                    intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                )
            )),

            # TODO why is a future defined at the project scope?
            update_or_create_db_entity(project, DbEntity(
                key=DbEntityKey.VMT_FUTURE_TRIP_LENGTHS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=VmtTripLengthsFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('internal_analysis'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),

            update_or_create_db_entity(project, DbEntity(
                key=DbEntityKey.VMT_BASE_TRIP_LENGTHS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=VmtTripLengthsFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('internal_analysis'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),

            update_or_create_db_entity(project, DbEntity(
                key=DbEntityKey.CLIMATE_ZONE,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=ClimateZoneFeature,
                    related_fields=dict(
                        evapotranspiration_zone=dict(
                            single=True,
                            related_class_name=uf_model('policy.water.evapotranspiration_baseline.EvapotranspirationBaseline'),
                            related_class_join_field_name='zone',
                            source_class_join_field_name='evapotranspiration_zone_id'),

                        forecasting_climate_zone=dict(
                            single=True,
                            related_class_name=uf_model('policy.energy.commercial_energy_baseline.CommercialEnergyBaseline'),
                            related_class_join_field_name='zone',
                            source_class_join_field_name='forecasting_climate_zone_id'),

                        title_24_zone=dict(
                            single=True,
                            related_class_name=uf_model('policy.energy.residential_energy_baseline.ResidentialEnergyBaseline'),
                            related_class_join_field_name='zone',
                            source_class_join_field_name='title_24_zone_id')
                    )
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('internal_analysis'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                ),
            )),

            update_or_create_db_entity(project, DbEntity(
                key=Key.EXISTING_LAND_USE_PARCEL_SOURCE,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogExistingLandUseParcelFeature,
                    primary_key='geography_id',
                    primary_key_type='varchar',
                    fields=dict(),
                    related_fields=dict(land_use_definition=dict(
                        single=True,
                        related_class_name='footprint.client.configuration.sacog.built_form.sacog_land_use_definition.SacogLandUseDefinition',
                        # Use this for the resource type, since we don't want a client-specific resource URL
                        # TODO not wired up yet
                        resource_model_class_name='footprint.main.models.built_form.ClientLandUseDefinition',
                        related_class_join_field_name='land_use',
                        source_class_join_field_name='land_use')
                    )
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(join_type='attribute')
                )
            )),
            update_or_create_db_entity(project, DbEntity(
                key=Key.VERNAL_POOL,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogVernalPoolFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('environmental_constraint')
                )
            )),
            update_or_create_db_entity(project, DbEntity(
                key=Key.WETLAND,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogWetlandFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('environmental_constraint')
                )
            )),
            update_or_create_db_entity(project, DbEntity(
                key=Key.STREAM,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogStreamFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('environmental_constraint')
                )
            ))
            # update_or_create_db_entity(project, DbEntity(
            #     key=Key.HARDWOOD,
            #     feature_class_configuration=FeatureClassConfiguration(
            #         abstract_class=SacogHardwoodFeature
            #     ),
            #     feature_behavior=FeatureBehavior(
            #         behavior=get_behavior('environmental_constraint')
            #     )
            # )),

        ]


