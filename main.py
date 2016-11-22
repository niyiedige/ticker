
from getinfo import getinfo
from input import inputfromexcel
from output import output


raws=inputfromexcel('input.xlsx','input')
outputlist=[]
#multithread
#jason

for raw in raws:
    z=getinfo(raw)
    outputlist+=z
output(outputlist)