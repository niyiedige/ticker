
from downloader import Downloader
from lxml import html
from clearstr import clearstr
from clearstr import seperatestr
from urllib.parse import urlparse
#from input import inputfromexcel
link='http://data.cnbc.com/quotes/.SPX'
sss={"link":'http://data.cnbc.com/quotes/.SPX','xpathlist':['//*[@id="cnbc-contents"]/div/section/div[1]/div[1]/table/tbody/tr/td[1]/span[1]/text()','//*[@id="cnbc-contents"]/div/section/div[1]/div[1]/table/tbody/tr/td[2]/div[1]/span/text()']}

def getinfo(datestructure_dic):
    #1.download,cache page
    #2.get xpathlist
    #3.get the infomation needed


    input=datestructure_dic
    targetlist=[input["link"]]
    targetxpath=input["xpathlist"]
    joblist=[]

    #can use pop here for multithread
    for link in targetlist:

        page = Downloader.download(link)
        tree = html.fromstring(page)

        scarpeinfo=[input['Ticker']]
        if input['Ticker']=='HANG SENG':
            a=tree.xpath('//*[@id="cnnBody"]/div[1]/div/div[2]/table/tbody/tr/td[1]/span/text()')[0]

            scarpeinfo.append(clearstr(a))
            scarpeinfo.append(clearstr(tree.xpath('//*[@id="cnnBody"]/div[1]/div/div[2]/table/tbody/tr/td[2]/span[2]/span/text()')[0]))
            scarpeinfo.append(clearstr(tree.xpath('//*[@id="cnnBody"]/div[1]/div/div[2]/table/tbody/tr/td[2]/span[4]/span/text()')[0]))
        else:
            for xpath in targetxpath:
                if xpath!=None:
                    #z is constantly changing, can be empty some time
                    z=tree.xpath(xpath)
                    if z:
                        print(z)
                        t=clearstr(z[0])
                        if t=="":
                            try:
                                t=clearstr(z[1])
                                scarpeinfo.append(t)

                            except IndexError:
                                scarpeinfo.append('Destination empty')

                        else:
                            scarpeinfo.append(t)
                    else:
                        scarpeinfo.append('xpath empty')

                else:
                    scarpeinfo.append('Not available')
            temp1=seperatestr(scarpeinfo[2])
            scarpeinfo[2]=temp1[0]
            scarpeinfo.append(temp1[1])
        joblist.append(scarpeinfo)
    return joblist
#print(getinfo(sss))

    #4.generate a new out put datacollection
    #returm it

