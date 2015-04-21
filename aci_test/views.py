from pyramid.view import view_config

def my_view(request):
    return {'project':'aci_test'}

@view_config(route_name='login', render='template/login.pt')
def login(request):
	return {}
