import json

def parse_request(request):
	path = request.path
	method = request.META.get('REQUEST_METHOD')
	user_agent = request.META.get('HTTP_USER_AGENT')
	referer = request.META.get('HTTP_REFERER')
	host = request.META.get('HTTP_HOST')
	client_ip = request.META.get('REMOTE_ADDR')
	return json.dumps({'url': path, 'method': method, 
					   'user_agent': user_agent, 'referer': referer,
					   'host': host, 'client_ip': client_ip})