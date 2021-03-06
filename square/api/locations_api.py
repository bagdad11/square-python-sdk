# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class LocationsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(LocationsApi, self).__init__(config, call_back)

    def list_locations(self):
        """Does a GET request to /v2/locations.

        Provides information of all locations of a business.
        Most other Connect API endpoints have a required `location_id` path
        parameter.
        The `id` field of the [`Location`](#type-location) objects returned by
        this
        endpoint correspond to that `location_id` parameter.

        Returns:
            ListLocationsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_location(self,
                        body):
        """Does a POST request to /v2/locations.

        Creates a location.
        For more information about locations, see [Locations API
        Overview](https://developer.squareup.com/docs/locations-api).

        Args:
            body (CreateLocationRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            CreateLocationResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_location(self,
                          location_id):
        """Does a GET request to /v2/locations/{location_id}.

        Retrieves details of a location. You can specify "main" 
        as the location ID to retrieve details of the 
        main location. For more information, 
        see [Locations API
        Overview](https://developer.squareup.com/docs/docs/locations-api).

        Args:
            location_id (string): The ID of the location to retrieve. If you
                specify the string "main", then the endpoint returns the main
                location.

        Returns:
            RetrieveLocationResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations/{location_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_location(self,
                        location_id,
                        body):
        """Does a PUT request to /v2/locations/{location_id}.

        Updates a location.

        Args:
            location_id (string): The ID of the location to update.
            body (UpdateLocationRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            UpdateLocationResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/locations/{location_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
