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


class ContactActivityActivitiesFields(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of contacts activities to include in the report
    """


    class MetaOapg:
        required = {
            "automation_event",
            "cellphone_field_disable",
            "web_push_bounce",
            "social_share",
            "double_optin_resend",
            "email_field_enable",
            "unsubscribe",
            "web_push_send",
            "resubscription",
            "web_push_subscription",
            "unsubscribe_manual",
            "phone_field_disable",
            "push_received",
            "push_send",
            "email_spam_complaint",
            "email_hard_bounce",
            "web_push_unsubscription",
            "invitation_send",
            "double_optin",
            "opens",
            "push_canceled",
            "edit_subscription",
            "voice_send",
            "subscription",
            "push_unsubscription",
            "forget_subscription",
            "unsubscribe_reason",
            "email_send",
            "voice_report",
            "email_field_disable",
            "email_soft_bounce",
            "push_error",
            "web_push_open",
            "sms_report",
            "conversion",
            "cellphone_field_enable",
            "unsubscribe_api",
            "push_open",
            "invitation_open",
            "facebook_like",
            "change_consent",
            "web_push_click",
            "web_push_delivered",
            "double_optedit",
            "push_delivered",
            "reply_to_email",
            "sms_send",
            "clicks",
            "recommends",
            "phone_field_enable",
        }
        
        class properties:
            opens = schemas.BoolSchema
            clicks = schemas.BoolSchema
            recommends = schemas.BoolSchema
            conversion = schemas.BoolSchema
            email_send = schemas.BoolSchema
            sms_send = schemas.BoolSchema
            sms_report = schemas.BoolSchema
            voice_send = schemas.BoolSchema
            voice_report = schemas.BoolSchema
            invitation_send = schemas.BoolSchema
            invitation_open = schemas.BoolSchema
            unsubscribe = schemas.BoolSchema
            email_soft_bounce = schemas.BoolSchema
            email_hard_bounce = schemas.BoolSchema
            subscription = schemas.BoolSchema
            resubscription = schemas.BoolSchema
            unsubscribe_reason = schemas.BoolSchema
            facebook_like = schemas.BoolSchema
            social_share = schemas.BoolSchema
            unsubscribe_manual = schemas.BoolSchema
            double_optin = schemas.BoolSchema
            email_spam_complaint = schemas.BoolSchema
            email_field_disable = schemas.BoolSchema
            cellphone_field_disable = schemas.BoolSchema
            phone_field_disable = schemas.BoolSchema
            unsubscribe_api = schemas.BoolSchema
            email_field_enable = schemas.BoolSchema
            cellphone_field_enable = schemas.BoolSchema
            phone_field_enable = schemas.BoolSchema
            edit_subscription = schemas.BoolSchema
            automation_event = schemas.BoolSchema
            push_send = schemas.BoolSchema
            push_delivered = schemas.BoolSchema
            push_error = schemas.BoolSchema
            push_received = schemas.BoolSchema
            push_open = schemas.BoolSchema
            push_canceled = schemas.BoolSchema
            push_unsubscription = schemas.BoolSchema
            reply_to_email = schemas.BoolSchema
            web_push_send = schemas.BoolSchema
            web_push_delivered = schemas.BoolSchema
            web_push_open = schemas.BoolSchema
            web_push_bounce = schemas.BoolSchema
            web_push_click = schemas.BoolSchema
            web_push_subscription = schemas.BoolSchema
            web_push_unsubscription = schemas.BoolSchema
            forget_subscription = schemas.BoolSchema
            change_consent = schemas.BoolSchema
            double_optin_resend = schemas.BoolSchema
            double_optedit = schemas.BoolSchema
            __annotations__ = {
                "opens": opens,
                "clicks": clicks,
                "recommends": recommends,
                "conversion": conversion,
                "email_send": email_send,
                "sms_send": sms_send,
                "sms_report": sms_report,
                "voice_send": voice_send,
                "voice_report": voice_report,
                "invitation_send": invitation_send,
                "invitation_open": invitation_open,
                "unsubscribe": unsubscribe,
                "email_soft_bounce": email_soft_bounce,
                "email_hard_bounce": email_hard_bounce,
                "subscription": subscription,
                "resubscription": resubscription,
                "unsubscribe_reason": unsubscribe_reason,
                "facebook_like": facebook_like,
                "social_share": social_share,
                "unsubscribe_manual": unsubscribe_manual,
                "double_optin": double_optin,
                "email_spam_complaint": email_spam_complaint,
                "email_field_disable": email_field_disable,
                "cellphone_field_disable": cellphone_field_disable,
                "phone_field_disable": phone_field_disable,
                "unsubscribe_api": unsubscribe_api,
                "email_field_enable": email_field_enable,
                "cellphone_field_enable": cellphone_field_enable,
                "phone_field_enable": phone_field_enable,
                "edit_subscription": edit_subscription,
                "automation_event": automation_event,
                "push_send": push_send,
                "push_delivered": push_delivered,
                "push_error": push_error,
                "push_received": push_received,
                "push_open": push_open,
                "push_canceled": push_canceled,
                "push_unsubscription": push_unsubscription,
                "reply_to_email": reply_to_email,
                "web_push_send": web_push_send,
                "web_push_delivered": web_push_delivered,
                "web_push_open": web_push_open,
                "web_push_bounce": web_push_bounce,
                "web_push_click": web_push_click,
                "web_push_subscription": web_push_subscription,
                "web_push_unsubscription": web_push_unsubscription,
                "forget_subscription": forget_subscription,
                "change_consent": change_consent,
                "double_optin_resend": double_optin_resend,
                "double_optedit": double_optedit,
            }
    
    automation_event: MetaOapg.properties.automation_event
    cellphone_field_disable: MetaOapg.properties.cellphone_field_disable
    web_push_bounce: MetaOapg.properties.web_push_bounce
    social_share: MetaOapg.properties.social_share
    double_optin_resend: MetaOapg.properties.double_optin_resend
    email_field_enable: MetaOapg.properties.email_field_enable
    unsubscribe: MetaOapg.properties.unsubscribe
    web_push_send: MetaOapg.properties.web_push_send
    resubscription: MetaOapg.properties.resubscription
    web_push_subscription: MetaOapg.properties.web_push_subscription
    unsubscribe_manual: MetaOapg.properties.unsubscribe_manual
    phone_field_disable: MetaOapg.properties.phone_field_disable
    push_received: MetaOapg.properties.push_received
    push_send: MetaOapg.properties.push_send
    email_spam_complaint: MetaOapg.properties.email_spam_complaint
    email_hard_bounce: MetaOapg.properties.email_hard_bounce
    web_push_unsubscription: MetaOapg.properties.web_push_unsubscription
    invitation_send: MetaOapg.properties.invitation_send
    double_optin: MetaOapg.properties.double_optin
    opens: MetaOapg.properties.opens
    push_canceled: MetaOapg.properties.push_canceled
    edit_subscription: MetaOapg.properties.edit_subscription
    voice_send: MetaOapg.properties.voice_send
    subscription: MetaOapg.properties.subscription
    push_unsubscription: MetaOapg.properties.push_unsubscription
    forget_subscription: MetaOapg.properties.forget_subscription
    unsubscribe_reason: MetaOapg.properties.unsubscribe_reason
    email_send: MetaOapg.properties.email_send
    voice_report: MetaOapg.properties.voice_report
    email_field_disable: MetaOapg.properties.email_field_disable
    email_soft_bounce: MetaOapg.properties.email_soft_bounce
    push_error: MetaOapg.properties.push_error
    web_push_open: MetaOapg.properties.web_push_open
    sms_report: MetaOapg.properties.sms_report
    conversion: MetaOapg.properties.conversion
    cellphone_field_enable: MetaOapg.properties.cellphone_field_enable
    unsubscribe_api: MetaOapg.properties.unsubscribe_api
    push_open: MetaOapg.properties.push_open
    invitation_open: MetaOapg.properties.invitation_open
    facebook_like: MetaOapg.properties.facebook_like
    change_consent: MetaOapg.properties.change_consent
    web_push_click: MetaOapg.properties.web_push_click
    web_push_delivered: MetaOapg.properties.web_push_delivered
    double_optedit: MetaOapg.properties.double_optedit
    push_delivered: MetaOapg.properties.push_delivered
    reply_to_email: MetaOapg.properties.reply_to_email
    sms_send: MetaOapg.properties.sms_send
    clicks: MetaOapg.properties.clicks
    recommends: MetaOapg.properties.recommends
    phone_field_enable: MetaOapg.properties.phone_field_enable
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opens"]) -> MetaOapg.properties.opens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommends"]) -> MetaOapg.properties.recommends: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversion"]) -> MetaOapg.properties.conversion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_send"]) -> MetaOapg.properties.email_send: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sms_send"]) -> MetaOapg.properties.sms_send: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sms_report"]) -> MetaOapg.properties.sms_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_send"]) -> MetaOapg.properties.voice_send: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_report"]) -> MetaOapg.properties.voice_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invitation_send"]) -> MetaOapg.properties.invitation_send: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invitation_open"]) -> MetaOapg.properties.invitation_open: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribe"]) -> MetaOapg.properties.unsubscribe: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_soft_bounce"]) -> MetaOapg.properties.email_soft_bounce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_hard_bounce"]) -> MetaOapg.properties.email_hard_bounce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> MetaOapg.properties.subscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resubscription"]) -> MetaOapg.properties.resubscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribe_reason"]) -> MetaOapg.properties.unsubscribe_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["facebook_like"]) -> MetaOapg.properties.facebook_like: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_share"]) -> MetaOapg.properties.social_share: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribe_manual"]) -> MetaOapg.properties.unsubscribe_manual: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double_optin"]) -> MetaOapg.properties.double_optin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_spam_complaint"]) -> MetaOapg.properties.email_spam_complaint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_field_disable"]) -> MetaOapg.properties.email_field_disable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cellphone_field_disable"]) -> MetaOapg.properties.cellphone_field_disable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_field_disable"]) -> MetaOapg.properties.phone_field_disable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribe_api"]) -> MetaOapg.properties.unsubscribe_api: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_field_enable"]) -> MetaOapg.properties.email_field_enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cellphone_field_enable"]) -> MetaOapg.properties.cellphone_field_enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_field_enable"]) -> MetaOapg.properties.phone_field_enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_subscription"]) -> MetaOapg.properties.edit_subscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automation_event"]) -> MetaOapg.properties.automation_event: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_send"]) -> MetaOapg.properties.push_send: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_delivered"]) -> MetaOapg.properties.push_delivered: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_error"]) -> MetaOapg.properties.push_error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_received"]) -> MetaOapg.properties.push_received: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_open"]) -> MetaOapg.properties.push_open: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_canceled"]) -> MetaOapg.properties.push_canceled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["push_unsubscription"]) -> MetaOapg.properties.push_unsubscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reply_to_email"]) -> MetaOapg.properties.reply_to_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_send"]) -> MetaOapg.properties.web_push_send: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_delivered"]) -> MetaOapg.properties.web_push_delivered: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_open"]) -> MetaOapg.properties.web_push_open: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_bounce"]) -> MetaOapg.properties.web_push_bounce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_click"]) -> MetaOapg.properties.web_push_click: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_subscription"]) -> MetaOapg.properties.web_push_subscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_push_unsubscription"]) -> MetaOapg.properties.web_push_unsubscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forget_subscription"]) -> MetaOapg.properties.forget_subscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["change_consent"]) -> MetaOapg.properties.change_consent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double_optin_resend"]) -> MetaOapg.properties.double_optin_resend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double_optedit"]) -> MetaOapg.properties.double_optedit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["opens", "clicks", "recommends", "conversion", "email_send", "sms_send", "sms_report", "voice_send", "voice_report", "invitation_send", "invitation_open", "unsubscribe", "email_soft_bounce", "email_hard_bounce", "subscription", "resubscription", "unsubscribe_reason", "facebook_like", "social_share", "unsubscribe_manual", "double_optin", "email_spam_complaint", "email_field_disable", "cellphone_field_disable", "phone_field_disable", "unsubscribe_api", "email_field_enable", "cellphone_field_enable", "phone_field_enable", "edit_subscription", "automation_event", "push_send", "push_delivered", "push_error", "push_received", "push_open", "push_canceled", "push_unsubscription", "reply_to_email", "web_push_send", "web_push_delivered", "web_push_open", "web_push_bounce", "web_push_click", "web_push_subscription", "web_push_unsubscription", "forget_subscription", "change_consent", "double_optin_resend", "double_optedit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opens"]) -> MetaOapg.properties.opens: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommends"]) -> MetaOapg.properties.recommends: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversion"]) -> MetaOapg.properties.conversion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_send"]) -> MetaOapg.properties.email_send: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sms_send"]) -> MetaOapg.properties.sms_send: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sms_report"]) -> MetaOapg.properties.sms_report: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_send"]) -> MetaOapg.properties.voice_send: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_report"]) -> MetaOapg.properties.voice_report: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invitation_send"]) -> MetaOapg.properties.invitation_send: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invitation_open"]) -> MetaOapg.properties.invitation_open: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribe"]) -> MetaOapg.properties.unsubscribe: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_soft_bounce"]) -> MetaOapg.properties.email_soft_bounce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_hard_bounce"]) -> MetaOapg.properties.email_hard_bounce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> MetaOapg.properties.subscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resubscription"]) -> MetaOapg.properties.resubscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribe_reason"]) -> MetaOapg.properties.unsubscribe_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["facebook_like"]) -> MetaOapg.properties.facebook_like: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_share"]) -> MetaOapg.properties.social_share: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribe_manual"]) -> MetaOapg.properties.unsubscribe_manual: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double_optin"]) -> MetaOapg.properties.double_optin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_spam_complaint"]) -> MetaOapg.properties.email_spam_complaint: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_field_disable"]) -> MetaOapg.properties.email_field_disable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cellphone_field_disable"]) -> MetaOapg.properties.cellphone_field_disable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_field_disable"]) -> MetaOapg.properties.phone_field_disable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribe_api"]) -> MetaOapg.properties.unsubscribe_api: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_field_enable"]) -> MetaOapg.properties.email_field_enable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cellphone_field_enable"]) -> MetaOapg.properties.cellphone_field_enable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_field_enable"]) -> MetaOapg.properties.phone_field_enable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_subscription"]) -> MetaOapg.properties.edit_subscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automation_event"]) -> MetaOapg.properties.automation_event: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_send"]) -> MetaOapg.properties.push_send: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_delivered"]) -> MetaOapg.properties.push_delivered: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_error"]) -> MetaOapg.properties.push_error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_received"]) -> MetaOapg.properties.push_received: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_open"]) -> MetaOapg.properties.push_open: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_canceled"]) -> MetaOapg.properties.push_canceled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["push_unsubscription"]) -> MetaOapg.properties.push_unsubscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reply_to_email"]) -> MetaOapg.properties.reply_to_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_send"]) -> MetaOapg.properties.web_push_send: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_delivered"]) -> MetaOapg.properties.web_push_delivered: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_open"]) -> MetaOapg.properties.web_push_open: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_bounce"]) -> MetaOapg.properties.web_push_bounce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_click"]) -> MetaOapg.properties.web_push_click: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_subscription"]) -> MetaOapg.properties.web_push_subscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_push_unsubscription"]) -> MetaOapg.properties.web_push_unsubscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forget_subscription"]) -> MetaOapg.properties.forget_subscription: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["change_consent"]) -> MetaOapg.properties.change_consent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double_optin_resend"]) -> MetaOapg.properties.double_optin_resend: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double_optedit"]) -> MetaOapg.properties.double_optedit: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["opens", "clicks", "recommends", "conversion", "email_send", "sms_send", "sms_report", "voice_send", "voice_report", "invitation_send", "invitation_open", "unsubscribe", "email_soft_bounce", "email_hard_bounce", "subscription", "resubscription", "unsubscribe_reason", "facebook_like", "social_share", "unsubscribe_manual", "double_optin", "email_spam_complaint", "email_field_disable", "cellphone_field_disable", "phone_field_disable", "unsubscribe_api", "email_field_enable", "cellphone_field_enable", "phone_field_enable", "edit_subscription", "automation_event", "push_send", "push_delivered", "push_error", "push_received", "push_open", "push_canceled", "push_unsubscription", "reply_to_email", "web_push_send", "web_push_delivered", "web_push_open", "web_push_bounce", "web_push_click", "web_push_subscription", "web_push_unsubscription", "forget_subscription", "change_consent", "double_optin_resend", "double_optedit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        automation_event: typing.Union[MetaOapg.properties.automation_event, bool, ],
        cellphone_field_disable: typing.Union[MetaOapg.properties.cellphone_field_disable, bool, ],
        web_push_bounce: typing.Union[MetaOapg.properties.web_push_bounce, bool, ],
        social_share: typing.Union[MetaOapg.properties.social_share, bool, ],
        double_optin_resend: typing.Union[MetaOapg.properties.double_optin_resend, bool, ],
        email_field_enable: typing.Union[MetaOapg.properties.email_field_enable, bool, ],
        unsubscribe: typing.Union[MetaOapg.properties.unsubscribe, bool, ],
        web_push_send: typing.Union[MetaOapg.properties.web_push_send, bool, ],
        resubscription: typing.Union[MetaOapg.properties.resubscription, bool, ],
        web_push_subscription: typing.Union[MetaOapg.properties.web_push_subscription, bool, ],
        unsubscribe_manual: typing.Union[MetaOapg.properties.unsubscribe_manual, bool, ],
        phone_field_disable: typing.Union[MetaOapg.properties.phone_field_disable, bool, ],
        push_received: typing.Union[MetaOapg.properties.push_received, bool, ],
        push_send: typing.Union[MetaOapg.properties.push_send, bool, ],
        email_spam_complaint: typing.Union[MetaOapg.properties.email_spam_complaint, bool, ],
        email_hard_bounce: typing.Union[MetaOapg.properties.email_hard_bounce, bool, ],
        web_push_unsubscription: typing.Union[MetaOapg.properties.web_push_unsubscription, bool, ],
        invitation_send: typing.Union[MetaOapg.properties.invitation_send, bool, ],
        double_optin: typing.Union[MetaOapg.properties.double_optin, bool, ],
        opens: typing.Union[MetaOapg.properties.opens, bool, ],
        push_canceled: typing.Union[MetaOapg.properties.push_canceled, bool, ],
        edit_subscription: typing.Union[MetaOapg.properties.edit_subscription, bool, ],
        voice_send: typing.Union[MetaOapg.properties.voice_send, bool, ],
        subscription: typing.Union[MetaOapg.properties.subscription, bool, ],
        push_unsubscription: typing.Union[MetaOapg.properties.push_unsubscription, bool, ],
        forget_subscription: typing.Union[MetaOapg.properties.forget_subscription, bool, ],
        unsubscribe_reason: typing.Union[MetaOapg.properties.unsubscribe_reason, bool, ],
        email_send: typing.Union[MetaOapg.properties.email_send, bool, ],
        voice_report: typing.Union[MetaOapg.properties.voice_report, bool, ],
        email_field_disable: typing.Union[MetaOapg.properties.email_field_disable, bool, ],
        email_soft_bounce: typing.Union[MetaOapg.properties.email_soft_bounce, bool, ],
        push_error: typing.Union[MetaOapg.properties.push_error, bool, ],
        web_push_open: typing.Union[MetaOapg.properties.web_push_open, bool, ],
        sms_report: typing.Union[MetaOapg.properties.sms_report, bool, ],
        conversion: typing.Union[MetaOapg.properties.conversion, bool, ],
        cellphone_field_enable: typing.Union[MetaOapg.properties.cellphone_field_enable, bool, ],
        unsubscribe_api: typing.Union[MetaOapg.properties.unsubscribe_api, bool, ],
        push_open: typing.Union[MetaOapg.properties.push_open, bool, ],
        invitation_open: typing.Union[MetaOapg.properties.invitation_open, bool, ],
        facebook_like: typing.Union[MetaOapg.properties.facebook_like, bool, ],
        change_consent: typing.Union[MetaOapg.properties.change_consent, bool, ],
        web_push_click: typing.Union[MetaOapg.properties.web_push_click, bool, ],
        web_push_delivered: typing.Union[MetaOapg.properties.web_push_delivered, bool, ],
        double_optedit: typing.Union[MetaOapg.properties.double_optedit, bool, ],
        push_delivered: typing.Union[MetaOapg.properties.push_delivered, bool, ],
        reply_to_email: typing.Union[MetaOapg.properties.reply_to_email, bool, ],
        sms_send: typing.Union[MetaOapg.properties.sms_send, bool, ],
        clicks: typing.Union[MetaOapg.properties.clicks, bool, ],
        recommends: typing.Union[MetaOapg.properties.recommends, bool, ],
        phone_field_enable: typing.Union[MetaOapg.properties.phone_field_enable, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContactActivityActivitiesFields':
        return super().__new__(
            cls,
            *args,
            automation_event=automation_event,
            cellphone_field_disable=cellphone_field_disable,
            web_push_bounce=web_push_bounce,
            social_share=social_share,
            double_optin_resend=double_optin_resend,
            email_field_enable=email_field_enable,
            unsubscribe=unsubscribe,
            web_push_send=web_push_send,
            resubscription=resubscription,
            web_push_subscription=web_push_subscription,
            unsubscribe_manual=unsubscribe_manual,
            phone_field_disable=phone_field_disable,
            push_received=push_received,
            push_send=push_send,
            email_spam_complaint=email_spam_complaint,
            email_hard_bounce=email_hard_bounce,
            web_push_unsubscription=web_push_unsubscription,
            invitation_send=invitation_send,
            double_optin=double_optin,
            opens=opens,
            push_canceled=push_canceled,
            edit_subscription=edit_subscription,
            voice_send=voice_send,
            subscription=subscription,
            push_unsubscription=push_unsubscription,
            forget_subscription=forget_subscription,
            unsubscribe_reason=unsubscribe_reason,
            email_send=email_send,
            voice_report=voice_report,
            email_field_disable=email_field_disable,
            email_soft_bounce=email_soft_bounce,
            push_error=push_error,
            web_push_open=web_push_open,
            sms_report=sms_report,
            conversion=conversion,
            cellphone_field_enable=cellphone_field_enable,
            unsubscribe_api=unsubscribe_api,
            push_open=push_open,
            invitation_open=invitation_open,
            facebook_like=facebook_like,
            change_consent=change_consent,
            web_push_click=web_push_click,
            web_push_delivered=web_push_delivered,
            double_optedit=double_optedit,
            push_delivered=push_delivered,
            reply_to_email=reply_to_email,
            sms_send=sms_send,
            clicks=clicks,
            recommends=recommends,
            phone_field_enable=phone_field_enable,
            _configuration=_configuration,
            **kwargs,
        )
