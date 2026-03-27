from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_match_zebra_response_401 import GetMatchZebraResponse401
from ...models.zebra import Zebra
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
        "url": "/match/{match_key}/zebra_motionworks".format(
            match_key=quote(str(match_key), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMatchZebraResponse401 | Zebra | None:
    if response.status_code == 200:
        response_200 = Zebra.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetMatchZebraResponse401.from_dict(response.json())

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
) -> Response[Any | GetMatchZebraResponse401 | Zebra]:
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
) -> Response[Any | GetMatchZebraResponse401 | Zebra]:
    """Gets Zebra MotionWorks data for a Match for the given match key.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMatchZebraResponse401 | Zebra]
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
) -> Any | GetMatchZebraResponse401 | Zebra | None:
    """Gets Zebra MotionWorks data for a Match for the given match key.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMatchZebraResponse401 | Zebra
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
) -> Response[Any | GetMatchZebraResponse401 | Zebra]:
    """Gets Zebra MotionWorks data for a Match for the given match key.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMatchZebraResponse401 | Zebra]
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
) -> Any | GetMatchZebraResponse401 | Zebra | None:
    """Gets Zebra MotionWorks data for a Match for the given match key.

    Args:
        match_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMatchZebraResponse401 | Zebra
    """

    return (
        await asyncio_detailed(
            match_key=match_key,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
