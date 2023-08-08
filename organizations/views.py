from django.shortcuts import render

orgs = [
    {
        "name": "Django Software Foundation",
        "description": "The Web Framework",
        "image": "images/demo/orgsdemodj.png"
    },
    {
        "name": "Open Street map",
        "description": "The Maps for OpenSource Stuff",
        "image": "images/demo/orgsdemoosm.png"
    }
]

isAuthenticated = True

# Create your views here.
def home(request):
    context = {
        'isAuthenticated': isAuthenticated
    }
    return render(request, "index.html", context=context)

def organizations(request):
    context = {
        'orgs': orgs
    }

    return render(request, "organizations/organizations.html", context=context)