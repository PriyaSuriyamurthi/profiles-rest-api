from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methoses as function(get,post,patch,put,delete)'
            'Is similar to a tradition Django View',
            'gives you the most control over application logic',
            'is mapped manually to URLS',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
