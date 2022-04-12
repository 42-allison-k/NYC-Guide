from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        #rendering the 'city.html' and sending context to be used
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        #rendering 'borough.html' and sending the context to be used
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    def get(self, request, borough, activity):
        #rendering 'activity.html' and sending the context to be used
        return render(
        request=request,
        template_name='activity.html',
        context={
            'borough': borough, 'activity': activity, 
            'venues':boroughs[borough][activity].keys()}
        )


class VenueView(View):
    
    def get(self, request, borough, activity, venue):
        #rendering 'venue.html' and sending the context to be displayed
        return render(
            request=request,
            template_name='venues.html',
            context={
                'borough':borough,
                'venue': venue,
                'description': boroughs[borough][activity][venue]['description']
            }
        )
