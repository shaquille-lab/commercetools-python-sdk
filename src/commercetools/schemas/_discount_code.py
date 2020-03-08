# DO NOT EDIT! This file is automatically generated

import marshmallow

from commercetools import helpers, types
from commercetools.schemas._common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools.schemas._type import FieldContainerField

__all__ = [
    "DiscountCodeChangeCartDiscountsActionSchema",
    "DiscountCodeChangeGroupsActionSchema",
    "DiscountCodeChangeIsActiveActionSchema",
    "DiscountCodeDraftSchema",
    "DiscountCodePagedQueryResponseSchema",
    "DiscountCodeReferenceSchema",
    "DiscountCodeResourceIdentifierSchema",
    "DiscountCodeSchema",
    "DiscountCodeSetCartPredicateActionSchema",
    "DiscountCodeSetCustomFieldActionSchema",
    "DiscountCodeSetCustomTypeActionSchema",
    "DiscountCodeSetDescriptionActionSchema",
    "DiscountCodeSetMaxApplicationsActionSchema",
    "DiscountCodeSetMaxApplicationsPerCustomerActionSchema",
    "DiscountCodeSetNameActionSchema",
    "DiscountCodeSetValidFromActionSchema",
    "DiscountCodeSetValidFromAndUntilActionSchema",
    "DiscountCodeSetValidUntilActionSchema",
    "DiscountCodeUpdateActionSchema",
    "DiscountCodeUpdateSchema",
]


class DiscountCodeDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeDraft`."
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    code = marshmallow.fields.String(allow_none=True)
    cart_discounts = marshmallow.fields.Nested(
        nested="commercetools.schemas._cart_discount.CartDiscountResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="cartDiscounts",
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )
    is_active = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="isActive"
    )
    max_applications = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplications"
    )
    max_applications_per_customer = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplicationsPerCustomer"
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    groups = marshmallow.fields.List(
        marshmallow.fields.Nested(
            nested="commercetools.schemas.None.stringSchema",
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
        missing=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.DiscountCodeDraft(**data)


class DiscountCodePagedQueryResponseSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodePagedQueryResponse`."
    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._discount_code.DiscountCodeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.DiscountCodePagedQueryResponse(**data)


class DiscountCodeReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._discount_code.DiscountCodeSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.DiscountCodeReference(**data)


class DiscountCodeResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.DiscountCodeResourceIdentifier(**data)


class DiscountCodeSchema(BaseResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCode`."
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
    name = LocalizedStringField(allow_none=True, missing=None)
    description = LocalizedStringField(allow_none=True, missing=None)
    code = marshmallow.fields.String(allow_none=True)
    cart_discounts = marshmallow.fields.Nested(
        nested="commercetools.schemas._cart_discount.CartDiscountReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="cartDiscounts",
    )
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )
    is_active = marshmallow.fields.Bool(allow_none=True, data_key="isActive")
    references = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("typeId", "type_id"),
            discriminator_schemas={
                "cart-discount": "commercetools.schemas._cart_discount.CartDiscountReferenceSchema",
                "cart": "commercetools.schemas._cart.CartReferenceSchema",
                "category": "commercetools.schemas._category.CategoryReferenceSchema",
                "channel": "commercetools.schemas._channel.ChannelReferenceSchema",
                "key-value-document": "commercetools.schemas._custom_object.CustomObjectReferenceSchema",
                "customer-group": "commercetools.schemas._customer_group.CustomerGroupReferenceSchema",
                "customer": "commercetools.schemas._customer.CustomerReferenceSchema",
                "discount-code": "commercetools.schemas._discount_code.DiscountCodeReferenceSchema",
                "inventory-entry": "commercetools.schemas._inventory.InventoryEntryReferenceSchema",
                "order-edit": "commercetools.schemas._order_edit.OrderEditReferenceSchema",
                "order": "commercetools.schemas._order.OrderReferenceSchema",
                "payment": "commercetools.schemas._payment.PaymentReferenceSchema",
                "product-discount": "commercetools.schemas._product_discount.ProductDiscountReferenceSchema",
                "product-type": "commercetools.schemas._product_type.ProductTypeReferenceSchema",
                "product": "commercetools.schemas._product.ProductReferenceSchema",
                "review": "commercetools.schemas._review.ReviewReferenceSchema",
                "shipping-method": "commercetools.schemas._shipping_method.ShippingMethodReferenceSchema",
                "shopping-list": "commercetools.schemas._shopping_list.ShoppingListReferenceSchema",
                "state": "commercetools.schemas._state.StateReferenceSchema",
                "store": "commercetools.schemas._store.StoreReferenceSchema",
                "tax-category": "commercetools.schemas._tax_category.TaxCategoryReferenceSchema",
                "type": "commercetools.schemas._type.TypeReferenceSchema",
                "zone": "commercetools.schemas._zone.ZoneReferenceSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        )
    )
    max_applications = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplications"
    )
    max_applications_per_customer = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplicationsPerCustomer"
    )
    custom = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    groups = marshmallow.fields.List(marshmallow.fields.String(allow_none=True))
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.DiscountCode(**data)


class DiscountCodeUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeUpdateAction(**data)


class DiscountCodeUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCartDiscounts": "commercetools.schemas._discount_code.DiscountCodeChangeCartDiscountsActionSchema",
                "changeGroups": "commercetools.schemas._discount_code.DiscountCodeChangeGroupsActionSchema",
                "changeIsActive": "commercetools.schemas._discount_code.DiscountCodeChangeIsActiveActionSchema",
                "setCartPredicate": "commercetools.schemas._discount_code.DiscountCodeSetCartPredicateActionSchema",
                "setCustomField": "commercetools.schemas._discount_code.DiscountCodeSetCustomFieldActionSchema",
                "setCustomType": "commercetools.schemas._discount_code.DiscountCodeSetCustomTypeActionSchema",
                "setDescription": "commercetools.schemas._discount_code.DiscountCodeSetDescriptionActionSchema",
                "setMaxApplications": "commercetools.schemas._discount_code.DiscountCodeSetMaxApplicationsActionSchema",
                "setMaxApplicationsPerCustomer": "commercetools.schemas._discount_code.DiscountCodeSetMaxApplicationsPerCustomerActionSchema",
                "setName": "commercetools.schemas._discount_code.DiscountCodeSetNameActionSchema",
                "setValidFrom": "commercetools.schemas._discount_code.DiscountCodeSetValidFromActionSchema",
                "setValidFromAndUntil": "commercetools.schemas._discount_code.DiscountCodeSetValidFromAndUntilActionSchema",
                "setValidUntil": "commercetools.schemas._discount_code.DiscountCodeSetValidUntilActionSchema",
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
        return types.DiscountCodeUpdate(**data)


class DiscountCodeChangeCartDiscountsActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeChangeCartDiscountsAction`."
    cart_discounts = marshmallow.fields.Nested(
        nested="commercetools.schemas._cart_discount.CartDiscountResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        data_key="cartDiscounts",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeChangeCartDiscountsAction(**data)


class DiscountCodeChangeGroupsActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeChangeGroupsAction`."
    groups = marshmallow.fields.List(marshmallow.fields.String(allow_none=True))

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeChangeGroupsAction(**data)


class DiscountCodeChangeIsActiveActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeChangeIsActiveAction`."
    is_active = marshmallow.fields.Bool(allow_none=True, data_key="isActive")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeChangeIsActiveAction(**data)


class DiscountCodeSetCartPredicateActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetCartPredicateAction`."
    cart_predicate = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="cartPredicate"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetCartPredicateAction(**data)


class DiscountCodeSetCustomFieldActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetCustomFieldAction`."
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetCustomFieldAction(**data)


class DiscountCodeSetCustomTypeActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetCustomTypeAction`."
    type = marshmallow.fields.Nested(
        nested="commercetools.schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetCustomTypeAction(**data)


class DiscountCodeSetDescriptionActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetDescriptionAction`."
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetDescriptionAction(**data)


class DiscountCodeSetMaxApplicationsActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetMaxApplicationsAction`."
    max_applications = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplications"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetMaxApplicationsAction(**data)


class DiscountCodeSetMaxApplicationsPerCustomerActionSchema(
    DiscountCodeUpdateActionSchema
):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetMaxApplicationsPerCustomerAction`."
    max_applications_per_customer = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="maxApplicationsPerCustomer"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetMaxApplicationsPerCustomerAction(**data)


class DiscountCodeSetNameActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetNameAction`."
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetNameAction(**data)


class DiscountCodeSetValidFromActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetValidFromAction`."
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetValidFromAction(**data)


class DiscountCodeSetValidFromAndUntilActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetValidFromAndUntilAction`."
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetValidFromAndUntilAction(**data)


class DiscountCodeSetValidUntilActionSchema(DiscountCodeUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.DiscountCodeSetValidUntilAction`."
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.DiscountCodeSetValidUntilAction(**data)
