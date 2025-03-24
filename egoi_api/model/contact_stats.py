# coding: utf-8

"""
    Marketing API

     # Introduction Welcome to the E-goi Marketing API! <br><br>This API enables you to integrate, automate, and manage all the marketing functionalities offered by E-goi. With it, you can interact with contact lists, send email campaigns, SMS, push notifications, and much more. <br><br>Our API is designed to simplify integration in a straightforward, efficient, and secure way, meeting the needs of developers and businesses looking to optimize their digital marketing operations. <br><br>Explore the documentation to discover all the possibilities and start creating integrations that drive your marketing results. # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.  The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.      BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Transport Layer Security (TLS) Transport Layer Security (TLS) is a widely used authentication and encryption protocol that establishes a secure communications channel for data-in-transit while ensuring that the client and server can validate one another.<br> Our API requires TLS 1.2 or TLS 1.3. We recommend <b>TLS 1.3</b>.<br><br> <b>TLS 1.3 ciphers</b> * TLS_AES_256_GCM_SHA384 (0x1302) ECDH x25519 (eq. 3072 bits RSA) FS * TLS_CHACHA20_POLY1305_SHA256 (0x1303) ECDH x25519 (eq. 3072 bits RSA) FS * TLS_AES_128_GCM_SHA256 (0x1301) ECDH x25519 (eq. 3072 bits RSA) FS  <b>TLS 1.2 ciphers</b> * TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030) ECDH x25519 (eq. 3072 bits RSA) FS * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f) ECDH x25519 (eq. 3072 bits RSA) FS * TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (0x9f) DH 4096 bits FS * TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (0x9e) DH 4096 bits FS  # Rate Limits Rate limits are used to control the amount of traffic that is allowed to flow between the client and the server.<br> This is done to prevent abuse and ensure that the API is available to all users.<br> The rate limits are applied to ensure the stability and security of our API and are based on the number of requests made in a given time period.<br> If the rate limit is exceeded, the API will return a 429 status code and the request will be rejected.<br> Each API response includes headers providing real-time rate limit information: * **X-RateLimit-Limit**: The maximum number of requests that the consumer is permitted to make in a given time period. * **X-RateLimit-Remaining**: The number of requests remaining in the current rate limit window. * **X-RateLimit-Reset**: The remaining time in seconds until the rate limit window resets.  # Account Limit The account limit is a rate limit that is applied to the account as a whole.<br> This limit is applied to all requests made by the account, regardless of the client making the request.<br> The account limit is applied to ensure that the account does not exceed the maximum number of requests allowed in a given time period. Each account has an overall usage limit per hour. If the account limit is exceeded, the API will return a 429 status code and the request will be rejected.<br> Each API response includes headers providing real-time rate limit information: * **X-Account-Limit**: The maximum number of requests that the account is permitted to make in a given time period. * **X-Account-Remaining**: The number of requests remaining in the current rate limit window. * **X-Account-Reset**: The remaining time in seconds until the rate limit window resets.   # Authentication  We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:     #!/bin/bash     curl -X GET 'https://api.egoiapp.com/my-account' \\     -H 'accept: application/json' \\     -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:     #!/bin/bash     curl -X POST 'http://api.egoiapp.com/tags' \\     -H 'accept: application/json' \\     -H 'Apikey: <YOUR_APY_KEY>' \\     -H 'Content-Type: application/json' \\     -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services.  * <a href='https://github.com/E-goi/sdk-java'>Java</a>  * <a href='https://github.com/E-goi/sdk-php'>PHP</a>  * <a href='https://github.com/E-goi/sdk-python'>Python</a>  * <a href='https://github.com/E-goi/sdk-ruby'>Ruby</a>  * <a href='https://github.com/E-goi/sdk-javascript'>Javascript</a>  * <a href='https://github.com/E-goi/sdk-csharp'>C#</a>  # Stream Limits Stream limits are security mesures we have to make sure our API have a fair use policy, for this reason, any request that creates or modifies data (**POST**, **PATCH** and **PUT**) is limited to a maximum of **20MB** of content length. If you arrive to this limit in one of your request, you'll receive a HTTP code **413 (Request Entity Too Large)** and the request will be ignored. To avoid this error in importation's requests, it's advised the request's division in batches that have each one less than 20MB.  # Timeouts Timeouts set a maximum waiting time on a request's response. Our API, sets a default timeout for each request and when breached, you'll receive an HTTP **408 (Request Timeout)** error code. You should take into consideration that response times can vary widely based on the complexity of the request, amount of data being analyzed, and the load on the system and workspace at the time of the query. When dealing with such errors, you should first attempt to reduce the complexity and amount of data under analysis, and only then, if problems are still occurring ask for support.  For all these reasons, the default timeout for each request is **10 Seconds** and any request that creates or modifies data (**POST**, **PATCH** and **PUT**) will have a timeout of **60 Seconds**. Specific timeouts may exist for specific requests, these can be found in the request's documentation.  # Callbacks A callback is an asynchronous API request that originates from the API server and is sent to the client in response to a previous request sent by that client.  The API will make a **POST** request to the address defined in the URL with the information regarding the event of interest and share data related to that event.  <a href='/usecases/callbacks/' target='_blank'>[Go to callbacks documentation]</a>  ***Note:*** Only http or https protocols are supported in the Url parameter.  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: V3
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from egoi_api import schemas  # noqa: F401


class ContactStats(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Contact stats
    """


    class MetaOapg:
        
        class properties:
            
            
            class email_stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sent = schemas.IntSchema
                        opens = schemas.IntSchema
                        clicks = schemas.IntSchema
                        soft_bounces = schemas.IntSchema
                        hard_bounces = schemas.IntSchema
                        forwards = schemas.IntSchema
                        conversions = schemas.IntSchema
                        social_actions = schemas.IntSchema
                        
                        
                        class last_send_date(
                            schemas.DateTimeBase,
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'date-time'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, datetime, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_send_date':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last_open_date(
                            schemas.DateTimeBase,
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'date-time'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, datetime, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_open_date':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last_click_date(
                            schemas.DateTimeBase,
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'date-time'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, datetime, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_click_date':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last_open_country(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_open_country':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last_open_region(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_open_region':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last_open_city(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_open_city':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "sent": sent,
                            "opens": opens,
                            "clicks": clicks,
                            "soft_bounces": soft_bounces,
                            "hard_bounces": hard_bounces,
                            "forwards": forwards,
                            "conversions": conversions,
                            "social_actions": social_actions,
                            "last_send_date": last_send_date,
                            "last_open_date": last_open_date,
                            "last_click_date": last_click_date,
                            "last_open_country": last_open_country,
                            "last_open_region": last_open_region,
                            "last_open_city": last_open_city,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sent"]) -> MetaOapg.properties.sent: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["opens"]) -> MetaOapg.properties.opens: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["soft_bounces"]) -> MetaOapg.properties.soft_bounces: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["hard_bounces"]) -> MetaOapg.properties.hard_bounces: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["forwards"]) -> MetaOapg.properties.forwards: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["conversions"]) -> MetaOapg.properties.conversions: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["social_actions"]) -> MetaOapg.properties.social_actions: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_send_date"]) -> MetaOapg.properties.last_send_date: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_open_date"]) -> MetaOapg.properties.last_open_date: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_click_date"]) -> MetaOapg.properties.last_click_date: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_open_country"]) -> MetaOapg.properties.last_open_country: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_open_region"]) -> MetaOapg.properties.last_open_region: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_open_city"]) -> MetaOapg.properties.last_open_city: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sent", "opens", "clicks", "soft_bounces", "hard_bounces", "forwards", "conversions", "social_actions", "last_send_date", "last_open_date", "last_click_date", "last_open_country", "last_open_region", "last_open_city", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sent"]) -> typing.Union[MetaOapg.properties.sent, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["opens"]) -> typing.Union[MetaOapg.properties.opens, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["clicks"]) -> typing.Union[MetaOapg.properties.clicks, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["soft_bounces"]) -> typing.Union[MetaOapg.properties.soft_bounces, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["hard_bounces"]) -> typing.Union[MetaOapg.properties.hard_bounces, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["forwards"]) -> typing.Union[MetaOapg.properties.forwards, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["conversions"]) -> typing.Union[MetaOapg.properties.conversions, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["social_actions"]) -> typing.Union[MetaOapg.properties.social_actions, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_send_date"]) -> typing.Union[MetaOapg.properties.last_send_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_open_date"]) -> typing.Union[MetaOapg.properties.last_open_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_click_date"]) -> typing.Union[MetaOapg.properties.last_click_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_open_country"]) -> typing.Union[MetaOapg.properties.last_open_country, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_open_region"]) -> typing.Union[MetaOapg.properties.last_open_region, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_open_city"]) -> typing.Union[MetaOapg.properties.last_open_city, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sent", "opens", "clicks", "soft_bounces", "hard_bounces", "forwards", "conversions", "social_actions", "last_send_date", "last_open_date", "last_click_date", "last_open_country", "last_open_region", "last_open_city", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    sent: typing.Union[MetaOapg.properties.sent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    opens: typing.Union[MetaOapg.properties.opens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    clicks: typing.Union[MetaOapg.properties.clicks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    soft_bounces: typing.Union[MetaOapg.properties.soft_bounces, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    hard_bounces: typing.Union[MetaOapg.properties.hard_bounces, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    forwards: typing.Union[MetaOapg.properties.forwards, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    conversions: typing.Union[MetaOapg.properties.conversions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    social_actions: typing.Union[MetaOapg.properties.social_actions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    last_send_date: typing.Union[MetaOapg.properties.last_send_date, None, str, datetime, schemas.Unset] = schemas.unset,
                    last_open_date: typing.Union[MetaOapg.properties.last_open_date, None, str, datetime, schemas.Unset] = schemas.unset,
                    last_click_date: typing.Union[MetaOapg.properties.last_click_date, None, str, datetime, schemas.Unset] = schemas.unset,
                    last_open_country: typing.Union[MetaOapg.properties.last_open_country, None, str, schemas.Unset] = schemas.unset,
                    last_open_region: typing.Union[MetaOapg.properties.last_open_region, None, str, schemas.Unset] = schemas.unset,
                    last_open_city: typing.Union[MetaOapg.properties.last_open_city, None, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'email_stats':
                    return super().__new__(
                        cls,
                        *args,
                        sent=sent,
                        opens=opens,
                        clicks=clicks,
                        soft_bounces=soft_bounces,
                        hard_bounces=hard_bounces,
                        forwards=forwards,
                        conversions=conversions,
                        social_actions=social_actions,
                        last_send_date=last_send_date,
                        last_open_date=last_open_date,
                        last_click_date=last_click_date,
                        last_open_country=last_open_country,
                        last_open_region=last_open_region,
                        last_open_city=last_open_city,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class sms_stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sent = schemas.IntSchema
                        delivered = schemas.IntSchema
                        __annotations__ = {
                            "sent": sent,
                            "delivered": delivered,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sent"]) -> MetaOapg.properties.sent: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["delivered"]) -> MetaOapg.properties.delivered: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sent", "delivered", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sent"]) -> typing.Union[MetaOapg.properties.sent, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["delivered"]) -> typing.Union[MetaOapg.properties.delivered, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sent", "delivered", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    sent: typing.Union[MetaOapg.properties.sent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    delivered: typing.Union[MetaOapg.properties.delivered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sms_stats':
                    return super().__new__(
                        cls,
                        *args,
                        sent=sent,
                        delivered=delivered,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class push_stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sent = schemas.IntSchema
                        delivered = schemas.IntSchema
                        not_delivered = schemas.IntSchema
                        views = schemas.IntSchema
                        clicks = schemas.IntSchema
                        
                        
                        class last_view_date(
                            schemas.DateTimeBase,
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'date-time'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, datetime, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_view_date':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "sent": sent,
                            "delivered": delivered,
                            "not_delivered": not_delivered,
                            "views": views,
                            "clicks": clicks,
                            "last_view_date": last_view_date,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sent"]) -> MetaOapg.properties.sent: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["delivered"]) -> MetaOapg.properties.delivered: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["not_delivered"]) -> MetaOapg.properties.not_delivered: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["views"]) -> MetaOapg.properties.views: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_view_date"]) -> MetaOapg.properties.last_view_date: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sent", "delivered", "not_delivered", "views", "clicks", "last_view_date", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sent"]) -> typing.Union[MetaOapg.properties.sent, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["delivered"]) -> typing.Union[MetaOapg.properties.delivered, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["not_delivered"]) -> typing.Union[MetaOapg.properties.not_delivered, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["views"]) -> typing.Union[MetaOapg.properties.views, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["clicks"]) -> typing.Union[MetaOapg.properties.clicks, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_view_date"]) -> typing.Union[MetaOapg.properties.last_view_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sent", "delivered", "not_delivered", "views", "clicks", "last_view_date", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    sent: typing.Union[MetaOapg.properties.sent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    delivered: typing.Union[MetaOapg.properties.delivered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    not_delivered: typing.Union[MetaOapg.properties.not_delivered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    views: typing.Union[MetaOapg.properties.views, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    clicks: typing.Union[MetaOapg.properties.clicks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    last_view_date: typing.Union[MetaOapg.properties.last_view_date, None, str, datetime, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'push_stats':
                    return super().__new__(
                        cls,
                        *args,
                        sent=sent,
                        delivered=delivered,
                        not_delivered=not_delivered,
                        views=views,
                        clicks=clicks,
                        last_view_date=last_view_date,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class webpush_stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sent = schemas.IntSchema
                        delivered = schemas.IntSchema
                        clicks = schemas.IntSchema
                        bounces = schemas.IntSchema
                        last_send_date = schemas.DateTimeSchema
                        last_delivery_date = schemas.DateTimeSchema
                        last_click_date = schemas.DateTimeSchema
                        last_bounce_date = schemas.DateTimeSchema
                        __annotations__ = {
                            "sent": sent,
                            "delivered": delivered,
                            "clicks": clicks,
                            "bounces": bounces,
                            "last_send_date": last_send_date,
                            "last_delivery_date": last_delivery_date,
                            "last_click_date": last_click_date,
                            "last_bounce_date": last_bounce_date,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sent"]) -> MetaOapg.properties.sent: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["delivered"]) -> MetaOapg.properties.delivered: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["bounces"]) -> MetaOapg.properties.bounces: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_send_date"]) -> MetaOapg.properties.last_send_date: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_delivery_date"]) -> MetaOapg.properties.last_delivery_date: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_click_date"]) -> MetaOapg.properties.last_click_date: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_bounce_date"]) -> MetaOapg.properties.last_bounce_date: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sent", "delivered", "clicks", "bounces", "last_send_date", "last_delivery_date", "last_click_date", "last_bounce_date", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sent"]) -> typing.Union[MetaOapg.properties.sent, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["delivered"]) -> typing.Union[MetaOapg.properties.delivered, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["clicks"]) -> typing.Union[MetaOapg.properties.clicks, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["bounces"]) -> typing.Union[MetaOapg.properties.bounces, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_send_date"]) -> typing.Union[MetaOapg.properties.last_send_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_delivery_date"]) -> typing.Union[MetaOapg.properties.last_delivery_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_click_date"]) -> typing.Union[MetaOapg.properties.last_click_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_bounce_date"]) -> typing.Union[MetaOapg.properties.last_bounce_date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sent", "delivered", "clicks", "bounces", "last_send_date", "last_delivery_date", "last_click_date", "last_bounce_date", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    sent: typing.Union[MetaOapg.properties.sent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    delivered: typing.Union[MetaOapg.properties.delivered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    clicks: typing.Union[MetaOapg.properties.clicks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    bounces: typing.Union[MetaOapg.properties.bounces, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    last_send_date: typing.Union[MetaOapg.properties.last_send_date, str, datetime, schemas.Unset] = schemas.unset,
                    last_delivery_date: typing.Union[MetaOapg.properties.last_delivery_date, str, datetime, schemas.Unset] = schemas.unset,
                    last_click_date: typing.Union[MetaOapg.properties.last_click_date, str, datetime, schemas.Unset] = schemas.unset,
                    last_bounce_date: typing.Union[MetaOapg.properties.last_bounce_date, str, datetime, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'webpush_stats':
                    return super().__new__(
                        cls,
                        *args,
                        sent=sent,
                        delivered=delivered,
                        clicks=clicks,
                        bounces=bounces,
                        last_send_date=last_send_date,
                        last_delivery_date=last_delivery_date,
                        last_click_date=last_click_date,
                        last_bounce_date=last_bounce_date,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class voice_stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        sent = schemas.IntSchema
                        answered = schemas.IntSchema
                        __annotations__ = {
                            "sent": sent,
                            "answered": answered,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sent"]) -> MetaOapg.properties.sent: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["answered"]) -> MetaOapg.properties.answered: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["sent", "answered", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sent"]) -> typing.Union[MetaOapg.properties.sent, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["answered"]) -> typing.Union[MetaOapg.properties.answered, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sent", "answered", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    sent: typing.Union[MetaOapg.properties.sent, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    answered: typing.Union[MetaOapg.properties.answered, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'voice_stats':
                    return super().__new__(
                        cls,
                        *args,
                        sent=sent,
                        answered=answered,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class traffic_stats(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class utm(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    utm_source = schemas.StrSchema
                                    utm_medium = schemas.StrSchema
                                    utm_campaign = schemas.StrSchema
                                    utm_content = schemas.StrSchema
                                    utm_term = schemas.StrSchema
                                    __annotations__ = {
                                        "utm_source": utm_source,
                                        "utm_medium": utm_medium,
                                        "utm_campaign": utm_campaign,
                                        "utm_content": utm_content,
                                        "utm_term": utm_term,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["utm_source"]) -> MetaOapg.properties.utm_source: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["utm_medium"]) -> MetaOapg.properties.utm_medium: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["utm_campaign"]) -> MetaOapg.properties.utm_campaign: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["utm_content"]) -> MetaOapg.properties.utm_content: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["utm_term"]) -> MetaOapg.properties.utm_term: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["utm_source"]) -> typing.Union[MetaOapg.properties.utm_source, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["utm_medium"]) -> typing.Union[MetaOapg.properties.utm_medium, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["utm_campaign"]) -> typing.Union[MetaOapg.properties.utm_campaign, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["utm_content"]) -> typing.Union[MetaOapg.properties.utm_content, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["utm_term"]) -> typing.Union[MetaOapg.properties.utm_term, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                utm_source: typing.Union[MetaOapg.properties.utm_source, str, schemas.Unset] = schemas.unset,
                                utm_medium: typing.Union[MetaOapg.properties.utm_medium, str, schemas.Unset] = schemas.unset,
                                utm_campaign: typing.Union[MetaOapg.properties.utm_campaign, str, schemas.Unset] = schemas.unset,
                                utm_content: typing.Union[MetaOapg.properties.utm_content, str, schemas.Unset] = schemas.unset,
                                utm_term: typing.Union[MetaOapg.properties.utm_term, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'utm':
                                return super().__new__(
                                    cls,
                                    *args,
                                    utm_source=utm_source,
                                    utm_medium=utm_medium,
                                    utm_campaign=utm_campaign,
                                    utm_content=utm_content,
                                    utm_term=utm_term,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class referrer(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    referrer = schemas.StrSchema
                                    __annotations__ = {
                                        "referrer": referrer,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["referrer"]) -> MetaOapg.properties.referrer: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["referrer", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["referrer"]) -> typing.Union[MetaOapg.properties.referrer, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["referrer", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                referrer: typing.Union[MetaOapg.properties.referrer, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'referrer':
                                return super().__new__(
                                    cls,
                                    *args,
                                    referrer=referrer,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class advertising(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    gclid = schemas.StrSchema
                                    msclkid = schemas.StrSchema
                                    fbclid = schemas.StrSchema
                                    __annotations__ = {
                                        "gclid": gclid,
                                        "msclkid": msclkid,
                                        "fbclid": fbclid,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["gclid"]) -> MetaOapg.properties.gclid: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["msclkid"]) -> MetaOapg.properties.msclkid: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["fbclid"]) -> MetaOapg.properties.fbclid: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["gclid", "msclkid", "fbclid", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["gclid"]) -> typing.Union[MetaOapg.properties.gclid, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["msclkid"]) -> typing.Union[MetaOapg.properties.msclkid, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["fbclid"]) -> typing.Union[MetaOapg.properties.fbclid, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gclid", "msclkid", "fbclid", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                gclid: typing.Union[MetaOapg.properties.gclid, str, schemas.Unset] = schemas.unset,
                                msclkid: typing.Union[MetaOapg.properties.msclkid, str, schemas.Unset] = schemas.unset,
                                fbclid: typing.Union[MetaOapg.properties.fbclid, str, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'advertising':
                                return super().__new__(
                                    cls,
                                    *args,
                                    gclid=gclid,
                                    msclkid=msclkid,
                                    fbclid=fbclid,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "utm": utm,
                            "referrer": referrer,
                            "advertising": advertising,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["utm"]) -> MetaOapg.properties.utm: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["referrer"]) -> MetaOapg.properties.referrer: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["advertising"]) -> MetaOapg.properties.advertising: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["utm", "referrer", "advertising", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["utm"]) -> typing.Union[MetaOapg.properties.utm, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["referrer"]) -> typing.Union[MetaOapg.properties.referrer, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["advertising"]) -> typing.Union[MetaOapg.properties.advertising, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["utm", "referrer", "advertising", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    utm: typing.Union[MetaOapg.properties.utm, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    referrer: typing.Union[MetaOapg.properties.referrer, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    advertising: typing.Union[MetaOapg.properties.advertising, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'traffic_stats':
                    return super().__new__(
                        cls,
                        *args,
                        utm=utm,
                        referrer=referrer,
                        advertising=advertising,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "email_stats": email_stats,
                "sms_stats": sms_stats,
                "push_stats": push_stats,
                "webpush_stats": webpush_stats,
                "voice_stats": voice_stats,
                "traffic_stats": traffic_stats,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_stats"]) -> MetaOapg.properties.email_stats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sms_stats"]) -> MetaOapg.properties.sms_stats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_stats"]) -> MetaOapg.properties.push_stats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webpush_stats"]) -> MetaOapg.properties.webpush_stats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_stats"]) -> MetaOapg.properties.voice_stats: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["traffic_stats"]) -> MetaOapg.properties.traffic_stats: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_stats", "sms_stats", "push_stats", "webpush_stats", "voice_stats", "traffic_stats", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_stats"]) -> typing.Union[MetaOapg.properties.email_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sms_stats"]) -> typing.Union[MetaOapg.properties.sms_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_stats"]) -> typing.Union[MetaOapg.properties.push_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webpush_stats"]) -> typing.Union[MetaOapg.properties.webpush_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_stats"]) -> typing.Union[MetaOapg.properties.voice_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["traffic_stats"]) -> typing.Union[MetaOapg.properties.traffic_stats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_stats", "sms_stats", "push_stats", "webpush_stats", "voice_stats", "traffic_stats", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email_stats: typing.Union[MetaOapg.properties.email_stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        sms_stats: typing.Union[MetaOapg.properties.sms_stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        push_stats: typing.Union[MetaOapg.properties.push_stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        webpush_stats: typing.Union[MetaOapg.properties.webpush_stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        voice_stats: typing.Union[MetaOapg.properties.voice_stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        traffic_stats: typing.Union[MetaOapg.properties.traffic_stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactStats':
        return super().__new__(
            cls,
            *args,
            email_stats=email_stats,
            sms_stats=sms_stats,
            push_stats=push_stats,
            webpush_stats=webpush_stats,
            voice_stats=voice_stats,
            traffic_stats=traffic_stats,
            _configuration=_configuration,
            **kwargs,
        )
