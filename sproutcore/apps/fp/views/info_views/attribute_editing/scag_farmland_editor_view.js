/*
 * UrbanFootprint v1.5
 * Copyright (C) 2016 Calthorpe Analytics
 *
 * This file is part of UrbanFootprint version 1.5
 *
 * UrbanFootprint is distributed under the terms of the GNU General
 * Public License version 3, as published by the Free Software Foundation. This
 * code is distributed WITHOUT ANY WARRANTY, without implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
 * Public License v3 for more details; see <http://www.gnu.org/licenses/>.
 */

sc_require('views/info_views/select_info_view');
sc_require('views/info_views/editable_text_field_view');
sc_require('properties/plural_property');


Footprint.FarmlandEditorView = SC.View.extend({
    classNames: ['footprint-farmland-editor-view'],
    childViews: ['farmlandView', 'commentView'],

    activeLayer: null,
    activeLayerBinding: SC.Binding.oneWay('Footprint.layerActiveController.content'),

    content: null,
    contentBinding: SC.Binding.oneWay('Footprint.featuresEditController.content'),

    farmlandView: SC.View.extend({
        childViews: ['farmlandTitleView', 'farmlandSelectView'],
        layout: {height: 40, left: 10, right: 30, top: 20},
        content: null,
        contentBinding: SC.Binding.from('.parentView.content'),

        farmlandTitleView: SC.LabelView.extend({
            classNames: ['footprint-bold-title-white-view'],
            textAlign: SC.ALIGN_CENTER,
            backgroundColor: '#3366CC',
            layout: {height: 16},
            value: 'SCAG Farmland Types'
        }),

        farmlandSelectView: Footprint.SelectInfoView.extend({
            layout: {height: 24, top: 16},
            contentBinding: SC.Binding.oneWay('Footprint.clientFarmlandDefinitionController.arrangedObjects'),
            menuWidth: 400,

            // Controller and View selection remain in sync
            selectionBinding: 'Footprint.clientFarmlandDefinitionController.selection',
            recordType: Footprint.ClientFarmlandDefinition,
            itemTitleKey: 'farmland_description',
            contentKey: 'features',
            contentStatusKey: 'featuresStatus',
            // The controller calls propertyDidChange on this when updates finish. We use it to update value
            refreshValue: null,
            refreshValueBinding: SC.Binding.oneWay('Footprint.featuresEditController.recordsDidUpdate'),

            features: null,
            featuresBinding: SC.Binding.oneWay('.parentView.content'),
            featuresStatus: null,
            featuresStatusBinding: SC.Binding.oneWay('*features.status'),

            // Create a computed property that returns the farmland_definition if all features have the same
            // farmland_definition. This property updates to changes to the features, their status, and the
            // farmland_definition of each.
            value: Footprint.pluralContentValuePropertyCreator('features', 'featuresStatus', 'farmland_definition', 'refreshValue'),
            // The value updates the singleSelection of the controller (which updates the selection of Controller and View)
            // Changing the selection in turn updates the value, which causes all current features values to update
            valueBinding: 'Footprint.clientFarmlandDefinitionController.singleSelection'
        })
    }),

    commentView: Footprint.EditableTextFieldView.extend({
        layout: {left: 10, right: 30, height: 100, top: 80},
        title: 'Notes',
        titleClassNames: ['footprint-bold-title-white-view'],
        titleBackgroundColor: '#3366CC',
        titleViewLayout: { height: 17, top: 0 },
        isTextArea: YES,
        isEditable:YES,
        contentBinding: SC.Binding.oneWay('.parentView.content'),
        editableContentViewLayout: { top: 17, bottom: 0 },
        contentValueKey: 'notes',
        // The controller calls propertyDidChange on this when updates finish. We use it to update value
        refreshValue: null,
        refreshValueBinding: SC.Binding.oneWay('Footprint.featuresEditController.recordsDidUpdate'),
        value: Footprint.pluralContentValueProperty
    })
});
