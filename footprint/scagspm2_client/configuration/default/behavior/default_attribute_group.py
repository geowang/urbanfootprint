from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.client.configuration.fixture import AttributeGroupFixture
from footprint.main.models.geospatial.attribute_group import AttributeGroupKey, AttributeGroup

__author__ = 'calthorpe'

class DefaultAttributeGroupFixture(DefaultMixin, AttributeGroupFixture):
    """
        Defines the default AttributeGroup Fixtures
    """
    def attribute_groups(self, **kwargs):
        key = AttributeGroupKey.Fab.ricate
        return [
            AttributeGroup(
                # Defines an association between a toOne relation and the primitive seed value
                # so that the latter can be kept in sync whenever the former is updated
                key=key('relation_to_primitive_association'),
                attribute_keys=['relation', 'primitive'],
            ),
            AttributeGroup(
                # Groups the update and create timestamps
                key=key('timestamps'),
                attribute_keys=['created', 'updated'],
            )
        ]
