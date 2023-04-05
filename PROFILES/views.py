from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import Profile
import uuid

class ProfileAPIView(viewsets.ViewSet):
    def login(self, request):
        if request.method == 'POST':
            member_id = request.data['member_id']
            password = request.data['password']
            try:
                profile = Profile.objects.get(member_id=member_id)
                if password == profile.password:
                    profile.sessionId = uuid.uuid4()
                    profile.save()
                    serializer = ProfileSerializer(profile, many=False)
                    return Response(serializer.data)
                else:
                    return Response({'errMsg': 'Wrong Credentials'}, status=status.HTTP_404_NOT_FOUND)
            except:
              return Response({'errMsg': 'User Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def is_admin(self, request):
        if request.method == 'POST':
            sessionId = request.data['session_id']
            try:
                profile = Profile.objects.get(sessionId=sessionId)
                if profile.is_admin:
                    return Response({'success':'True', 'is_admin':'True'})
                else:
                    return Response({'success':'True', 'is_admin':'False'}) 
            except:
                return Response({'success':'False'})
