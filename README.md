# Minecraft Server Selector
A web front-end utility for selecting which Minecraft server to run.

# Getting Started

## Requirements
 1. Django 1.8
 2. Python 3.2.5
 3. Java
 4. ???
 
## Deploying the App

    pip install -r requirements.txt
    ./run_server.py


# Manual steps

## How To Deploy a FTB Server Manually

1. Download the server zip file from the FTB website. http://www.feed-the-beast.com/modpacks
2. Extract the Zip
3. Run the FTBInstall script
4. Edit the eula to be True
5. Add any extra mods to the mods folder
6. Run the ServerStart script

## How To Start the FTB Client

1. Download the FTBLauncher http://www.feed-the-beast.com/
2. Select the modpack (We usually play Infinity Evolved v2.0.2)
3. Edit modpacks, and add any extra mods (we use MagicalCrops)
4. Create a Profile with your Mojang credentials
5. Launch FTB

## Upgrade the Server

TODO

### Translation in Django

https://docs.djangoproject.com/en/1.8/topics/i18n/translation/

```python
from django.utils.translation import ugettext as _
from django.http import HttpResponse

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
```