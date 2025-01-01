from django.shortcuts import render
from django.utils.encoding import smart_str
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .serializers import UserSerilaizer, TranieeProfileSerilizer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import TraineeProfile
from rest_framework_simplejwt.authentication import JWTAuthentication
from weasyprint import HTML, CSS

# NOTE : Admin password: atkadmin

# list all trainees 
class ListTrainees(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.prefetch_related("trainee_profile")
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

class UpdateDeleteTrainee(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.prefetch_related("trainee_profile")
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

# list a single trainee
class ListTrainee(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

class ProfileTrainee(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TranieeProfileSerilizer
    permission_classes = [IsAuthenticated]
    queryset = TraineeProfile.objects.all()

class UpdateDeleteProfileTrainee(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = TranieeProfileSerilizer
    permission_classes = [IsAuthenticated]
    queryset = TraineeProfile




class GenerateReport(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def sanitize_data(self, data):
        for item in data:
            for key, value in item.__dict__.items():
                if isinstance(value, str):
                    item.__dict__[key] = value.encode('utf-8', errors='ignore').decode('utf-8')
        return data

    def get(self, request, format=None):
        trainee_data = self.sanitize_data(User.objects.exclude(email="atk_admin@gmail.com"))
        # render data to string 
        html_string = render_to_string("trainee_report.html", {"trainees": trainee_data})
        html_string = smart_str(html_string, encoding='utf-8')
        
        css = CSS(string="""
            @page {
                size: A4 landscape;
                margin: 1cm;
            }
                  body {
                font-size: 10px;
                word-wrap: break-word;
            }

            table {
                width: 100%;
                table-layout: fixed;
            }

            td, th {
                word-wrap: break-word;
                overflow: hidden;
                padding: 2px;
            }

            div.page-break {
                page-break-after: always;
            }
        """)

        # Convert the HTML to a PDF
        html = HTML(string=html_string)
        pdf = html.write_pdf(stylesheets=[css])
        # turn the PDF into a Response
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report.pdf"'
        return response