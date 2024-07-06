from rest_framework import generics

from api.models.member import Member
from api.serilizers.member import MemberSerializer


class MemberView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class MemberlistView(generics.ListAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

