from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters

import json

from . import models, serializers


class CustomSearchFilter(filters.SearchFilter):
    def get_search_terms(self, request):
        params = request.query_params.get(self.search_param, '')
        params = params.replace('\x00', '')  # strip null characters
        params = params.replace(',', ' ')
        #params = params.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
        db_backend = settings.DATABASES['default']['ENGINE'].split('.')[-1]
        if db_backend == 'sqlite3':
            return [json.dumps(param).replace('"', '') for param in params.split()]
        return params.split()

class CustomPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'

class ContactList(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    queryset = models.Contact.objects.order_by("-created_at")
    serializer_class = serializers.ContactSerializer 
    filter_backends = [CustomSearchFilter]
    search_fields = ('json',)
    pagination_class = CustomPagination

mail_body = """

※このメールはシステムからの自動返信です

{email}様

お世話になっております。
{site_name}へのお問い合わせありがとうございました。

以下の内容でお問い合わせを受け付けいたしました。管理人が確認いたします

━━━━━━□■□　お問い合わせ内容　□■□━━━━━━

E-Mail：{email}

お問い合わせ内容：{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

———————————————————————
{site_name}
https://{site_domain}/

———————————————————————"""

class ContactCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = models.Contact.objects.none()
    serializer_class = serializers.ContactSerializer 

    def create(self, request, *args, **kwargs):
        current_site = get_current_site(request)
        site_name = current_site.name
        site_domain = current_site.domain

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json = serializer.data['json']
        email = json['email']
        message = json['message']

        email_message = EmailMessage(
            f"【{site_name}】お問い合わせありがとうございます",
            mail_body.format(email=email, message=message, site_name=site_name, site_domain=site_domain),
            f'noreply@{site_domain}',
            [email,],
            [f'contact@{site_domain}',],
            #reply_to=['another@example.com'],
            #headers={'Message-ID': 'foo'},
        )
        email_message.send(fail_silently=False)
        return super().create(request, *args, **kwargs)

def contact_view(request):
    current_site = get_current_site(request)
    site_name = current_site.name
    context = {'is_debug': settings.DEBUG, "site_name": site_name}
    return render(request, 'contact/contact.html', context)
