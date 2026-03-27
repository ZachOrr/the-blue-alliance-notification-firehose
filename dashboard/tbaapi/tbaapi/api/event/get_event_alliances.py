from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elimination_alliance import EliminationAlliance
from ...models.get_event_alliances_response_401 import GetEventAlliancesResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_key: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/event/{event_key}/alliances".format(
            event_key=quote(str(event_key), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> list[EliminationAlliance] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_1 = []
                _response_200_type_1 = data
                for response_200_type_1_item_data in _response_200_type_1:
                    response_200_type_1_item = EliminationAlliance.from_dict(response_200_type_1_item_data)

                    response_200_type_1.append(response_200_type_1_item)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EliminationAlliance] | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetEventAlliancesResponse401.from_dict(response.json())

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
) -> Response[Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None]:
    """Gets a list of Elimination Alliances for the given Event.

    Args:
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None]
    """

    kwargs = _get_kwargs(
        event_key=event_key,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None | None:
    """Gets a list of Elimination Alliances for the given Event.

    Args:
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None
    """

    return sync_detailed(
        event_key=event_key,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None]:
    """Gets a list of Elimination Alliances for the given Event.

    Args:
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None]
    """

    kwargs = _get_kwargs(
        event_key=event_key,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None | None:
    """Gets a list of Elimination Alliances for the given Event.

    Args:
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEventAlliancesResponse401 | list[EliminationAlliance] | None
    """

    return (
        await asyncio_detailed(
            event_key=event_key,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
