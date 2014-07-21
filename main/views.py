from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
import requests
from instagram.client import InstagramAPI





class IndexView(TemplateView):
	template_name = "index.html"

pass


def generate(request):
	code = request.GET['code']

	data = {'client_id': '50831fa41c5a4d3cba82f9bd14bb4a86', 'client_secret' : 'fd9652076534434eb4550015b119a417','grant_type':'authorization_code','code':code, 'redirect_uri':'http://localhost:8000/gen'}
	r = requests.post('https://api.instagram.com/oauth/access_token', data=data)
	access_token = r.json()['access_token']
	user_id = r.json()['user']['id']
	


	

	api = InstagramAPI(access_token=access_token)

	f = api.user_followed_by(user_id)
	for i in f:
		print i
	

	return HttpResponseRedirect('/test')


