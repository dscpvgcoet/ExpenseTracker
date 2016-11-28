"""
    api/va/accounts views
"""

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django_723e import settings
from django_723e.models.accounts.models import Account
from django_723e.models.accounts.serializers import AccountSerializer, UserSerializer
from django_723e.models.currency.models import Currency

@permission_classes((IsAuthenticated,))
class api_accounts(viewsets.ModelViewSet):
    """
        Distribute Account model object
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

@permission_classes((IsAuthenticated,))
class api_users(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self):
        user = self.get_object()
        if self.request.user.is_staff or self.request.user.id == user.id:
            serializer = self.get_serializer(user, many=False)
            return Response(serializer.data, status=200)
        else:
            return Response({'code': 401}, status=401)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self):
        user = self.get_object()
        if self.request.user.is_staff:
            user.delete()
            return Response({'code': 200}, status=200)
        elif self.request.user.id == user.id:
            self.request.user.delete()
            return Response({'code': 200}, status=200)
        else:
            return Response({'code': 401}, status=401)

@api_view(['POST', 'PUT'])
def subscription(request):
    """
    Create a user account
    """

    if request.method == 'POST':
        if not settings.ALLOW_ACCOUNT_CREATION:
            return Response({'code': 403}, status=403)

        args = request.data

        try:
            user = User.objects.get(username=args.get('username'))
            return Response(
                {'field': 'username', 'errorMsg': 'This user already exist'},
                status=400)
        except User.DoesNotExist:
            # Create User
            user = User.objects.create_user(
                args.get('username'),
                args.get('email'),
                args.get('password'))
            user.save()
            # Create Account
            currency = Currency.objects.get(id=args.get('currency'))
            Account.objects.create(user=user, name=args.get('name'), currency=currency)

            token = Token.objects.get_or_create(user=user)
            # Log user with Token
            return Response({'code': 200, 'token': token[0].key}, status=200)

    if request.method == 'PUT':

        user = request.user
        args = request.data

        if args.get('oldPassword'):
            if not authenticate(username=user.username, password=args.get('oldPassword')):
                return Response({'field': 'oldPassword', 'errorMsg': 'Wrong password'}, status=400)
            else:
                user.set_password(args.get('newPassword'))

        user.email = args.get('email')
        user.save()

        return Response({'code': 200}, status=200)
