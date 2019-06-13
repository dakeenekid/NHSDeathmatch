from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from deathmatch.utils import processor


sessions = {}

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

def view_home(request):
    processor.initSession(request, False)
    if request.method == 'POST':
        # print(request.session.items())
        if(request.POST.get("fname")):
            processor.accept_person(request, request.POST.get("fname", False))
        if (request.POST.get("theme")):
            processor.setTheme(request, request.POST.get("theme", False))
            #print(processor.getTheme(request))
        if(request.POST.get("yes")):
            processor.accept_person(request, request.POST.get("yes", False))
        if(request.POST.get("no")):
            processor.delete_person(request, request.POST.get("no", False))
        if (request.POST.get("reset")):
            processor.reset(request)
        if (request.POST.get("random")):
            processor.generateRandomBracket(request)

    if processor.getNumberLeft(request) != 0:
        currPerson = processor.get_person(request)
    else:
        currPerson = "null"
    if (processor.getNumberLeft(request) == 0 or processor.getNumberAccepted(request) == 256):
        request.session['isDeathmatch'] = True
        #print(request.session['isDeathmatch'])
        if request.method == 'POST':
            #print("post")
            #print(request.POST)
            # print(len(processor.getSortedDict()[-1.0]))
            if(request.POST.get("p1")):
                # print("p1")
                processor.addWinner(request, request.POST.get("p1", False))
                processor.increaseCount(request, request.POST.get("p1", False), 1.0)
            if (request.POST.get("p2")):
                # print("p2")
                processor.addWinner(request, request.POST.get("p2", False))
                processor.increaseCount(request, request.POST.get("p2", False), 1.0)
            if (request.POST.get("reset")):
                processor.reset(request)
            if (processor.isRoundOver(request)):
                processor.startNewRound(request)
            if processor.isGameOver(request):
                #print("Game Over!")
                results = processor.getSortedDict(request)
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

                #processor.printEverything(request)
                return render(request, 'results.html', {'s':s, 'a':a,
                                                        'b':b, 'c':c,
                                                        'd':d, 'f':f,
                                                        'na':na, 'theme':processor.getTheme(request)})
            else:
                processor.setUpDeathmatch(request)
                acc = request.session['accepted']
                win = request.session['winners']
                players = processor.getNextPair(request)
                player1, player2 = players[0], players[1]
                if len(set(win)) == len(win):
                    del acc[:2]
                else:
                    win = list(set(win))
                request.session['accepted'] = acc
                request.session['winners'] = win
        #processor.printEverything(request)
            return render(request, 'deathmatch.html', {"player1":player1, "player2":player2, "rounds":processor.getRounds(request),
                                                   "progress":processor.getProgress(request), "theme":processor.getTheme(request)})
    #processor.printEverything(request)
    return render(request,'index.html',{"result":currPerson, "number":processor.getNumberLeft(request), "number2":256-processor.getNumberAccepted(request),
                                        "theme":processor.getTheme(request)})

# def get_first_result(request):
#     if request.method == 'POST':
#         if(request.POST.ge                del acc[:2]t(""))