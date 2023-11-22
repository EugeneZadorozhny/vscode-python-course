"""
Configures and exports an instance of APIRouter for the /shows path
"""
from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.routing import APIRouter

from podcastapi.data import podcast_table

shows_router = APIRouter(prefix="/shows", tags=["shows"])


@shows_router.get("{show_id}")
def get_show_by_id(show_id: int) -> Response:
    '''Returns show that matches the given show_id'''

    show = podcast_table.get(doc_id=show_id)
    if show:
        return JSONResponse(show)
    return Response(status_code=status.HTTP_404_NOT_FOUND)

@shows_router.get("{show_id}/categories")
def get_show_categories(show_id: int) -> Response:
    '''Returns categories for a given show_id'''

    show = podcast_table.get(doc_id=show_id)
    if show and "categories" in show:
        return JSONResponse(show["categories"])
    return Response(status_code=status.HTTP_404_NOT_FOUND)

@shows_router.get("{show_id}/episodes")
def get_show_episodes(show_id: int) -> Response:
    '''Returns the associated episodes for a given show'''

    show = podcast_table.get(doc_id=show_id)
    if show and "episodes" in show:
        return JSONResponse(show["episodes"])
    return Response(status_code=status.HTTP_404_NOT_FOUND)
