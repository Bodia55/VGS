from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import Profile
import uuid

class ProfileAPIView(viewsets.ViewSet):
    def login(self, request):
        if request.method == 'POST':
            guc_id = request.data['guc_id']
            password = request.data['password']
            try:
                profile = Profile.objects.get(guc_id=guc_id)
                if password == profile.password:
                    profile.sessionId = uuid.uuid4()
                    profile.save()
                    serializer = ProfileSerializer(profile, many=False)
                    return Response(serializer.data)
                else:
                    return Response({'errMsg': 'Wrong Credentials'}, status=status.HTTP_404_NOT_FOUND)
            except:
              return Response({'errMsg': 'User Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
