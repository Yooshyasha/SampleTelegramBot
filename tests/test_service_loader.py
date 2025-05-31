"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

import asyncio

import pytest

from avitoworkerservice.src.core.service_loader import ServiceLoader


@pytest.fixture
def service_loader():
    return ServiceLoader()

def test_load_services(service_loader):
    service_loader.load()
    assert len(service_loader._services) > 0

def test_initialize_services(service_loader):
    async def destroy_services():
        service_loader.load()
        service_loader.initialize()
        assert service_loader._is_initialized is True

    asyncio.run(destroy_services())

def test_destroy_services(service_loader):
    async def destroy_services():
        service_loader.load()
        service_loader.initialize()
        service_loader.destroy()
        assert service_loader._is_initialized is False

    asyncio.run(destroy_services())
