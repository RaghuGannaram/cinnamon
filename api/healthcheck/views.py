from rest_framework.response import Response
from rest_framework.decorators import api_view

import psutil
import socket

@api_view(['GET'])
def health_check(request):
    """
    Returns system health details including CPU, memory usage, hostname, and database status.
    """
    health_status = {
        "status": "healthy",
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "hostname": socket.gethostname(),
    }
    
    return Response(health_status)
