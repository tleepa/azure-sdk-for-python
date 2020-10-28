# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class DigitalTwinModelsAddOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinModelsAddOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinModelsDeleteOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinModelsDeleteOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinModelsGetByIdOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinModelsGetByIdOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinModelsListOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param max_items_per_page: The maximum number of items to retrieve per request. The server may
     choose to return less than the requested number.
    :type max_items_per_page: int
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'max_items_per_page': {'key': 'MaxItemsPerPage', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinModelsListOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.max_items_per_page = kwargs.get('max_items_per_page', None)


class DigitalTwinModelsUpdateOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinModelsUpdateOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsAddOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsAddOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsAddRelationshipOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsAddRelationshipOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsDeleteOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param if_match: Only perform the operation if the entity's etag matches one of the etags
     provided or * is provided.
    :type if_match: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'if_match': {'key': 'If-Match', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsDeleteOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.if_match = kwargs.get('if_match', None)


class DigitalTwinsDeleteRelationshipOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param if_match: Only perform the operation if the entity's etag matches one of the etags
     provided or * is provided.
    :type if_match: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'if_match': {'key': 'If-Match', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsDeleteRelationshipOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.if_match = kwargs.get('if_match', None)


class DigitalTwinsGetByIdOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsGetByIdOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsGetComponentOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsGetComponentOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsGetRelationshipByIdOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsGetRelationshipByIdOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsListIncomingRelationshipsOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsListIncomingRelationshipsOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsListRelationshipsOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsListRelationshipsOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsModelData(msrest.serialization.Model):
    """A model definition and metadata for that model.

    All required parameters must be populated in order to send to Azure.

    :param display_name: A language map that contains the localized display names as specified in
     the model definition.
    :type display_name: dict[str, str]
    :param description: A language map that contains the localized descriptions as specified in the
     model definition.
    :type description: dict[str, str]
    :param id: Required. The id of the model as specified in the model definition.
    :type id: str
    :param upload_time: The time the model was uploaded to the service.
    :type upload_time: ~datetime.datetime
    :param decommissioned: Indicates if the model is decommissioned. Decommissioned models cannot
     be referenced by newly created digital twins.
    :type decommissioned: bool
    :param model: The model definition.
    :type model: object
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': '{str}'},
        'description': {'key': 'description', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'upload_time': {'key': 'uploadTime', 'type': 'iso-8601'},
        'decommissioned': {'key': 'decommissioned', 'type': 'bool'},
        'model': {'key': 'model', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsModelData, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs['id']
        self.upload_time = kwargs.get('upload_time', None)
        self.decommissioned = kwargs.get('decommissioned', False)
        self.model = kwargs.get('model', None)


class DigitalTwinsSendComponentTelemetryOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsSendComponentTelemetryOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsSendTelemetryOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsSendTelemetryOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class DigitalTwinsUpdateComponentOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param if_match: Only perform the operation if the entity's etag matches one of the etags
     provided or * is provided.
    :type if_match: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'if_match': {'key': 'If-Match', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsUpdateComponentOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.if_match = kwargs.get('if_match', None)


class DigitalTwinsUpdateOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param if_match: Only perform the operation if the entity's etag matches one of the etags
     provided or * is provided.
    :type if_match: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'if_match': {'key': 'If-Match', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsUpdateOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.if_match = kwargs.get('if_match', None)


class DigitalTwinsUpdateRelationshipOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param if_match: Only perform the operation if the entity's etag matches one of the etags
     provided or * is provided.
    :type if_match: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'if_match': {'key': 'If-Match', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DigitalTwinsUpdateRelationshipOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.if_match = kwargs.get('if_match', None)


class Error(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: A human-readable representation of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~azure.digitaltwins.core.models.Error]
    :param innererror: An object containing more specific information than the current object about
     the error.
    :type innererror: ~azure.digitaltwins.core.models.InnerError
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None
        self.innererror = kwargs.get('innererror', None)


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: The error details.
    :type error: ~azure.digitaltwins.core.models.Error
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class EventRoute(msrest.serialization.Model):
    """A route which directs notification and telemetry events to an endpoint. Endpoints are a destination outside of Azure Digital Twins such as an EventHub.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The id of the event route.
    :vartype id: str
    :param endpoint_name: Required. The name of the endpoint this event route is bound to.
    :type endpoint_name: str
    :param filter: Required. An expression which describes the events which are routed to the
     endpoint.
    :type filter: str
    """

    _validation = {
        'id': {'readonly': True},
        'endpoint_name': {'required': True},
        'filter': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'endpoint_name': {'key': 'endpointName', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventRoute, self).__init__(**kwargs)
        self.id = None
        self.endpoint_name = kwargs['endpoint_name']
        self.filter = kwargs['filter']


class EventRouteCollection(msrest.serialization.Model):
    """A collection of EventRoute objects.

    :param value: The EventRoute objects.
    :type value: list[~azure.digitaltwins.core.models.EventRoute]
    :param next_link: A URI to retrieve the next page of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EventRoute]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventRouteCollection, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class EventRoutesAddOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventRoutesAddOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class EventRoutesDeleteOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventRoutesDeleteOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class EventRoutesGetByIdOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventRoutesGetByIdOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)


class EventRoutesListOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param max_items_per_page: The maximum number of items to retrieve per request. The server may
     choose to return less than the requested number.
    :type max_items_per_page: int
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'max_items_per_page': {'key': 'MaxItemsPerPage', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventRoutesListOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.max_items_per_page = kwargs.get('max_items_per_page', None)


class IncomingRelationship(msrest.serialization.Model):
    """An incoming relationship.

    :param relationship_id: A user-provided string representing the id of this relationship, unique
     in the context of the source digital twin, i.e. sourceId + relationshipId is unique in the
     context of the service.
    :type relationship_id: str
    :param source_id: The id of the source digital twin.
    :type source_id: str
    :param relationship_name: The name of the relationship.
    :type relationship_name: str
    :param relationship_link: Link to the relationship, to be used for deletion.
    :type relationship_link: str
    """

    _attribute_map = {
        'relationship_id': {'key': '$relationshipId', 'type': 'str'},
        'source_id': {'key': '$sourceId', 'type': 'str'},
        'relationship_name': {'key': '$relationshipName', 'type': 'str'},
        'relationship_link': {'key': '$relationshipLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(IncomingRelationship, self).__init__(**kwargs)
        self.relationship_id = kwargs.get('relationship_id', None)
        self.source_id = kwargs.get('source_id', None)
        self.relationship_name = kwargs.get('relationship_name', None)
        self.relationship_link = kwargs.get('relationship_link', None)


class IncomingRelationshipCollection(msrest.serialization.Model):
    """A collection of incoming relationships which relate digital twins together.

    :param value:
    :type value: list[~azure.digitaltwins.core.models.IncomingRelationship]
    :param next_link: A URI to retrieve the next page of objects.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[IncomingRelationship]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(IncomingRelationshipCollection, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class InnerError(msrest.serialization.Model):
    """A more specific error description than was provided by the containing error.

    :param code: A more specific error code than was provided by the containing error.
    :type code: str
    :param innererror: An object containing more specific information than the current object about
     the error.
    :type innererror: ~azure.digitaltwins.core.models.InnerError
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InnerError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.innererror = kwargs.get('innererror', None)


class PagedDigitalTwinsModelDataCollection(msrest.serialization.Model):
    """A collection of DigitalTwinsModelData objects.

    :param value: The DigitalTwinsModelData objects.
    :type value: list[~azure.digitaltwins.core.models.DigitalTwinsModelData]
    :param next_link: A URI to retrieve the next page of objects.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DigitalTwinsModelData]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PagedDigitalTwinsModelDataCollection, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class QueryResult(msrest.serialization.Model):
    """The results of a query operation and an optional continuation token.

    :param value: The query results.
    :type value: list[object]
    :param continuation_token: A token which can be used to construct a new QuerySpecification to
     retrieve the next set of results.
    :type continuation_token: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[object]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueryResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.continuation_token = kwargs.get('continuation_token', None)


class QuerySpecification(msrest.serialization.Model):
    """A query specification containing either a query statement or a continuation token from a previous query result.

    :param query: The query to execute. This value is ignored if a continuation token is provided.
    :type query: str
    :param continuation_token: A token which is used to retrieve the next set of results from a
     previous query.
    :type continuation_token: str
    """

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuerySpecification, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.continuation_token = kwargs.get('continuation_token', None)


class QueryTwinsOptions(msrest.serialization.Model):
    """Parameter group.

    :param traceparent: Identifies the request in a distributed tracing system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification information and is a companion
     to traceparent.
    :type tracestate: str
    :param max_items_per_page: The maximum number of items to retrieve per request. The server may
     choose to return less than the requested number.
    :type max_items_per_page: int
    """

    _attribute_map = {
        'traceparent': {'key': 'traceparent', 'type': 'str'},
        'tracestate': {'key': 'tracestate', 'type': 'str'},
        'max_items_per_page': {'key': 'MaxItemsPerPage', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueryTwinsOptions, self).__init__(**kwargs)
        self.traceparent = kwargs.get('traceparent', None)
        self.tracestate = kwargs.get('tracestate', None)
        self.max_items_per_page = kwargs.get('max_items_per_page', None)


class RelationshipCollection(msrest.serialization.Model):
    """A collection of relationships which relate digital twins together.

    :param value: The relationship objects.
    :type value: list[object]
    :param next_link: A URI to retrieve the next page of objects.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[object]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RelationshipCollection, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)