__author__ = 'cgiridhar'
from django.contrib.auth.models import User
from models import UserProfile
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import Authentication, ApiKeyAuthentication, MultiAuthentication
#from authorization import UserObjectsOnlyAuthorization, EnterpriseObjectsAuthorization
from tastypie.models import create_api_key
from django.db import models
models.signals.post_save.connect(create_api_key, sender=User)
import copy

from tastypie.http import HttpResponse
from tastypie.cache import SimpleCache
from tastypie import fields
from tastypie.exceptions import BadRequest
import json
#from utils import Utils


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        include_resource_uri = False
        always_return_data = True
        allowed_methods = ['get', 'post', 'put']
        #authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def dehydrate(self, bundle):
        # Utils().show_fields(bundle, 'email', 'username', 'first_name', 'last_name',
        #                     'last_login', 'date_joined')
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['users'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            email = bundle.data['email']
            username = bundle.data['username']
            if email is None:
                raise BadRequest("user can't be blank!")
            if email and User.objects.filter(email=email).count() > 0:
                raise BadRequest("email should be unique!")
            if username and User.objects.filter(username=username).count() > 0:
                raise BadRequest("username should be unique!")

        except KeyError as missing_key:
            raise BadRequest("Must provide {missing_key} when creating an enterprise.".format(missing_key=missing_key))
        return super(UserResource, self).obj_create(bundle, **kwargs)


class UserProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'
        always_return_data = True
        include_resource_uri = False
        allowed_methods = ['post', 'get', 'put']
        authorization = Authorization()
        #authentication = ApiKeyAuthentication()
        #cache = SimpleCache(cache_name='resources',timeout=3600, public=True)

    def dehydrate(self, bundle, **kwargs):
        """ Works on GET Requests """
        return bundle



    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['profile'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict


    def obj_create(self, bundle, request=None, **kwargs):
        try:
            user = bundle.data['user']
            username = bundle.data['user']['username']
        except KeyError as missing_key:
            raise BadRequest("Must provide {missing_key} when creating a user profile".format(missing_key=missing_key))

        return super(UserProfileResource, self).obj_create(bundle, **kwargs)

    def determine_format(self, request):
        return 'application/json'