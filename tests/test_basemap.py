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


@pytest.mark.asyncio
async def test_metadata():
    datasette = Datasette([], memory=True)
    await datasette.invoke_startup()
    response = await datasette.client.get("/basemap/metadata.json?_shape=array")
    metadata = {r["name"]: r["value"] for r in response.json()}
    assert metadata == {
        "name": "datasette-basemap 0.2",
        "format": "png",
        "minzoom": "0",
        "maxzoom": "6",
        "bounds": "-180.0,-90.0,180.0,90.0",
        "center": "0.0,0.0,3",
        "template": "{{#__location__}}{{/__location__}} {{#__teaser__}}          {{/__teaser__}}{{#__full__}}{{/__full__}}",
        "attribution": "© OpenStreetMap contributors",
    }
