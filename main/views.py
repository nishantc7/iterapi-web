from rest_framework import generics
from rest_framework.response import Response
from iterapi import Student
from rest_framework.parsers import JSONParser
from main.serializer import UserSerializer


class MainView(generics.CreateAPIView):

    parser_classes = [JSONParser]
    serializer_class = UserSerializer

    def post(self, request):
        user_id = request.data['user_id']
        password = request.data['password']
        st = Student(user_id, password)
        return Response(st.getAttendance())


class ResultView(generics.CreateAPIView):
    parser_classes = [JSONParser]
    serializer_class = UserSerializer

    def post(self, request):
        user_id = request.data['user_id']
        password = request.data['password']
        sem = request.data['sem']
        st = Student(user_id, password)
        return Response(st.getDetailedResult(sem))


class InfoView(generics.CreateAPIView):
    parser_classes = [JSONParser]
    serializer_class = UserSerializer

    def post(self, request):
        user_id = request.data['user_id']
        password = request.data['password']
        st = Student(user_id, password)
        return Response(st.getInfo())

class CgpaView(generics.CreateAPIView):
    parser_classes = [JSONParser]
    serializer_class = UserSerializer

    def post(self, request):
        user_id = request.data['user_id']
        password = request.data['password']
        st = Student(user_id, password)
        return Response(st.getResult())
