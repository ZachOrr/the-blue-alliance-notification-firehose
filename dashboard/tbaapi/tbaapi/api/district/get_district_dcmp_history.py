from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_district_dcmp_history_response_200_item import GetDistrictDCMPHistoryResponse200Item
from ...models.get_district_dcmp_history_response_401 import GetDistrictDCMPHistoryResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    district_abbreviation: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/district/{district_abbreviation}/dcmp_history".format(
            district_abbreviation=quote(str(district_abbreviation), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetDistrictDCMPHistoryResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetDistrictDCMPHistoryResponse401.from_dict(response.json())

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
) -> Response[Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    district_abbreviation: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]]:
    """Gets a list of DCMP events and awards for the given district abbreviation.

    Args:
        district_abbreviation (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]]
    """

    kwargs = _get_kwargs(
        district_abbreviation=district_abbreviation,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    district_abbreviation: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item] | None:
    """Gets a list of DCMP events and awards for the given district abbreviation.

    Args:
        district_abbreviation (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]
    """

    return sync_detailed(
        district_abbreviation=district_abbreviation,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    district_abbreviation: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]]:
    """Gets a list of DCMP events and awards for the given district abbreviation.

    Args:
        district_abbreviation (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]]
    """

    kwargs = _get_kwargs(
        district_abbreviation=district_abbreviation,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    district_abbreviation: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item] | None:
    """Gets a list of DCMP events and awards for the given district abbreviation.

    Args:
        district_abbreviation (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDistrictDCMPHistoryResponse401 | list[GetDistrictDCMPHistoryResponse200Item]
    """

    return (
        await asyncio_detailed(
            district_abbreviation=district_abbreviation,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
