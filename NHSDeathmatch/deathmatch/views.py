from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from deathmatch.utils import processor



class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

def view_home(request):
    if request.method == 'POST':
        if(request.POST.get("fname")):
            processor.accept_person(request.POST.get("fname", False))
        if (request.POST.get("theme")):
            processor.setTheme(request.POST.get("theme", False))
            print(processor.getTheme())
        if(request.POST.get("yes")):
            processor.accept_person(request.POST.get("yes", False))
        if(request.POST.get("no")):
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
        if request.method == 'POST':
            # print(len(processor.getSortedDict()[-1.0]))
            if(request.POST.get("p1")):
                # print("p1")
                processor.addWinner(request.POST.get("p1", False))
                processor.increaseCount(request.POST.get("p1", False), 1.0)
            if (request.POST.get("p2")):
                # print("p2")
                processor.addWinner(request.POST.get("p2", False))
                processor.increaseCount(request.POST.get("p2", False), 1.0)
            if (request.POST.get("reset")):
                processor.reset()
            if (processor.isRoundOver()):
                processor.startNewRound()
                print("new round!")
            if processor.isGameOver():
                print("Game Over!")
                results = processor.getSortedDict()
                sl = results[8.0]
                al = results[7.0] + results[6.0]
                bl = results[5.0]
                cl = results[4.0] + results[3.0]
                dl = results[2.0] + results[1.0]
                fl = results[0.0]
                try:
                    nal = results[-1.0]
                except KeyError:
                    nal = ""
                s = " ".join(sl)
                a = ", ".join(al)
                b = ", ".join(bl)
                c = ", ".join(cl)
                d = ", ".join(dl)
                f = ", ".join(fl)
                na = ", ".join(nal)

                return render(request, 'results.html', {'s':s, 'a':a,
                                                        'b':b, 'c':c,
                                                        'd':d, 'f':f,
                                                        'na':na})
            else:
                processor.setUpDeathmatch()
                players = processor.getNextPair()
                player1, player2 = players[0], players[1]
        return render(request, 'deathmatch.html', {"player1":player1, "player2":player2, "rounds":processor.getRounds(),
                                                   "progress":processor.getProgress(), "theme":processor.getTheme()})
    return render(request,'index.html',{"result":currPerson, "number":number, "number2":256-processor.getNumberAccepted(),
                                        "theme":processor.getTheme()})

# def get_first_result(request):
#     if request.method == 'POST':
#         if(request.POST.get(""))