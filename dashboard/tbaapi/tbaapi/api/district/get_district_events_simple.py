from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_simple import EventSimple
from ...models.get_district_events_simple_response_401 import GetDistrictEventsSimpleResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    district_key: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/district/{district_key}/events/simple".format(
            district_key=quote(str(district_key), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDistrictEventsSimpleResponse401 | list[EventSimple] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EventSimple.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetDistrictEventsSimpleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    district_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]]:
    """Gets a short-form list of events in the given district.

    Args:
        district_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]]
    """

    kwargs = _get_kwargs(
        district_key=district_key,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    district_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetDistrictEventsSimpleResponse401 | list[EventSimple] | None:
    """Gets a short-form list of events in the given district.

    Args:
        district_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]
    """

    return sync_detailed(
        district_key=district_key,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    district_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]]:
    """Gets a short-form list of events in the given district.

    Args:
        district_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]]
    """

    kwargs = _get_kwargs(
        district_key=district_key,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    district_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetDistrictEventsSimpleResponse401 | list[EventSimple] | None:
    """Gets a short-form list of events in the given district.

    Args:
        district_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDistrictEventsSimpleResponse401 | list[EventSimple]
    """

    return (
        await asyncio_detailed(
            district_key=district_key,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
