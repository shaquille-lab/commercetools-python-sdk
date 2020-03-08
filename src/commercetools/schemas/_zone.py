# DO NOT EDIT! This file is automatically generated

import marshmallow

from commercetools import helpers, types
from commercetools.schemas._common import (
    BaseResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

__all__ = [
    "LocationSchema",
    "ZoneAddLocationActionSchema",
    "ZoneChangeNameActionSchema",
    "ZoneDraftSchema",
    "ZonePagedQueryResponseSchema",
    "ZoneReferenceSchema",
    "ZoneRemoveLocationActionSchema",
    "ZoneResourceIdentifierSchema",
    "ZoneSchema",
    "ZoneSetDescriptionActionSchema",
    "ZoneSetKeyActionSchema",
    "ZoneUpdateActionSchema",
    "ZoneUpdateSchema",
]


class LocationSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.Location`."
    country = marshmallow.fields.String()
    state = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Location(**data)


class ZoneDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ZoneDraft`."
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    locations = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.LocationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ZoneDraft(**data)


class ZonePagedQueryResponseSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ZonePagedQueryResponse`."
    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ZonePagedQueryResponse(**data)


class ZoneReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.ZoneSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ZoneReference(**data)


class ZoneResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ZoneResourceIdentifier(**data)


class ZoneSchema(BaseResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.Zone`."
    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = marshmallow.fields.Nested(
        nested="commercetools.schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    locations = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.LocationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Zone(**data)


class ZoneUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ZoneUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ZoneUpdateAction(**data)


class ZoneUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ZoneUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addLocation": "commercetools.schemas._zone.ZoneAddLocationActionSchema",
                "changeName": "commercetools.schemas._zone.ZoneChangeNameActionSchema",
                "removeLocation": "commercetools.schemas._zone.ZoneRemoveLocationActionSchema",
                "setDescription": "commercetools.schemas._zone.ZoneSetDescriptionActionSchema",
                "setKey": "commercetools.schemas._zone.ZoneSetKeyActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ZoneUpdate(**data)


class ZoneAddLocationActionSchema(ZoneUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneAddLocationAction`."
    location = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.LocationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ZoneAddLocationAction(**data)


class ZoneChangeNameActionSchema(ZoneUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneChangeNameAction`."
    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ZoneChangeNameAction(**data)


class ZoneRemoveLocationActionSchema(ZoneUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneRemoveLocationAction`."
    location = marshmallow.fields.Nested(
        nested="commercetools.schemas._zone.LocationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ZoneRemoveLocationAction(**data)


class ZoneSetDescriptionActionSchema(ZoneUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneSetDescriptionAction`."
    description = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ZoneSetDescriptionAction(**data)


class ZoneSetKeyActionSchema(ZoneUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ZoneSetKeyAction`."
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ZoneSetKeyAction(**data)
