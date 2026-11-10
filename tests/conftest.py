"""Asynchronous Python client for TRMNL."""

from collections.abc import AsyncGenerator

import aiohttp
from aiointercept import aiointercept
import pytest

from syrupy import SnapshotAssertion
from trmnl import TRMNLClient

from .syrupy import TRMNLSnapshotExtension


@pytest.fixture(name="snapshot")
def snapshot_assertion(snapshot: SnapshotAssertion) -> SnapshotAssertion:
    """Return snapshot assertion fixture with the TRMNL extension."""
    return snapshot.use_extension(TRMNLSnapshotExtension)


@pytest.fixture
async def client() -> AsyncGenerator[TRMNLClient]:
    """Return a TRMNL client."""
    async with (
        aiohttp.ClientSession() as session,
        TRMNLClient("token", session=session) as trmnl_client,
    ):
        yield trmnl_client


@pytest.fixture(name="responses")
async def aiointercept_fixture() -> AsyncGenerator[aiointercept]:
    """Return aiointercept fixture."""
    async with aiointercept(mock_external_urls=True) as mocked_responses:
        yield mocked_responses
