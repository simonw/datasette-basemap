from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_database():
    datasette = Datasette([], memory=True)
    await datasette.invoke_startup()
    response = await datasette.client.get("/basemap.json")
    assert 200 == response.status_code
    data = response.json()
    assert data["database"] == "basemap"
    tiles = [t for t in response.json()["tables"] if t["name"] == "tiles"][0]
    assert {
        "name": "tiles",
        "columns": ["zoom_level", "tile_column", "tile_row", "tile_data"],
    }.items() <= tiles.items()
