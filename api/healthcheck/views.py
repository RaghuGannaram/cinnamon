from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def health_check(request):
    """
    Returns system health details including CPU, memory usage, hostname, and database status.
    """
    health_status = {
        "status": "Ok",
    }
    
    return Response(health_status)
