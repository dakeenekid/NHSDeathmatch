from django.shortcuts import render
from django.views.generic import TemplateView

from deathmatch.utils import processor



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

def view_home(request):
    if request.method == 'POST':
        if(request.POST.get("yes")):
            print(request.POST)
            processor.accept_person(request.POST.get("yes", False))
        if(request.POST.get("no")):
            print(request.POST)
            processor.delete_person(request.POST.get("no", False))
        if (request.POST.get("reset")):
            processor.reset()
        if (request.POST.get("random")):
            processor.generateRandomBracket()
    i = 0
    if processor.getNumberLeft() != 0:
        currPerson = processor.get_person()
    else:
        currPerson = "null"
    number = processor.getNumberLeft()
    if (processor.getNumberLeft() == 0 or processor.getNumberAccepted() == 256):
        # if there's only one person left
        if request.method == 'POST':
            if(request.POST.get("p1")):
                print("p1")
                processor.addWinner(request.POST.get("p1", False))
                processor.increaseCount(request.POST.get("p1", False))
                print(processor.getCount(request.POST.get("p1", False)))
            if (request.POST.get("p2")):
                print("p2")
                processor.addWinner(request.POST.get("p2", False))
                processor.increaseCount(request.POST.get("p2", False))
                print(processor.getCount(request.POST.get("p2", False)))
            if (request.POST.get("reset")):
                processor.reset()
            if (processor.isRoundOver()):
                processor.startNewRound()
                print("new round!")
            if processor.isGameOver():
                print("Game Over!")
                return render(request, 'results.html', {})
            else:
                processor.setUpDeathmatch()
                players = processor.getNextPair()
                player1, player2 = players[0], players[1]
        return render(request, 'deathmatch.html', {"player1":player1, "player2":player2, "rounds":processor.getRounds()})
    return render(request,'index.html',{"result":currPerson, "number":number, "number2":256-processor.getNumberAccepted()})

# def get_first_result(request):
#     if request.method == 'POST':
#         if(request.POST.get(""))