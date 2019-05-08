# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType

if typing.TYPE_CHECKING:
    from ._channel import ChannelReference
    from ._customer_group import CustomerGroupReference
    from ._product_discount import ProductDiscountReference
    from ._type import CustomFields, CustomFieldsDraft
__all__ = [
    "Address",
    "Asset",
    "AssetDimensions",
    "AssetDraft",
    "AssetSource",
    "CentPrecisionMoney",
    "DiscountedPrice",
    "GeoJson",
    "GeoJsonPoint",
    "HighPrecisionMoney",
    "Image",
    "ImageDimensions",
    "KeyReference",
    "LocalizedString",
    "Money",
    "MoneyType",
    "Price",
    "PriceDraft",
    "PriceTier",
    "Reference",
    "ReferenceTypeId",
    "Resource",
    "ResourceIdentifier",
    "ScopedPrice",
    "TypedMoney",
]


class Address(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AddressSchema`."
    #: Optional :class:`str`
    id: typing.Optional[str]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`str`
    title: typing.Optional[str]
    #: Optional :class:`str`
    salutation: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``firstName`` `in Commercetools)`
    first_name: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``lastName`` `in Commercetools)`
    last_name: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``streetName`` `in Commercetools)`
    street_name: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``streetNumber`` `in Commercetools)`
    street_number: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``additionalStreetInfo`` `in Commercetools)`
    additional_street_info: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``postalCode`` `in Commercetools)`
    postal_code: typing.Optional[str]
    #: Optional :class:`str`
    city: typing.Optional[str]
    #: Optional :class:`str`
    region: typing.Optional[str]
    #: Optional :class:`str`
    state: typing.Optional[str]
    #: :class:`str`
    country: typing.Optional["str"]
    #: Optional :class:`str`
    company: typing.Optional[str]
    #: Optional :class:`str`
    department: typing.Optional[str]
    #: Optional :class:`str`
    building: typing.Optional[str]
    #: Optional :class:`str`
    apartment: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``pOBox`` `in Commercetools)`
    p_o_box: typing.Optional[str]
    #: Optional :class:`str`
    phone: typing.Optional[str]
    #: Optional :class:`str`
    mobile: typing.Optional[str]
    #: Optional :class:`str`
    email: typing.Optional[str]
    #: Optional :class:`str`
    fax: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``additionalAddressInfo`` `in Commercetools)`
    additional_address_info: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        salutation: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        street_number: typing.Optional[str] = None,
        additional_street_info: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        country: typing.Optional["str"] = None,
        company: typing.Optional[str] = None,
        department: typing.Optional[str] = None,
        building: typing.Optional[str] = None,
        apartment: typing.Optional[str] = None,
        p_o_box: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        mobile: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        fax: typing.Optional[str] = None,
        additional_address_info: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
    ) -> None:
        self.id = id
        self.key = key
        self.title = title
        self.salutation = salutation
        self.first_name = first_name
        self.last_name = last_name
        self.street_name = street_name
        self.street_number = street_number
        self.additional_street_info = additional_street_info
        self.postal_code = postal_code
        self.city = city
        self.region = region
        self.state = state
        self.country = country
        self.company = company
        self.department = department
        self.building = building
        self.apartment = apartment
        self.p_o_box = p_o_box
        self.phone = phone
        self.mobile = mobile
        self.email = email
        self.fax = fax
        self.additional_address_info = additional_address_info
        self.external_id = external_id
        super().__init__()

    def __repr__(self) -> str:
        return (
            "Address(id=%r, key=%r, title=%r, salutation=%r, first_name=%r, last_name=%r, street_name=%r, street_number=%r, additional_street_info=%r, postal_code=%r, city=%r, region=%r, state=%r, country=%r, company=%r, department=%r, building=%r, apartment=%r, p_o_box=%r, phone=%r, mobile=%r, email=%r, fax=%r, additional_address_info=%r, external_id=%r)"
            % (
                self.id,
                self.key,
                self.title,
                self.salutation,
                self.first_name,
                self.last_name,
                self.street_name,
                self.street_number,
                self.additional_street_info,
                self.postal_code,
                self.city,
                self.region,
                self.state,
                self.country,
                self.company,
                self.department,
                self.building,
                self.apartment,
                self.p_o_box,
                self.phone,
                self.mobile,
                self.email,
                self.fax,
                self.additional_address_info,
                self.external_id,
            )
        )


class Asset(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AssetSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: List of :class:`commercetools.types.AssetSource`
    sources: typing.Optional[typing.List["AssetSource"]]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: Optional list of :class:`str`
    tags: typing.Optional[typing.List[str]]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        sources: typing.Optional[typing.List["AssetSource"]] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        tags: typing.Optional[typing.List[str]] = None,
        custom: typing.Optional["CustomFields"] = None,
        key: typing.Optional[str] = None,
    ) -> None:
        self.id = id
        self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        self.custom = custom
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return (
            "Asset(id=%r, sources=%r, name=%r, description=%r, tags=%r, custom=%r, key=%r)"
            % (
                self.id,
                self.sources,
                self.name,
                self.description,
                self.tags,
                self.custom,
                self.key,
            )
        )


class AssetDimensions(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AssetDimensionsSchema`."
    #: :class:`int`
    w: typing.Optional[int]
    #: :class:`int`
    h: typing.Optional[int]

    def __init__(
        self, *, w: typing.Optional[int] = None, h: typing.Optional[int] = None
    ) -> None:
        self.w = w
        self.h = h
        super().__init__()

    def __repr__(self) -> str:
        return "AssetDimensions(w=%r, h=%r)" % (self.w, self.h)


class AssetDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AssetDraftSchema`."
    #: List of :class:`commercetools.types.AssetSource`
    sources: typing.Optional[typing.List["AssetSource"]]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: Optional list of :class:`str`
    tags: typing.Optional[typing.List[str]]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        sources: typing.Optional[typing.List["AssetSource"]] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        tags: typing.Optional[typing.List[str]] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        key: typing.Optional[str] = None,
    ) -> None:
        self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        self.custom = custom
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return (
            "AssetDraft(sources=%r, name=%r, description=%r, tags=%r, custom=%r, key=%r)"
            % (
                self.sources,
                self.name,
                self.description,
                self.tags,
                self.custom,
                self.key,
            )
        )


class AssetSource(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AssetSourceSchema`."
    #: :class:`str`
    uri: typing.Optional[str]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.AssetDimensions`
    dimensions: typing.Optional["AssetDimensions"]
    #: Optional :class:`str` `(Named` ``contentType`` `in Commercetools)`
    content_type: typing.Optional[str]

    def __init__(
        self,
        *,
        uri: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        dimensions: typing.Optional["AssetDimensions"] = None,
        content_type: typing.Optional[str] = None,
    ) -> None:
        self.uri = uri
        self.key = key
        self.dimensions = dimensions
        self.content_type = content_type
        super().__init__()

    def __repr__(self) -> str:
        return "AssetSource(uri=%r, key=%r, dimensions=%r, content_type=%r)" % (
            self.uri,
            self.key,
            self.dimensions,
            self.content_type,
        )


class DiscountedPrice(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountedPriceSchema`."
    #: :class:`commercetools.types.Money`
    value: typing.Optional["Money"]
    #: :class:`commercetools.types.ProductDiscountReference`
    discount: typing.Optional["ProductDiscountReference"]

    def __init__(
        self,
        *,
        value: typing.Optional["Money"] = None,
        discount: typing.Optional["ProductDiscountReference"] = None,
    ) -> None:
        self.value = value
        self.discount = discount
        super().__init__()

    def __repr__(self) -> str:
        return "DiscountedPrice(value=%r, discount=%r)" % (self.value, self.discount)


class GeoJson(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.GeoJsonSchema`."
    #: :class:`str`
    type: typing.Optional[str]
    #: :class:`list`
    coordinates: typing.Optional[list]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        coordinates: typing.Optional[list] = None,
    ) -> None:
        self.type = type
        self.coordinates = coordinates
        super().__init__()

    def __repr__(self) -> str:
        return "GeoJson(type=%r, coordinates=%r)" % (self.type, self.coordinates)


class Image(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ImageSchema`."
    #: :class:`str`
    url: typing.Optional[str]
    #: :class:`commercetools.types.ImageDimensions`
    dimensions: typing.Optional["ImageDimensions"]
    #: Optional :class:`str`
    label: typing.Optional[str]

    def __init__(
        self,
        *,
        url: typing.Optional[str] = None,
        dimensions: typing.Optional["ImageDimensions"] = None,
        label: typing.Optional[str] = None,
    ) -> None:
        self.url = url
        self.dimensions = dimensions
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "Image(url=%r, dimensions=%r, label=%r)" % (
            self.url,
            self.dimensions,
            self.label,
        )


class ImageDimensions(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ImageDimensionsSchema`."
    #: :class:`int`
    w: typing.Optional[int]
    #: :class:`int`
    h: typing.Optional[int]

    def __init__(
        self, *, w: typing.Optional[int] = None, h: typing.Optional[int] = None
    ) -> None:
        self.w = w
        self.h = h
        super().__init__()

    def __repr__(self) -> str:
        return "ImageDimensions(w=%r, h=%r)" % (self.w, self.h)


class KeyReference(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.KeyReferenceSchema`."
    #: :class:`commercetools.types.ReferenceTypeId` `(Named` ``typeId`` `in Commercetools)`
    type_id: typing.Optional["ReferenceTypeId"]
    #: :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        key: typing.Optional[str] = None,
    ) -> None:
        self.type_id = type_id
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return "KeyReference(type_id=%r, key=%r)" % (self.type_id, self.key)


class LocalizedString(typing.Dict[(str, str)]):
    def __repr__(self) -> str:
        return "LocalizedString(%s)" % (
            ", ".join(f"{k}={v!r}" for k, v in self.items())
        )


class Money(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.MoneySchema`."
    #: :class:`int` `(Named` ``centAmount`` `in Commercetools)`
    cent_amount: typing.Optional[int]
    #: :class:`str` `(Named` ``currencyCode`` `in Commercetools)`
    currency_code: typing.Optional["str"]

    def __init__(
        self,
        *,
        cent_amount: typing.Optional[int] = None,
        currency_code: typing.Optional["str"] = None,
    ) -> None:
        self.cent_amount = cent_amount
        self.currency_code = currency_code
        super().__init__()

    def __repr__(self) -> str:
        return "Money(cent_amount=%r, currency_code=%r)" % (
            self.cent_amount,
            self.currency_code,
        )


class MoneyType(enum.Enum):
    CENT_PRECISION = "centPrecision"
    HIGH_PRECISION = "highPrecision"


class Price(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PriceSchema`."
    #: Optional :class:`str`
    id: typing.Optional[str]
    #: :class:`commercetools.types.Money`
    value: typing.Optional["Money"]
    #: Optional :class:`str`
    country: typing.Optional["str"]
    #: Optional :class:`commercetools.types.CustomerGroupReference` `(Named` ``customerGroup`` `in Commercetools)`
    customer_group: typing.Optional["CustomerGroupReference"]
    #: Optional :class:`commercetools.types.ChannelReference`
    channel: typing.Optional["ChannelReference"]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]
    #: Optional :class:`commercetools.types.DiscountedPrice`
    discounted: typing.Optional["DiscountedPrice"]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional list of :class:`commercetools.types.PriceTier`
    tiers: typing.Optional[typing.List["PriceTier"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        value: typing.Optional["Money"] = None,
        country: typing.Optional["str"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        custom: typing.Optional["CustomFields"] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
    ) -> None:
        self.id = id
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.discounted = discounted
        self.custom = custom
        self.tiers = tiers
        super().__init__()

    def __repr__(self) -> str:
        return (
            "Price(id=%r, value=%r, country=%r, customer_group=%r, channel=%r, valid_from=%r, valid_until=%r, discounted=%r, custom=%r, tiers=%r)"
            % (
                self.id,
                self.value,
                self.country,
                self.customer_group,
                self.channel,
                self.valid_from,
                self.valid_until,
                self.discounted,
                self.custom,
                self.tiers,
            )
        )


class PriceDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PriceDraftSchema`."
    #: :class:`commercetools.types.Money`
    value: typing.Optional["Money"]
    #: Optional :class:`str`
    country: typing.Optional["str"]
    #: Optional :class:`commercetools.types.CustomerGroupReference` `(Named` ``customerGroup`` `in Commercetools)`
    customer_group: typing.Optional["CustomerGroupReference"]
    #: Optional :class:`commercetools.types.ChannelReference`
    channel: typing.Optional["ChannelReference"]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional list of :class:`commercetools.types.PriceTier`
    tiers: typing.Optional[typing.List["PriceTier"]]

    def __init__(
        self,
        *,
        value: typing.Optional["Money"] = None,
        country: typing.Optional["str"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
    ) -> None:
        self.value = value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.custom = custom
        self.tiers = tiers
        super().__init__()

    def __repr__(self) -> str:
        return (
            "PriceDraft(value=%r, country=%r, customer_group=%r, channel=%r, valid_from=%r, valid_until=%r, custom=%r, tiers=%r)"
            % (
                self.value,
                self.country,
                self.customer_group,
                self.channel,
                self.valid_from,
                self.valid_until,
                self.custom,
                self.tiers,
            )
        )


class PriceTier(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PriceTierSchema`."
    #: :class:`int` `(Named` ``minimumQuantity`` `in Commercetools)`
    minimum_quantity: typing.Optional[int]
    #: :class:`commercetools.types.Money`
    value: typing.Optional["Money"]

    def __init__(
        self,
        *,
        minimum_quantity: typing.Optional[int] = None,
        value: typing.Optional["Money"] = None,
    ) -> None:
        self.minimum_quantity = minimum_quantity
        self.value = value
        super().__init__()

    def __repr__(self) -> str:
        return "PriceTier(minimum_quantity=%r, value=%r)" % (
            self.minimum_quantity,
            self.value,
        )


class ReferenceTypeId(enum.Enum):
    CART = "cart"
    CART_DISCOUNT = "cart-discount"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    CUSTOMER_GROUP = "customer-group"
    DISCOUNT_CODE = "discount-code"
    KEY_VALUE_DOCUMENT = "key-value-document"
    PAYMENT = "payment"
    PRODUCT = "product"
    PRODUCT_TYPE = "product-type"
    PRODUCT_DISCOUNT = "product-discount"
    ORDER = "order"
    REVIEW = "review"
    SHOPPING_LIST = "shopping-list"
    SHIPPING_METHOD = "shipping-method"
    STATE = "state"
    STORE = "store"
    TAX_CATEGORY = "tax-category"
    TYPE = "type"
    ZONE = "zone"
    INVENTORY_ENTRY = "inventory-entry"
    ORDER_EDIT = "order-edit"


class Resource(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ResourceSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: typing.Optional[datetime.datetime]
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        super().__init__()

    def __repr__(self) -> str:
        return "Resource(id=%r, version=%r, created_at=%r, last_modified_at=%r)" % (
            self.id,
            self.version,
            self.created_at,
            self.last_modified_at,
        )


class ResourceIdentifier(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ResourceIdentifierSchema`."
    #: Optional :class:`commercetools.types.ReferenceTypeId` `(Named` ``typeId`` `in Commercetools)`
    type_id: typing.Optional["ReferenceTypeId"]
    #: Optional :class:`str`
    id: typing.Optional[str]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
    ) -> None:
        self.type_id = type_id
        self.id = id
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return "ResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class ScopedPrice(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ScopedPriceSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: :class:`commercetools.types.TypedMoney`
    value: typing.Optional["TypedMoney"]
    #: :class:`commercetools.types.TypedMoney` `(Named` ``currentValue`` `in Commercetools)`
    current_value: typing.Optional["TypedMoney"]
    #: Optional :class:`str`
    country: typing.Optional["str"]
    #: Optional :class:`commercetools.types.CustomerGroupReference` `(Named` ``customerGroup`` `in Commercetools)`
    customer_group: typing.Optional["CustomerGroupReference"]
    #: Optional :class:`commercetools.types.ChannelReference`
    channel: typing.Optional["ChannelReference"]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]
    #: Optional :class:`commercetools.types.DiscountedPrice`
    discounted: typing.Optional["DiscountedPrice"]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        value: typing.Optional["TypedMoney"] = None,
        current_value: typing.Optional["TypedMoney"] = None,
        country: typing.Optional["str"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        channel: typing.Optional["ChannelReference"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        custom: typing.Optional["CustomFields"] = None,
    ) -> None:
        self.id = id
        self.value = value
        self.current_value = current_value
        self.country = country
        self.customer_group = customer_group
        self.channel = channel
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.discounted = discounted
        self.custom = custom
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ScopedPrice(id=%r, value=%r, current_value=%r, country=%r, customer_group=%r, channel=%r, valid_from=%r, valid_until=%r, discounted=%r, custom=%r)"
            % (
                self.id,
                self.value,
                self.current_value,
                self.country,
                self.customer_group,
                self.channel,
                self.valid_from,
                self.valid_until,
                self.discounted,
                self.custom,
            )
        )


class GeoJsonPoint(GeoJson):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.GeoJsonPointSchema`."
    #: :class:`list`
    coordinates: typing.Optional[list]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        coordinates: typing.Optional[list] = None,
    ) -> None:
        self.coordinates = coordinates
        super().__init__(type="Point", coordinates=coordinates)

    def __repr__(self) -> str:
        return "GeoJsonPoint(type=%r, coordinates=%r)" % (self.type, self.coordinates)


class Reference(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReferenceSchema`."
    #: Optional :class:`commercetools.types.ReferenceTypeId` `(Named` ``typeId`` `in Commercetools)`
    type_id: typing.Optional["ReferenceTypeId"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
    ) -> None:
        self.type_id = type_id
        super().__init__(type_id=type_id, id=id, key=key)

    def __repr__(self) -> str:
        return "Reference(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class TypedMoney(Money):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TypedMoneySchema`."
    #: :class:`commercetools.types.MoneyType`
    type: typing.Optional["MoneyType"]
    #: :class:`int` `(Named` ``fractionDigits`` `in Commercetools)`
    fraction_digits: typing.Optional[int]

    def __init__(
        self,
        *,
        cent_amount: typing.Optional[int] = None,
        currency_code: typing.Optional["str"] = None,
        type: typing.Optional["MoneyType"] = None,
        fraction_digits: typing.Optional[int] = None,
    ) -> None:
        self.type = type
        self.fraction_digits = fraction_digits
        super().__init__(cent_amount=cent_amount, currency_code=currency_code)

    def __repr__(self) -> str:
        return (
            "TypedMoney(cent_amount=%r, currency_code=%r, type=%r, fraction_digits=%r)"
            % (self.cent_amount, self.currency_code, self.type, self.fraction_digits)
        )


class CentPrecisionMoney(TypedMoney):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CentPrecisionMoneySchema`."

    def __init__(
        self,
        *,
        cent_amount: typing.Optional[int] = None,
        currency_code: typing.Optional["str"] = None,
        type: typing.Optional["MoneyType"] = None,
        fraction_digits: typing.Optional[int] = None,
    ) -> None:
        super().__init__(
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.CENT_PRECISION,
            fraction_digits=fraction_digits,
        )

    def __repr__(self) -> str:
        return (
            "CentPrecisionMoney(cent_amount=%r, currency_code=%r, type=%r, fraction_digits=%r)"
            % (self.cent_amount, self.currency_code, self.type, self.fraction_digits)
        )


class HighPrecisionMoney(TypedMoney):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.HighPrecisionMoneySchema`."
    #: :class:`int` `(Named` ``preciseAmount`` `in Commercetools)`
    precise_amount: typing.Optional[int]

    def __init__(
        self,
        *,
        cent_amount: typing.Optional[int] = None,
        currency_code: typing.Optional["str"] = None,
        type: typing.Optional["MoneyType"] = None,
        fraction_digits: typing.Optional[int] = None,
        precise_amount: typing.Optional[int] = None,
    ) -> None:
        self.precise_amount = precise_amount
        super().__init__(
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.HIGH_PRECISION,
            fraction_digits=fraction_digits,
        )

    def __repr__(self) -> str:
        return (
            "HighPrecisionMoney(cent_amount=%r, currency_code=%r, type=%r, fraction_digits=%r, precise_amount=%r)"
            % (
                self.cent_amount,
                self.currency_code,
                self.type,
                self.fraction_digits,
                self.precise_amount,
            )
        )
