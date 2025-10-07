from django.shortcuts import render
from django.http import HttpResponse

# Function to render the simple landing page
def landing_page(request):
    """
    Renders the dummy landing page template.
    """
    # django.shortcuts.render looks for templates in the 'templates/<app_name>/' folder
    return render(request, 'data_manager/landing.html')