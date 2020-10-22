# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class QueryOperations:
    """QueryOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.digitaltwins.core.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def query_twins(
        self,
        query_specification: "models.QuerySpecification",
        query_twins_options: Optional["models.QueryTwinsOptions"] = None,
        **kwargs
    ) -> "models.QueryResult":
        """Executes a query that allows traversing relationships and filtering by property values.
        Status codes:


        * 200 OK
        * 400 Bad Request

          * BadRequest - The continuation token is invalid.
          * SqlQueryError - The query contains some errors.

        * 429 Too Many Requests

          * QuotaReachedError - The maximum query rate limit has been reached.

        :param query_specification: The query specification to execute.
        :type query_specification: ~azure.digitaltwins.core.models.QuerySpecification
        :param query_twins_options: Parameter group.
        :type query_twins_options: ~azure.digitaltwins.core.models.QueryTwinsOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryResult, or the result of cls(response)
        :rtype: ~azure.digitaltwins.core.models.QueryResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.QueryResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        
        _traceparent = None
        _tracestate = None
        _max_items_per_page = None
        if query_twins_options is not None:
            _traceparent = query_twins_options.traceparent
            _tracestate = query_twins_options.tracestate
            _max_items_per_page = query_twins_options.max_items_per_page
        api_version = "2020-10-31"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.query_twins.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", _traceparent, 'str')
        if _tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", _tracestate, 'str')
        if _max_items_per_page is not None:
            header_parameters['max-items-per-page'] = self._serialize.header("max_items_per_page", _max_items_per_page, 'int')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(query_specification, 'QuerySpecification')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['query-charge']=self._deserialize('float', response.headers.get('query-charge'))
        deserialized = self._deserialize('QueryResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    query_twins.metadata = {'url': '/query'}  # type: ignore