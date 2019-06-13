import random
import numpy as np
import operator
import difflib
names = ["David Abdurakhmanov","Marisa Abeles","Benjamin Aliber","Joseph Anastasi","Sofia Antonelli","Isabella Arbelaez","Andrew Arrondo","Hugh Atkinson","William Baker","Zoe Baker","Spencer Balder","Peter Bannon","Maeve Barker","Talia Barrett","Serena Bartlett","Joshua Batra","Jacob Bello","Griffin Berger","Andrew Berlinsky","Ketsia Bernard","Michael Bernard","Daniela Berner","Alexander Berney","Jaiman Bharadwa","Morgan Bilodeau","Andrew Blackburn","Olivia Blackmer","Alice Blake","Daniel Blumenstein","Sean Bogan","Reed Boisvert","Jonathan Bolivar","Melanie Bonilla","Daniel Borowsky","Alexandria Boutin","Maria Brasoveanu","Sydney Braunstein","Olivia Breen","Allison Brightman","Cate Brodowski","Victoria Bruce","Luke Bryson","David Busa","Pedro Caceres","You Cai","Timothy Callahan","Stephen Carr","Micah Carr-Gloth","Savannah Carucci","Holly Chadwick","Claire Chambers","Hamilton Champagne","Gabriella Chansky","Margaret Charter","Jason Child","Thomas Chmielewski","Brianna Chu","Marc Cifiello","Lauryne Civil","Kathryn Clancy","Daniel Cohen","Joshua Cohen","Shoshana Cohen","Thomas Cohen","Cameron Collyer","Mason Colwell","Maria L. Colon Figueroa","John Corbett","Henry Corderman","Tristan Coren","Nell Cosman","Julia Cuddy","Spencer Curran","Josie Dardinski","Julia Dasey","Abigail Dateo","Sebastian Davis","Stephen Demaio","Alexa DeMaria","Brittany DeMaria","Daniel DeMayo","Kelsey Desing","Benjamin Desmarais","Miriam DeSouza","Luis Diaz","Alexandra Diener","Nicolas Dimase","Isabel Dirks","Sarah Dodds","Jacob Doherty","Taylor Drew","Jacques Duport","Charles Eisenstadt","Alexander Ektov","Elise Erickson","Julia Evans","Sydney Fallon","Cole Fayemi","Dana Fernandez","Ava Feuer","Samuel Feuer","Sophie Findlay-Walters","Remi Fink","Logan Finn","Madison FitzGerald","Paul Flanagan","Sara Flano","Ryan Fleck","Joseph Fleming","Cameron Flynn","William Foley","Caroline Forbes","Karina Franco","Katya Franco","Taylor Frazzette","Madeline Frederick","Jason Freedman","Anna Friedman","Ella Friedman","Maxine Friedman","Mackenzie Fuller","Rose Gallagher","Saige Galovski","Hannah Garand","Anna Garf","Elise Gaudette","Anton Geyyer","Samantha Gilarde","Kyle Gilman","Benjamin Glanz","Nancy Glennon","Stephanie Godes","Spenser Goff","Ian Goldberg","Jacob Goldberg","Maya Golden","Ryan Goodale","Jenny Gould","Sachi Goyal","Kevin Grady","Jacob Grebber","Benjamin Greenes","Devin Griffin","Megan Griffin","Erica Guan","Rok Gundaker","Katherine Guttilla","Adrineh Guzelian","Timothy Hagerott","Lucy Hale","Natalie Hallagan","Payton Hartung","Jack Hayes","Connor Healey","Abigail Healy","Julia Hebert","Callista Hem","Sadye Herman","Abigail Hershenson","Kaylee Himmel","Garrett Hirsch","Sari Hirsh","Madeline Hluska","Kristin Ho","Julie Hoffmeister","Jeffrey Hohler","Sarah Hood","William Hood","Rachel Horrigan","Cohen Hu","XuanQiao Huang","Casey Hurwitch","Jayme Hurwitz","Alexandria Hwang","Jack Idelson","Marianna Jantzen","Thomas Jordan","Trent Kamke","Ethan Kams","Sonal Kango","Shih-Ting Kao","Daniel Kaplan","Samantha Karten","Dimitris Kartsagoulis","Nolan Katcher","Alyssa Katz","Mya Kearney","Benjamin Keegan","Henry Keegan","Samuel Keenan","Ana Keene","Davis Keene","Quinn Kelly","Henry Kennedy","Haley Kent","Ryan Kerrigan","Catherine Keshishyan","Samantha Keyes","Theresa Kim","Zoe Kim","Scott Kirschner","Parker Kirstein","Justin Kline","Symantha Komola","Anastasia Kopellas","Joshua Kornbleuth","Shilpa Krishnan","Jonathan Krushell","Jonah Kurker","Jacob Lagoon","Ivanna Lai","Justin Lam","Leo Leary","Ethan Lee","Samantha Lee","Jacob Lees","Steven Leicht","Celine Lemaire","Sebastian LeMay","Nicholas Lesanto","Julia Leshchiner","Michaela Leslie","Jack Levine","David Levy","Grace Li","Iris Li","Bergan Licht","Angel Lin","Kurt Lindenthal","Harrison Little","Seth Lockwood","Luke Lombardo","Henry London","Isabel Ludlow","Francesca Luppino","Craig Lustig","Kevin MacKenzie","Allison Mahoney","Megan Mahoney","Nicholas Mahoney","Caroline Malkin","Nicole Malouf","Nealaksi Maniraja","Eileen Manning","Caleb Marcus","David Marget","Beth Markman","Harrison Maron","David Martin","Ryan Martin","Max Masterson","Basil Matorin","Matthew Matossian","Philip Mazo","Rachel McCarthy","Grace McDonald","Lauren McGrath","Sebastian McKay","Bryce McKenzie","Cameron McLeod","Mikayla McNeill","Elizabeth Mesnik","Lily Mesnik","Leah Miller","Jordan Milstein","Mackenzie Mitchell","Stephanie Mittaz","Micaela Mittleman","Audrey Mock","Madeline Mollerus","Jake Monheimer","Shane Morley","Benjamin Moy","Calvin Mueller","Jason Mulno","John Murmes-Jarosz","Nicholas Murray","Natalie Mutter","Isabelle Nagle","Christopher Najarian","Ellie Nash","Eve Neely","Chloe Newman","Thomas Ng","Joel Nikolajczyk","Phillip Nikolayev","Chidinma Nwodo","Caroline O’Connor","Luca O’Donnell","Justin Ochalla","Alecsander Ochoa","Charles Ogletree","Tyler Osborne","Maya Osman","Zachary Packard","Caroline Palmatier","Emmanuel Panov","Andrew Patsios","Emma Patz","Erin Payne","Matthew Pelletier","Caleb Peress","Brian Perlman","Liana Perlman","Sarah Perlman","Elizabeth Phalen","William Popper","Samantha Porter","Matthew Powers","Alexandra Putprush","Noah Ramos","Shayan Raza","Brook Reilly","Jillian Reilly","Alexandra Resnick","Luke Risicato","Mark Roberts","Mozart Rodriguez","Lillian Rogers","Marco Roostaie","Ashley Rose","Matthew Rosenberg","Mia Rosengard","Elli Rozman","Giulia Rozzo","Nathan Ruddy","Jonathan Rudolph","Christian Rufo","Samuel Rutter","Elana Sadok","Asli Sahin","Alexandra Schmalz","Jacob Schneider","Gail Schor","Jackson Schwartz","Noah Schwartz","Nurit Schwartz","Shermar Scott","Thijs Seppenwolde","Claudia Sesso","Katherine Shannon","Benjamin Shapiro","Shaashwat Sharma","Emily Shaughnessy","Danielle Shaw","Raymond Shen","Jonathan Shia","Ethan Shifman","Forrest Shimazu","Charlotte Silverman","Eli Simon","Karalyn Sims","Anna Sinert","Francesca Sirignano","Hannah Smith","Matthew Smith","Meghan Smith","Hannah Spencer","Kayla Spitz","Zachary Sprinsky","Bradford Sprogis","Cole Steadman","Christina Steinberg","William Sten","Niamh Stokes","Emma Stoloff","Shane Stratford","Melissa Strauss","Joshua Stroup","Kyle Sullivan","Ryan Supple","Kevin Sutton","Evelyn Sweeney","Maxwell Sylvia","Nicholas Szeto","Siena Tacelli","Lev Taylor","Elliot Teeter","Eric Texeria","John Theall","Radley Theolien","Aisha Tipnis","Jordyn Tobasky","Anne Marie Toolan","Alon Trogan","Amber Tsui","Claire Vacca","William vallatini","Megan Van Alphen","Mihail Vasijuk","Michelle Veiner","Amelia Vettraino","Eliza Vogt","Julia Wainwright","Brendan Walsh","Daniel Walsh","Alex Warner","Carolyn Waters","Ryan Weitzel","Nicholas Whalen","Richard Wheeler","Maxwell Whelan","Adam Wilensky","Leslie Wong","Alyssa Woo","Liam Woodman","Joseph Woodnorth","Eric Wu","Stephen Xin","Christina Yang","Lauren Yee","Nina Yee","Caitlin Young","Aggelos Zymaris","Oludare Adegbesan","Jack Arentowicz","Sarah Bouamra","Mackenzie Carson","Eric Chen","Ethan Coleman","Benjamin Doss","Dillon Duvall","Jared Head","Nicholas Janne","Sarah Kaufman","Noah Lavine","Takya Lee","Frederick McGillicuddy","Kyle Rivera","Brandon Savejvong","Anthony Scaltas","Andy Seifer","Katherine Silva","Tristan Smyser","Andrei Treil","Dawit Woldegiorgis","Qi Zhu"]
newNames = ["David Abdurakhmanov","Marisa Abeles","Benjamin Aliber","Joseph Anastasi","Sofia Antonelli","Isabella Arbelaez","Andrew Arrondo","Hugh Atkinson","William Baker","Zoe Baker","Spencer Balder","Peter Bannon","Maeve Barker","Talia Barrett","Serena Bartlett","Joshua Batra","Jacob Bello","Griffin Berger","Andrew Berlinsky","Ketsia Bernard","Michael Bernard","Daniela Berner","Alexander Berney","Jaiman Bharadwa","Morgan Bilodeau","Andrew Blackburn","Olivia Blackmer","Alice Blake","Daniel Blumenstein","Sean Bogan","Reed Boisvert","Jonathan Bolivar","Melanie Bonilla","Daniel Borowsky","Alexandria Boutin","Maria Brasoveanu","Sydney Braunstein","Olivia Breen","Allison Brightman","Cate Brodowski","Victoria Bruce","Luke Bryson","David Busa","Pedro Caceres","You Cai","Timothy Callahan","Stephen Carr","Micah Carr-Gloth","Savannah Carucci","Holly Chadwick","Claire Chambers","Hamilton Champagne","Gabriella Chansky","Margaret Charter","Jason Child","Thomas Chmielewski","Brianna Chu","Marc Cifiello","Lauryne Civil","Kathryn Clancy","Daniel Cohen","Joshua Cohen","Shoshana Cohen","Thomas Cohen","Cameron Collyer","Mason Colwell","Maria L. Colon Figueroa","John Corbett","Henry Corderman","Tristan Coren","Nell Cosman","Julia Cuddy","Spencer Curran","Josie Dardinski","Julia Dasey","Abigail Dateo","Sebastian Davis","Stephen Demaio","Alexa DeMaria","Brittany DeMaria","Daniel DeMayo","Kelsey Desing","Benjamin Desmarais","Miriam DeSouza","Luis Diaz","Alexandra Diener","Nicolas Dimase","Isabel Dirks","Sarah Dodds","Jacob Doherty","Taylor Drew","Jacques Duport","Charles Eisenstadt","Alexander Ektov","Elise Erickson","Julia Evans","Sydney Fallon","Cole Fayemi","Dana Fernandez","Ava Feuer","Samuel Feuer","Sophie Findlay-Walters","Remi Fink","Logan Finn","Madison FitzGerald","Paul Flanagan","Sara Flano","Ryan Fleck","Joseph Fleming","Cameron Flynn","William Foley","Caroline Forbes","Karina Franco","Katya Franco","Taylor Frazzette","Madeline Frederick","Jason Freedman","Anna Friedman","Ella Friedman","Maxine Friedman","Mackenzie Fuller","Rose Gallagher","Saige Galovski","Hannah Garand","Anna Garf","Elise Gaudette","Anton Geyyer","Samantha Gilarde","Kyle Gilman","Benjamin Glanz","Nancy Glennon","Stephanie Godes","Spenser Goff","Ian Goldberg","Jacob Goldberg","Maya Golden","Ryan Goodale","Jenny Gould","Sachi Goyal","Kevin Grady","Jacob Grebber","Benjamin Greenes","Devin Griffin","Megan Griffin","Erica Guan","Rok Gundaker","Katherine Guttilla","Adrineh Guzelian","Timothy Hagerott","Lucy Hale","Natalie Hallagan","Payton Hartung","Jack Hayes","Connor Healey","Abigail Healy","Julia Hebert","Callista Hem","Sadye Herman","Abigail Hershenson","Kaylee Himmel","Garrett Hirsch","Sari Hirsh","Madeline Hluska","Kristin Ho","Julie Hoffmeister","Jeffrey Hohler","Sarah Hood","William Hood","Rachel Horrigan","Cohen Hu","XuanQiao Huang","Casey Hurwitch","Jayme Hurwitz","Alexandria Hwang","Jack Idelson","Marianna Jantzen","Thomas Jordan","Trent Kamke","Ethan Kams","Sonal Kango","Shih-Ting Kao","Daniel Kaplan","Samantha Karten","Dimitris Kartsagoulis","Nolan Katcher","Alyssa Katz","Mya Kearney","Benjamin Keegan","Henry Keegan","Samuel Keenan","Ana Keene","Davis Keene","Quinn Kelly","Henry Kennedy","Haley Kent","Ryan Kerrigan","Catherine Keshishyan","Samantha Keyes","Theresa Kim","Zoe Kim","Scott Kirschner","Parker Kirstein","Justin Kline","Symantha Komola","Anastasia Kopellas","Joshua Kornbleuth","Shilpa Krishnan","Jonathan Krushell","Jonah Kurker","Jacob Lagoon","Ivanna Lai","Justin Lam","Leo Leary","Ethan Lee","Samantha Lee","Jacob Lees","Steven Leicht","Celine Lemaire","Sebastian LeMay","Nicholas Lesanto","Julia Leshchiner","Michaela Leslie","Jack Levine","David Levy","Grace Li","Iris Li","Bergan Licht","Angel Lin","Kurt Lindenthal","Harrison Little","Seth Lockwood","Luke Lombardo","Henry London","Isabel Ludlow","Francesca Luppino","Craig Lustig","Kevin MacKenzie","Allison Mahoney","Megan Mahoney","Nicholas Mahoney","Caroline Malkin","Nicole Malouf","Nealaksi Maniraja","Eileen Manning","Caleb Marcus","David Marget","Beth Markman","Harrison Maron","David Martin","Ryan Martin","Max Masterson","Basil Matorin","Matthew Matossian","Philip Mazo","Rachel McCarthy","Grace McDonald","Lauren McGrath","Sebastian McKay","Bryce McKenzie","Cameron McLeod","Mikayla McNeill","Elizabeth Mesnik","Lily Mesnik","Leah Miller","Jordan Milstein","Mackenzie Mitchell","Stephanie Mittaz","Micaela Mittleman","Audrey Mock","Madeline Mollerus","Jake Monheimer","Shane Morley","Benjamin Moy","Calvin Mueller","Jason Mulno","John Murmes-Jarosz","Nicholas Murray","Natalie Mutter","Isabelle Nagle","Christopher Najarian","Ellie Nash","Eve Neely","Chloe Newman","Thomas Ng","Joel Nikolajczyk","Phillip Nikolayev","Chidinma Nwodo","Caroline O’Connor","Luca O’Donnell","Justin Ochalla","Alecsander Ochoa","Charles Ogletree","Tyler Osborne","Maya Osman","Zachary Packard","Caroline Palmatier","Emmanuel Panov","Andrew Patsios","Emma Patz","Erin Payne","Matthew Pelletier","Caleb Peress","Brian Perlman","Liana Perlman","Sarah Perlman","Elizabeth Phalen","William Popper","Samantha Porter","Matthew Powers","Alexandra Putprush","Noah Ramos","Shayan Raza","Brook Reilly","Jillian Reilly","Alexandra Resnick","Luke Risicato","Mark Roberts","Mozart Rodriguez","Lillian Rogers","Marco Roostaie","Ashley Rose","Matthew Rosenberg","Mia Rosengard","Elli Rozman","Giulia Rozzo","Nathan Ruddy","Jonathan Rudolph","Christian Rufo","Samuel Rutter","Elana Sadok","Asli Sahin","Alexandra Schmalz","Jacob Schneider","Gail Schor","Jackson Schwartz","Noah Schwartz","Nurit Schwartz","Shermar Scott","Thijs Seppenwolde","Claudia Sesso","Katherine Shannon","Benjamin Shapiro","Shaashwat Sharma","Emily Shaughnessy","Danielle Shaw","Raymond Shen","Jonathan Shia","Ethan Shifman","Forrest Shimazu","Charlotte Silverman","Eli Simon","Karalyn Sims","Anna Sinert","Francesca Sirignano","Hannah Smith","Matthew Smith","Meghan Smith","Hannah Spencer","Kayla Spitz","Zachary Sprinsky","Bradford Sprogis","Cole Steadman","Christina Steinberg","William Sten","Niamh Stokes","Emma Stoloff","Shane Stratford","Melissa Strauss","Joshua Stroup","Kyle Sullivan","Ryan Supple","Kevin Sutton","Evelyn Sweeney","Maxwell Sylvia","Nicholas Szeto","Siena Tacelli","Lev Taylor","Elliot Teeter","Eric Texeria","John Theall","Radley Theolien","Aisha Tipnis","Jordyn Tobasky","Anne Marie Toolan","Alon Trogan","Amber Tsui","Claire Vacca","William vallatini","Megan Van Alphen","Mihail Vasijuk","Michelle Veiner","Amelia Vettraino","Eliza Vogt","Julia Wainwright","Brendan Walsh","Daniel Walsh","Alex Warner","Carolyn Waters","Ryan Weitzel","Nicholas Whalen","Richard Wheeler","Maxwell Whelan","Adam Wilensky","Leslie Wong","Alyssa Woo","Liam Woodman","Joseph Woodnorth","Eric Wu","Stephen Xin","Christina Yang","Lauren Yee","Nina Yee","Caitlin Young","Aggelos Zymaris","Oludare Adegbesan","Jack Arentowicz","Sarah Bouamra","Mackenzie Carson","Eric Chen","Ethan Coleman","Benjamin Doss","Dillon Duvall","Jared Head","Nicholas Janne","Sarah Kaufman","Noah Lavine","Takya Lee","Frederick McGillicuddy","Kyle Rivera","Brandon Savejvong","Anthony Scaltas","Andy Seifer","Katherine Silva","Tristan Smyser","Andrei Treil","Dawit Woldegiorgis","Qi Zhu"]
counts = np.zeros(len(names))
# accepted, removed, winners = list(), list(), list()
# theme = "a fight"
#
# scores = dict(zip(names,counts.T))
# rounds = 0
# deathmatchChoices = 0

# deathmatch simulation
#random.shuffle(names)
def initSession(request, isReset):
    if not request.session._session:
        names = newNames
        random.shuffle(names)
        request.session['names'] = names
        request.session['removed'] = list()
        request.session['accepted'] = list()
        request.session['winners'] = list()
        request.session['scores'] = dict(zip(names, counts.T))
        request.session['theme'] = "a fight"
        request.session['rounds'] = 0
        request.session['deathmatchChoices'] = 0
        request.session['isDeathmatch'] = False
        request.session['isActive'] = True
        request.session.set_expiry(0)
        #print("started")
    elif isReset == True: # if names doesn't exist yet
        names = newNames
        random.shuffle(names)
        request.session['names'] = names
        request.session['removed'] = list()
        request.session['accepted'] = list()
        request.session['winners'] = list()
        request.session['scores'] = dict(zip(names,counts.T))
        request.session['theme'] = "a fight"
        request.session['rounds'] = 0
        request.session['deathmatchChoices'] = 0
        request.session.set_expiry(0)
        #print("reset")
    else:
        #print("done")
        pass


def get_person(request):
    while True:
        p = random.choice(request.session['names'])
        if p not in request.session['accepted']:
            return p
        else:
            pass

def getCount(request, person):
    return request.session['scores'][person]

def increaseCount(request, person, amount):
    try:
        request.session['scores'][person] += amount
        return "success"
    except:
        return "Person Not Found!"

def accept_person(request, person):
    acc = request.session['accepted']
    n = request.session['names']
    if person in request.session['names']:
        acc.append(person)
        n.remove(person)
        request.session['accepted'] = acc
        request.session['names'] = n
    else:
        a = difflib.get_close_matches(person, request.session['names'])
        if len(a) > 1:
            request.session['accepted'].append(a[0])
            request.session['names'].remove(a[0])
        else:
            pass

def delete_person(request, person):
    rem = request.session['removed']
    n = request.session['names']
    s = request.session['scores']
    rem.append(person)
    n.remove(person)
    s[person] = s[person] - 1.0

    request.session['removed'] = rem
    request.session['names'] = n
    request.session['scores'] = s
    #print(len(request.session['names']))
    #print("Deleted {}".format(person))

def getNumberLeft(request):
    if len(request.session['names']) >= 256:
        return 181-len(request.session['removed'])
    else:
        return 0

def getNumberAccepted(request):
    return len(request.session['accepted'])

def reset(request):
    # if (getNumberLeft(request) == 0 or getNumberAccepted(request) == 256):
    #     request.session['names'] = request.session['names'].clear()
    #     request.session['names'] = request.session['names'].extend(newNames)
    #     random.shuffle(request.session['names'])
    #     request.session['removed'] = request.session['removed'].clear()
    #     request.session['accepted'] = request.session['accepted'].clear()
    #     request.session['names'] = request.session['names'].extend(request.session['removed'])
    #     request.session['names'] = request.session['names'].extend(request.session['accepted'])
    # random.shuffle(request.session['names'])
    # request.session['removed'].clear()
    # request.session['accepted'].clear()
    # request.session['winners'].clear()
    # request.session['scores'] = dict.fromkeys(request.session['scores'],0.0)
    # request.session['rounds'] = 0
    # request.session['theme'] = 'a fight'
    # request.session['deathmatchChoices'] = 0
    initSession(request, True)

def setUpDeathmatch(request):
    acc = request.session['accepted']
    rem = request.session['removed']
    n = request.session['names']
    random.shuffle(acc)
    if len(acc) != 256 and len(rem) == 181 and request.session['isDeathmatch'] == False: # if we removed 181 people
        acc.extend(names)
        n.clear()
    request.session['accepted'] = acc
    request.session['removed'] = rem
    request.session['names'] = n
    # elif len(accepted) != 256 and len(removed) != 181: # if we accepted a mix
    #     accepted.extend(names)
    #     accepted = removeDuplicates(accepted)
    #print("Accepted length: {}".format(len(accepted)))
    #print("Winners length: {}".format(len(winners)))

def getNextPair(request):
    acc = request.session['accepted']
    ppl = acc[:2]
    # del acc[:2]
    request.session['accepted'] = acc
    return ppl

def addWinner(request, person):
    win = request.session['winners']
    win.append(person)
    request.session['deathmatchChoices'] = request.session['deathmatchChoices'] + 1
    request.session['winners'] = win

def isRoundOver(request):
    return len(request.session['accepted']) <= 0

def startNewRound(request):
    print("new round")
    acc = request.session['accepted']
    win = request.session['winners']
    print(len(win))
    acc.extend(win)
    print(len(acc))
    win.clear()
    request.session['rounds'] = request.session['rounds'] + 1
    request.session['accepted'] = acc
    request.session['winners'] = win
    # losersBracketSetup(rounds)

def getRounds(request):
    return request.session['rounds']

def isGameOver(request):
    return request.session['rounds'] == 8 and len(request.session['accepted']) == 1

def generateRandomBracket(request):
    # names.clear()
    # names.extend(newNames)
    for i in range(181 - len(request.session['removed'])):
        delete_person(request, get_person(request))
    for i in range(256 - len(request.session['accepted'])):
        accept_person(request, get_person(request))

    #print("Accepted: {}".format(len(request.session['accepted'])))

def getSortedDict(request):
    v = {}
    for key, value in sorted(request.session['scores'].items(), key=operator.itemgetter(1)):
        v.setdefault(value, []).append(key)
    return v


def getProgress(request):
    return round(request.session['deathmatchChoices']/255.0 * 100, 2)

# def simulate():
#     generateRandomBracket()
#     while rounds <= 10:
#         while not isRoundOver():
#             if(len(accepted) == 256):
#                 p1, p2 = accepted[:2]
#                 del accepted[:2]
#                 personChosen = random.choice([p1, p2])
#                 addWinner(personChosen)
#                 increaseCount(personChosen, 1.0)
#             else:
#                 p1, p2 = getNextPair()
#                 personChosen = random.choice([p1,p2])
#                 addWinner(personChosen)
#                 if rounds <= 10:
#                     increaseCount(personChosen, 1.0)
#                 else:
#                     increaseCount(personChosen, .5)
#                 setUpDeathmatch()
#         startNewRound()
#         print(rounds)
#     print(getSortedDict())
#         # print(getSortedDict())

def getTheme(request):
    return request.session['theme']

def setTheme(request, competition):
    request.session['theme'] = competition

def printEverything(request):
    print(len(request.session['names']))
    print(len(request.session['accepted']))
    print(len(request.session['removed']))
    print(len(request.session['winners']))