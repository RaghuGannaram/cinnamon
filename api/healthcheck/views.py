"""
This module contains the health check view.
"""

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def health_check(_request):
    """Returns Ok if the server is running."""

    health_status = {
        "status": "Ok",
    }

    return Response(health_status)
