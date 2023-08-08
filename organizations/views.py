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

# Create your views here.
def home(request):
    return render(request, "organizations/index.html")

def organizations(request):
    context = {
        'orgs': orgs
    }

    return render(request, "organizations/organizations.html", context=context)