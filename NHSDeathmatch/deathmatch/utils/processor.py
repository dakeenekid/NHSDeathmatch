import random
import numpy as np
import math
names = ["David Abdurakhmanov","Marisa Abeles","Benjamin Aliber","Joseph Anastasi","Sofia Antonelli","Isabella Arbelaez","Andrew Arrondo","Hugh Atkinson","William Baker","Zoe Baker","Spencer Balder","Peter Bannon","Maeve Barker","Talia Barrett","Serena Bartlett","Joshua Batra","Jacob Bello","Griffin Berger","Andrew Berlinsky","Ketsia Bernard","Michael Bernard","Daniela Berner","Alexander Berney","Jaiman Bharadwa","Morgan Bilodeau","Andrew Blackburn","Olivia Blackmer","Alice Blake","Daniel Blumenstein","Sean Bogan","Reed Boisvert","Jonathan Bolivar","Melanie Bonilla","Daniel Borowsky","Alexandria Boutin","Maria Brasoveanu","Sydney Braunstein","Olivia Breen","Allison Brightman","Cate Brodowski","Victoria Bruce","Luke Bryson","David Busa","Pedro Caceres","You Cai","Timothy Callahan","Stephen Carr","Micah Carr-Gloth","Savannah Carucci","Holly Chadwick","Claire Chambers","Hamilton Champagne","Gabriella Chansky","Margaret Charter","Jason Child","Thomas Chmielewski","Brianna Chu","Marc Cifiello","Lauryne Civil","Kathryn Clancy","Daniel Cohen","Joshua Cohen","Shoshana Cohen","Thomas Cohen","Cameron Collyer","Mason Colwell","Maria L. Colon Figueroa","John Corbett","Henry Corderman","Tristan Coren","Nell Cosman","Julia Cuddy","Spencer Curran","Josie Dardinski","Julia Dasey","Abigail Dateo","Sebastian Davis","Stephen Demaio","Alexa DeMaria","Brittany DeMaria","Daniel DeMayo","Kelsey Desing","Benjamin Desmarais","Miriam DeSouza","Luis Diaz","Alexandra Diener","Nicolas Dimase","Isabel Dirks","Sarah Dodds","Jacob Doherty","Taylor Drew","Jacques Duport","Charles Eisenstadt","Alexander Ektov","Elise Erickson","Julia Evans","Sydney Fallon","Cole Fayemi","Dana Fernandez","Ava Feuer","Samuel Feuer","Sophie Findlay-Walters","Remi Fink","Logan Finn","Madison FitzGerald","Paul Flanagan","Sara Flano","Ryan Fleck","Joseph Fleming","Cameron Flynn","William Foley","Caroline Forbes","Karina Franco","Katya Franco","Taylor Frazzette","Madeline Frederick","Jason Freedman","Anna Friedman","Ella Friedman","Maxine Friedman","Mackenzie Fuller","Rose Gallagher","Saige Galovski","Hannah Garand","Anna Garf","Elise Gaudette","Anton Geyyer","Samantha Gilarde","Kyle Gilman","Benjamin Glanz","Nancy Glennon","Stephanie Godes","Spenser Goff","Ian Goldberg","Jacob Goldberg","Maya Golden","Ryan Goodale","Jenny Gould","Sachi Goyal","Kevin Grady","Jacob Grebber","Benjamin Greenes","Devin Griffin","Megan Griffin","Erica Guan","Rok Gundaker","Katherine Guttilla","Adrineh Guzelian","Timothy Hagerott","Lucy Hale","Natalie Hallagan","Payton Hartung","Jack Hayes","Connor Healey","Abigail Healy","Julia Hebert","Callista Hem","Sadye Herman","Abigail Hershenson","Kaylee Himmel","Garrett Hirsch","Sari Hirsh","Madeline Hluska","Kristin Ho","Julie Hoffmeister","Jeffrey Hohler","Sarah Hood","William Hood","Rachel Horrigan","Cohen Hu","XuanQiao Huang","Casey Hurwitch","Jayme Hurwitz","Alexandria Hwang","Jack Idelson","Marianna Jantzen","Thomas Jordan","Trent Kamke","Ethan Kams","Sonal Kango","Shih-Ting Kao","Daniel Kaplan","Samantha Karten","Dimitris Kartsagoulis","Nolan Katcher","Alyssa Katz","Mya Kearney","Benjamin Keegan","Henry Keegan","Samuel Keenan","Ana Keene","Davis Keene","Quinn Kelly","Henry Kennedy","Haley Kent","Ryan Kerrigan","Catherine Keshishyan","Samantha Keyes","Theresa Kim","Zoe Kim","Scott Kirschner","Parker Kirstein","Justin Kline","Symantha Komola","Anastasia Kopellas","Joshua Kornbleuth","Shilpa Krishnan","Jonathan Krushell","Jonah Kurker","Jacob Lagoon","Ivanna Lai","Justin Lam","Leo Leary","Ethan Lee","Samantha Lee","Jacob Lees","Steven Leicht","Celine Lemaire","Sebastian LeMay","Nicholas Lesanto","Julia Leshchiner","Michaela Leslie","Jack Levine","David Levy","Grace Li","Iris Li","Bergan Licht","Angel Lin","Kurt Lindenthal","Harrison Little","Seth Lockwood","Luke Lombardo","Henry London","Isabel Ludlow","Francesca Luppino","Craig Lustig","Kevin MacKenzie","Allison Mahoney","Megan Mahoney","Nicholas Mahoney","Caroline Malkin","Nicole Malouf","Nealaksi Maniraja","Eileen Manning","Caleb Marcus","David Marget","Beth Markman","Harrison Maron","David Martin","Ryan Martin","Max Masterson","Basil Matorin","Matthew Matossian","Philip Mazo","Rachel McCarthy","Grace McDonald","Lauren McGrath","Sebastian McKay","Bryce McKenzie","Cameron McLeod","Mikayla McNeill","Elizabeth Mesnik","Lily Mesnik","Leah Miller","Jordan Milstein","Mackenzie Mitchell","Stephanie Mittaz","Micaela Mittleman","Audrey Mock","Madeline Mollerus","Jake Monheimer","Shane Morley","Benjamin Moy","Calvin Mueller","Jason Mulno","John Murmes-Jarosz","Nicholas Murray","Natalie Mutter","Isabelle Nagle","Christopher Najarian","Ellie Nash","Eve Neely","Chloe Newman","Thomas Ng","Joel Nikolajczyk","Phillip Nikolayev","Chidinma Nwodo","Caroline O’Connor","Luca O’Donnell","Justin Ochalla","Alecsander Ochoa","Charles Ogletree","Tyler Osborne","Maya Osman","Zachary Packard","Caroline Palmatier","Emmanuel Panov","Andrew Patsios","Emma Patz","Erin Payne","Matthew Pelletier","Caleb Peress","Brian Perlman","Liana Perlman","Sarah Perlman","Elizabeth Phalen","William Popper","Samantha Porter","Matthew Powers","Alexandra Putprush","Noah Ramos","Shayan Raza","Brook Reilly","Jillian Reilly","Alexandra Resnick","Luke Risicato","Mark Roberts","Mozart Rodriguez","Lillian Rogers","Marco Roostaie","Ashley Rose","Matthew Rosenberg","Mia Rosengard","Elli Rozman","Giulia Rozzo","Nathan Ruddy","Jonathan Rudolph","Christian Rufo","Samuel Rutter","Elana Sadok","Asli Sahin","Alexandra Schmalz","Jacob Schneider","Gail Schor","Jackson Schwartz","Noah Schwartz","Nurit Schwartz","Shermar Scott","Thijs Seppenwolde","Claudia Sesso","Katherine Shannon","Benjamin Shapiro","Shaashwat Sharma","Emily Shaughnessy","Danielle Shaw","Raymond Shen","Jonathan Shia","Ethan Shifman","Forrest Shimazu","Charlotte Silverman","Eli Simon","Karalyn Sims","Anna Sinert","Francesca Sirignano","Hannah Smith","Matthew Smith","Meghan Smith","Hannah Spencer","Kayla Spitz","Zachary Sprinsky","Bradford Sprogis","Cole Steadman","Christina Steinberg","William Sten","Niamh Stokes","Emma Stoloff","Shane Stratford","Melissa Strauss","Joshua Stroup","Kyle Sullivan","Ryan Supple","Kevin Sutton","Evelyn Sweeney","Maxwell Sylvia","Nicholas Szeto","Siena Tacelli","Lev Taylor","Elliot Teeter","Eric Texeria","John Theall","Radley Theolien","Aisha Tipnis","Jordyn Tobasky","Anne Marie Toolan","Alon Trogan","Amber Tsui","Claire Vacca","William vallatini","Megan Van Alphen","Mihail Vasijuk","Michelle Veiner","Amelia Vettraino","Eliza Vogt","Julia Wainwright","Brendan Walsh","Daniel Walsh","Alex Warner","Carolyn Waters","Ryan Weitzel","Nicholas Whalen","Richard Wheeler","Maxwell Whelan","Adam Wilensky","Leslie Wong","Alyssa Woo","Liam Woodman","Joseph Woodnorth","Eric Wu","Stephen Xin","Christina Yang","Lauren Yee","Nina Yee","Caitlin Young","Aggelos Zymaris","Oludare Adegbesan","Jack Arentowicz","Sarah Bouamra","Mackenzie Carson","Eric Chen","Ethan Coleman","Benjamin Doss","Dillon Duvall","Jared Head","Nicholas Janne","Sarah Kaufman","Noah Lavine","Takya Lee","Frederick McGillicuddy","Kyle Rivera","Brandon Savejvong","Anthony Scaltas","Andy Seifer","Katherine Silva","Tristan Smyser","Andrei Treil","Dawit Woldegiorgis","Qi Zhu"]
newNames = ["David Abdurakhmanov","Marisa Abeles","Benjamin Aliber","Joseph Anastasi","Sofia Antonelli","Isabella Arbelaez","Andrew Arrondo","Hugh Atkinson","William Baker","Zoe Baker","Spencer Balder","Peter Bannon","Maeve Barker","Talia Barrett","Serena Bartlett","Joshua Batra","Jacob Bello","Griffin Berger","Andrew Berlinsky","Ketsia Bernard","Michael Bernard","Daniela Berner","Alexander Berney","Jaiman Bharadwa","Morgan Bilodeau","Andrew Blackburn","Olivia Blackmer","Alice Blake","Daniel Blumenstein","Sean Bogan","Reed Boisvert","Jonathan Bolivar","Melanie Bonilla","Daniel Borowsky","Alexandria Boutin","Maria Brasoveanu","Sydney Braunstein","Olivia Breen","Allison Brightman","Cate Brodowski","Victoria Bruce","Luke Bryson","David Busa","Pedro Caceres","You Cai","Timothy Callahan","Stephen Carr","Micah Carr-Gloth","Savannah Carucci","Holly Chadwick","Claire Chambers","Hamilton Champagne","Gabriella Chansky","Margaret Charter","Jason Child","Thomas Chmielewski","Brianna Chu","Marc Cifiello","Lauryne Civil","Kathryn Clancy","Daniel Cohen","Joshua Cohen","Shoshana Cohen","Thomas Cohen","Cameron Collyer","Mason Colwell","Maria L. Colon Figueroa","John Corbett","Henry Corderman","Tristan Coren","Nell Cosman","Julia Cuddy","Spencer Curran","Josie Dardinski","Julia Dasey","Abigail Dateo","Sebastian Davis","Stephen Demaio","Alexa DeMaria","Brittany DeMaria","Daniel DeMayo","Kelsey Desing","Benjamin Desmarais","Miriam DeSouza","Luis Diaz","Alexandra Diener","Nicolas Dimase","Isabel Dirks","Sarah Dodds","Jacob Doherty","Taylor Drew","Jacques Duport","Charles Eisenstadt","Alexander Ektov","Elise Erickson","Julia Evans","Sydney Fallon","Cole Fayemi","Dana Fernandez","Ava Feuer","Samuel Feuer","Sophie Findlay-Walters","Remi Fink","Logan Finn","Madison FitzGerald","Paul Flanagan","Sara Flano","Ryan Fleck","Joseph Fleming","Cameron Flynn","William Foley","Caroline Forbes","Karina Franco","Katya Franco","Taylor Frazzette","Madeline Frederick","Jason Freedman","Anna Friedman","Ella Friedman","Maxine Friedman","Mackenzie Fuller","Rose Gallagher","Saige Galovski","Hannah Garand","Anna Garf","Elise Gaudette","Anton Geyyer","Samantha Gilarde","Kyle Gilman","Benjamin Glanz","Nancy Glennon","Stephanie Godes","Spenser Goff","Ian Goldberg","Jacob Goldberg","Maya Golden","Ryan Goodale","Jenny Gould","Sachi Goyal","Kevin Grady","Jacob Grebber","Benjamin Greenes","Devin Griffin","Megan Griffin","Erica Guan","Rok Gundaker","Katherine Guttilla","Adrineh Guzelian","Timothy Hagerott","Lucy Hale","Natalie Hallagan","Payton Hartung","Jack Hayes","Connor Healey","Abigail Healy","Julia Hebert","Callista Hem","Sadye Herman","Abigail Hershenson","Kaylee Himmel","Garrett Hirsch","Sari Hirsh","Madeline Hluska","Kristin Ho","Julie Hoffmeister","Jeffrey Hohler","Sarah Hood","William Hood","Rachel Horrigan","Cohen Hu","XuanQiao Huang","Casey Hurwitch","Jayme Hurwitz","Alexandria Hwang","Jack Idelson","Marianna Jantzen","Thomas Jordan","Trent Kamke","Ethan Kams","Sonal Kango","Shih-Ting Kao","Daniel Kaplan","Samantha Karten","Dimitris Kartsagoulis","Nolan Katcher","Alyssa Katz","Mya Kearney","Benjamin Keegan","Henry Keegan","Samuel Keenan","Ana Keene","Davis Keene","Quinn Kelly","Henry Kennedy","Haley Kent","Ryan Kerrigan","Catherine Keshishyan","Samantha Keyes","Theresa Kim","Zoe Kim","Scott Kirschner","Parker Kirstein","Justin Kline","Symantha Komola","Anastasia Kopellas","Joshua Kornbleuth","Shilpa Krishnan","Jonathan Krushell","Jonah Kurker","Jacob Lagoon","Ivanna Lai","Justin Lam","Leo Leary","Ethan Lee","Samantha Lee","Jacob Lees","Steven Leicht","Celine Lemaire","Sebastian LeMay","Nicholas Lesanto","Julia Leshchiner","Michaela Leslie","Jack Levine","David Levy","Grace Li","Iris Li","Bergan Licht","Angel Lin","Kurt Lindenthal","Harrison Little","Seth Lockwood","Luke Lombardo","Henry London","Isabel Ludlow","Francesca Luppino","Craig Lustig","Kevin MacKenzie","Allison Mahoney","Megan Mahoney","Nicholas Mahoney","Caroline Malkin","Nicole Malouf","Nealaksi Maniraja","Eileen Manning","Caleb Marcus","David Marget","Beth Markman","Harrison Maron","David Martin","Ryan Martin","Max Masterson","Basil Matorin","Matthew Matossian","Philip Mazo","Rachel McCarthy","Grace McDonald","Lauren McGrath","Sebastian McKay","Bryce McKenzie","Cameron McLeod","Mikayla McNeill","Elizabeth Mesnik","Lily Mesnik","Leah Miller","Jordan Milstein","Mackenzie Mitchell","Stephanie Mittaz","Micaela Mittleman","Audrey Mock","Madeline Mollerus","Jake Monheimer","Shane Morley","Benjamin Moy","Calvin Mueller","Jason Mulno","John Murmes-Jarosz","Nicholas Murray","Natalie Mutter","Isabelle Nagle","Christopher Najarian","Ellie Nash","Eve Neely","Chloe Newman","Thomas Ng","Joel Nikolajczyk","Phillip Nikolayev","Chidinma Nwodo","Caroline O’Connor","Luca O’Donnell","Justin Ochalla","Alecsander Ochoa","Charles Ogletree","Tyler Osborne","Maya Osman","Zachary Packard","Caroline Palmatier","Emmanuel Panov","Andrew Patsios","Emma Patz","Erin Payne","Matthew Pelletier","Caleb Peress","Brian Perlman","Liana Perlman","Sarah Perlman","Elizabeth Phalen","William Popper","Samantha Porter","Matthew Powers","Alexandra Putprush","Noah Ramos","Shayan Raza","Brook Reilly","Jillian Reilly","Alexandra Resnick","Luke Risicato","Mark Roberts","Mozart Rodriguez","Lillian Rogers","Marco Roostaie","Ashley Rose","Matthew Rosenberg","Mia Rosengard","Elli Rozman","Giulia Rozzo","Nathan Ruddy","Jonathan Rudolph","Christian Rufo","Samuel Rutter","Elana Sadok","Asli Sahin","Alexandra Schmalz","Jacob Schneider","Gail Schor","Jackson Schwartz","Noah Schwartz","Nurit Schwartz","Shermar Scott","Thijs Seppenwolde","Claudia Sesso","Katherine Shannon","Benjamin Shapiro","Shaashwat Sharma","Emily Shaughnessy","Danielle Shaw","Raymond Shen","Jonathan Shia","Ethan Shifman","Forrest Shimazu","Charlotte Silverman","Eli Simon","Karalyn Sims","Anna Sinert","Francesca Sirignano","Hannah Smith","Matthew Smith","Meghan Smith","Hannah Spencer","Kayla Spitz","Zachary Sprinsky","Bradford Sprogis","Cole Steadman","Christina Steinberg","William Sten","Niamh Stokes","Emma Stoloff","Shane Stratford","Melissa Strauss","Joshua Stroup","Kyle Sullivan","Ryan Supple","Kevin Sutton","Evelyn Sweeney","Maxwell Sylvia","Nicholas Szeto","Siena Tacelli","Lev Taylor","Elliot Teeter","Eric Texeria","John Theall","Radley Theolien","Aisha Tipnis","Jordyn Tobasky","Anne Marie Toolan","Alon Trogan","Amber Tsui","Claire Vacca","William vallatini","Megan Van Alphen","Mihail Vasijuk","Michelle Veiner","Amelia Vettraino","Eliza Vogt","Julia Wainwright","Brendan Walsh","Daniel Walsh","Alex Warner","Carolyn Waters","Ryan Weitzel","Nicholas Whalen","Richard Wheeler","Maxwell Whelan","Adam Wilensky","Leslie Wong","Alyssa Woo","Liam Woodman","Joseph Woodnorth","Eric Wu","Stephen Xin","Christina Yang","Lauren Yee","Nina Yee","Caitlin Young","Aggelos Zymaris","Oludare Adegbesan","Jack Arentowicz","Sarah Bouamra","Mackenzie Carson","Eric Chen","Ethan Coleman","Benjamin Doss","Dillon Duvall","Jared Head","Nicholas Janne","Sarah Kaufman","Noah Lavine","Takya Lee","Frederick McGillicuddy","Kyle Rivera","Brandon Savejvong","Anthony Scaltas","Andy Seifer","Katherine Silva","Tristan Smyser","Andrei Treil","Dawit Woldegiorgis","Qi Zhu"]
counts = np.zeros(len(names))
accepted, removed, winners = list(), list(), list()

scores = dict(zip(names,counts.T))
rounds = 0

# deathmatch simulation
#random.shuffle(names)

def get_person():
    while True:
        p = random.choice(names)
        if p not in accepted:
            return p
        else:
            pass

def getCount(person):
    return scores[person]

def increaseCount(person):
    try:
        scores[person] += 1.0
        return "success"
    except:
        return "Person Not Found!"

def removeDuplicates(listofElements):
    # Create an empty list to store unique elements
    uniqueList = []

    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    # Return the list of unique elements
    return uniqueList


def accept_person(person):
    accepted.append(person)
    names.remove(person)

def delete_person(person):
    removed.append(person)
    names.remove(person)
    #print("Deleted {}".format(person))

def getNumberLeft():
    if len(names) >= 256:
        return len(names)+len(accepted)-256
    else:
        return 0

def getNumberAccepted():
    return len(accepted)

def reset():
    if (getNumberLeft() == 0 or getNumberAccepted() == 256):
        names.clear()
        names.extend(newNames)
        random.shuffle(names)
        removed.clear()
        accepted.clear()
    names.extend(removed)
    random.shuffle(names)
    removed.clear()
    accepted.clear()

def setUpDeathmatch():
    global accepted
    random.shuffle(accepted)
    if len(accepted) != 256 and len(removed) == 181: # if we removed 181 people
        accepted.extend(names)
        names.clear()
    elif len(accepted) != 256 and len(removed) != 181: # if we accepted a mix
        accepted.extend(names)
        accepted = removeDuplicates(accepted)
        names.clear()
    print("Accepted length: {}".format(len(accepted)))
    print("Winners length: {}".format(len(winners)))

def getNextPair():
    ppl = accepted[:2]
    del accepted[:2]
    return ppl

def addWinner(person):
    winners.append(person)

def isRoundOver():
    return len(accepted) <= 0

def startNewRound():
    accepted.extend(winners)
    winners.clear()
    global rounds
    rounds += 1

def getRounds():
    return rounds

def isGameOver():
    return len(accepted) == 1

def generateRandomBracket():
    names.clear()
    names.extend(newNames)
    for i in range(256):
        accept_person(get_person())
    for i in range(181):
        delete_person(random.choice(names))