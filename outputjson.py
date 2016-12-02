import json

def outputprep(output):

    d={}
    
    d["Name"] = output[0][0]
    d["LastTradePriceOnly"]=float(output[0][1].replace(',',''))
    if output[0][1]!='UNCH':
        d["Change"]=float(output[0][2].replace(',',''))
    else:
        d["Change"]=0
    
    d["PercentageChange"]=output[0][3]
    return d



'''

    # quote list of dic
    # result dic
    # d individual quote
    quote = []
    d={}
    d["Name"] = "Luke"
    d["LastTradePriceOnly"]='111'
    d["Change"]="50"
    d["PercentageChange"]="1%"
    quote.append(d)
    result={"quote":quote}
    output={'result':result}
    a=json.dumps(output)
    print(a)
   '''