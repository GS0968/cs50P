import re

def main():
    state=parse(str(input("HTML: ")))
    print(state)

def parse(s):
    if iframecheck(s)=="None":
        return "None"
    else:
        link=iframecheck(s)
        rest,embed=link.split("embed/")
        link="https://youtu.be/"+embed
        return link

def iframecheck(s):
    if matches := re.search("^<iframe (.* )?src=\"(https?://(www.)?youtube\.com/embed/[a-zA-Z0-9]+)\"( .*s)?></iframe>$", s):
        return(matches.group(2))
    else:
        return"None"



#def linkcheck(s):
    #if matches := re.search("^https?://(www.)?youtube.com/embed/[a-zA-Z0-9]+$", s):
        #print ("TRUE")
        #print(matches.group(0))
    #else:
        #print ("Error")
        #print(s)

if __name__=="__main__":
    main()
