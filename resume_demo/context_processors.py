 #3. context_processors take a request object as their argument and return a dictionary of items to be merged into the context.
    #This will come in handy when you need to make something available globally to all templates.
 
from django.contrib.auth.models import User

def project_context(request):

	context = {
		'me': User.objects.first(),
		
	}

	return context