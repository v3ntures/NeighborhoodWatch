import requests
from bs4 import BeautifulSoup

###########Imports###########

#Drude Report
drudge = requests.get('http://drudgereport.com/')
drudge.raise_for_status()

#Zero Hedge
zH = requests.get('http://www.zerohedge.com/')
zH.raise_for_status()

#Natural News
nN = requests.get('http://www.naturalnews.com/#')
nN.raise_for_status()

#Info Wars
iW = requests.get('http://www.infowars.com/')
iW.raise_for_status()

#Ground Zero
gZ = requests.get('http://www.groundzeromedia.org/category/articles/')
gZ.raise_for_status()

###########Parsing###########

#Drudge Report
drudgeReport = BeautifulSoup(drudge.text,"html.parser")

#Zero Hedge
zeroHedge = BeautifulSoup(zH.text,"html.parser")

#Natural News
naturalNews = BeautifulSoup(nN.text,"html.parser")

#Info Wars
infoWars = BeautifulSoup(iW.text,"html.parser")

#Ground Zero
groundZero = BeautifulSoup(gZ.text,"html.parser")

###########Crawl###########

#Drudge Report
drudgeElems = drudgeReport.select('b > a')

#Zero Hedge
zeroHedgeElems = zeroHedge.select('.content-box-1 > h2 > a')

#Natural News
naturalNewsElems = naturalNews.select('.IFH > a')

#Info Wars
infoWarsElems = infoWars.select('.article-content > h3 > a')

#Ground Zero
GroundZeroElems = groundZero.select('article > header > h1 > a')

###########Output###########
stories = []

def buildLinks(elements):
    i = 0
    while i < len(elements):
            link = elements[i].get('href')
            title = elements[i].getText()
            complete = "<div class='story'><a href='{0}'>{1}</a></div><br>".format(link,title)
            stories.append(complete)
            #print (complete)
            i = i + 1


buildLinks(zeroHedgeElems)
buildLinks(drudgeElems)
buildLinks(naturalNewsElems)
buildLinks(infoWarsElems)
buildLinks(GroundZeroElems)

#Write HTML File
with open('C:/Users/lqdev_000/Documents/Development/NeighborhoodWatch/index.html','w') as file:
    
    file.write("<!DOCTYPE html>\n\
    <html>\n\
    <head>\n\
        <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css' integrity='sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7' crossorigin='anonymous'>\n\
        <link rel='stylesheet' href='main.css'>\n\
        <script>\n\
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n\
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n\
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n\
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n\
            ga('create', 'UA-71617038-1', 'auto');\n\
            ga('send', 'pageview');\n\
        </script>\n\
        <meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no'>\n\
        <title>Neightborhood Watch</title>\n\
    </head>\n\
    <body class='container-fluid'>\n\
            <div id='top'>\n\
                <h1><span class='glyphicon glyphicon-eye-open' aria-hidden='true'></span>Neighborhood Watch</h1>\n\
                <h2>Staying Vigilant of the Overseers</h2>\n\
            </div>\n\
            <div id='stories'>\n\
        ")

    for story in stories:
        file.write(story + "\n")
    
    file.write("</div>\n\
        <script async src='//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'></script>\n\
        <!-- Mobile -->\n\
        <ins class='adsbygoogle'\n\
            style='display:block'\n\
            data-ad-client='ca-pub-6386433729094097'\n\
            data-ad-slot='9394532162'\n\
            data-ad-format='link'></ins>\n\
        <script>\n\
        (adsbygoogle = window.adsbygoogle || []).push({});\n\
    </script>\n\
    </body>\n\
    </html>")
    
    if(file.closed == False):
        file.close()

print (len(stories))
