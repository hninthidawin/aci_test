from pyramid.view import view_config

@view_config(route_name='home', renderer='aci_test:templates/home.pt')
def home(request):
	return {}

@view_config(route_name='angular_login', renderer='aci_test:client_src/views/login_form.html')
def login(request):
	return {}