import requests as rq
import json
import openai
openai.api_key ="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"
lis=[]
print("X*************************************************************************************************X")
print("X                         Welcome TO the ChATBot                                                  X")
def ai2(i,lis):
    var=""
    for i in lis:
        var=var+i+"\n"
    if i==0:
        conversation=input("talk about how you are feeling today : \n you :  ")
        var="person : " +var+conversation
    else :
        conversation=input("you : ")
        var=var+conversation
    sentiment=openai.Completion.create(
        model="text-davinci-003",
        prompt="continue the following conversation as a friend that tries to ask some questions and helps the person to make decisions,output only one sentence and dont output multiple lines: "+var ,
        temperature=1.5,
        max_tokens=3000
        )
    var=var+sentiment["choices"][0]["text"]
    print(sentiment["choices"][0]["text"])
    lis.append("person : " +conversation)
    lis.append("chat bot: "+ sentiment["choices"][0]["text"])
def ai(l):
    var=""
    for i in l:
        var=var+i+"\n"
    sentiment=openai.Completion.create(
        model="text-davinci-003",
        prompt=var+": read the conversation between the person and chat bot and only output a genre of music in a single word according to the person :" ,
        temperature=0.0,
        max_tokens=2000
    )
    return sentiment["choices"][0]["text"]
for i in range(20):
    ai2(i,lis)
    decision=input("do you wanna continue?y or n  :  ")
    if decision=='n':
        typ=ai(lis)
        headers={
        "Authorization":"Bearer BQCzBV-Dp68tJXlpZcGaSSvGqvB40Xz9eRpztOzMa3n_3Lxio5U9yiEB8jCDRWsBb_OljV0P91zbdYSg2EJsLByhiB_nJultNqPlXiyUQ_M-gheAIxBMXlZVCKjAIkyzFrg7OlNopGEw5vkrJRUOxbSNNhuzyQrhHv0OZ84FYZwbie9JcVkKG414pWIFKDyUy09XAniUe4F9fjNLt49DDXO-xvbGt699ib17WTWoqIptx0FntvfzEHTVoYGlFL0Q_JUb4Pa9-dh7MTFrPj9Oph9U13GFwCrpka7FR9oQpHlHC7K4Cv1pNmLFsGnEhNDo3hKyQQRWoJFJyw",
        "Accept":"application/json",
        "Content-Type": "application/json"
        }
        searcher=rq.get(f"https://api.spotify.com/v1/search?q={typ}&type=playlist&limit=1&country=US",headers=headers)
        namea=searcher.json()
        playlist_id=namea['playlists']['items'][0]['id']
        playlists=rq.get(f'https://api.spotify.com/v1/playlists/{playlist_id}?q=limit=2&country=US',headers=headers)
        link=playlists.json()
        print(link["external_urls"]["spotify"])
        break
