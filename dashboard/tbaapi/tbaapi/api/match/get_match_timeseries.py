from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_match_timeseries_response_200_item import GetMatchTimeseriesResponse200Item
from ...models.get_match_timeseries_response_401 import GetMatchTimeseriesResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    match_key: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/match/{match_key}/timeseries".format(
            match_key=quote(str(match_key), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetMatchTimeseriesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetMatchTimeseriesResponse401.from_dict(response.json())

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
) -> Response[Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    match_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]]:
    """Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if
    not available.
    *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or
    missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
    *WARNING:* This endpoint and corresponding data models are under *active development* and may change
    at any time, including in breaking ways.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]]
    """

    kwargs = _get_kwargs(
        match_key=match_key,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    match_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item] | None:
    """Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if
    not available.
    *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or
    missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
    *WARNING:* This endpoint and corresponding data models are under *active development* and may change
    at any time, including in breaking ways.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]
    """

    return sync_detailed(
        match_key=match_key,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    match_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]]:
    """Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if
    not available.
    *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or
    missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
    *WARNING:* This endpoint and corresponding data models are under *active development* and may change
    at any time, including in breaking ways.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]]
    """

    kwargs = _get_kwargs(
        match_key=match_key,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    match_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item] | None:
    """Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if
    not available.
    *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or
    missing data. Do not rely on this data for any purpose. In fact, pretend we made it up.
    *WARNING:* This endpoint and corresponding data models are under *active development* and may change
    at any time, including in breaking ways.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMatchTimeseriesResponse401 | list[GetMatchTimeseriesResponse200Item]
    """

    return (
        await asyncio_detailed(
            match_key=match_key,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
