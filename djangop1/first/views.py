from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import nltk
from django.contrib import messages
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from random import shuffle
from .models import Codeinfo
# Create your views here.
username=''
def home(request):
    return render(request,'register.html')

msg1={}
def login(request):
    if request.method =='POST':
        global username
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
            return redirect(contact)
        else:
            messages.info(request,'invaild details')
            return redirect('login')  
    else:
       return render(request,'login.html')     
def logout(request):
    auth.logout(request)
    return render(request,'login.html')
def register(request):
    if request.method =='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
       
        user=User.objects.create_user(username=username,email=email,password=password);
        user.save();
        return render(request,'login.html')
    else:
       return render(request,'register.html') 
def contact(request):
    if request.method =='POST':
        codename=request.POST['codename']
        
        x = [[i] for i in range(10000)]
        shuffle(x)
        
        
        
 # to process standard python strings
        lemmer = nltk.stem.WordNetLemmatizer()
#Wo#rdNet is a semantically-oriented dictionary of English included in NLTK.
        f=open('content.txt','r',errors = 'ignore')
        raw=f.read()
        raw=raw.lower()# converts to lowercase
        nltk.download('punkt') # first-time use only
        nltk.download('wordnet') # first-time use only
        sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
        word_tokens = nltk.word_tokenize(raw)# converts to list of words

        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
        GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
        GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
        def greeting(sentence):
        
            for word in sentence.split():
                if word.lower() in GREETING_INPUTS:
                    return random.choice(GREETING_RESPONSES)

        def response(user_response):
            robo_response=''
            sent_tokens.append(user_response)
            TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
            tfidf = TfidfVec.fit_transform(sent_tokens)
            
            vals = cosine_similarity(tfidf[-1], tfidf)
        
            idx=vals.argsort()[0][-2]
        
            flat = vals.flatten()
        
            flat.sort()
            req_tfidf = flat[-2]
            if(req_tfidf==0):
                robo_response=robo_response+"I am sorry! I don't understand you"
                return robo_response
            else:
                robo_response = robo_response+sent_tokens[idx]
                return robo_response
        flag=True
        #print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
        if(flag==True):
            user_response = codename
            user_response=user_response.lower()
            if(user_response!='bye'):
                if(user_response=='thanks' or user_response=='thank you' ):
                    flag=False
                    msg1['msg']="ROBO: You are welcome.."
                else:
                    if(greeting(user_response)!=None):
                        msg1['msg']="ROBO: "+greeting(user_response)
                    else:
                        msg1['msg']=(response(user_response))
                        sent_tokens.remove(user_response)
            elif(user_response=='bye'):
                flag=False 
                msg1['msg']="ROBO: Bye! take care.."
            else:
                msg1['msg']=response(user_response)
        
        codeinfo1=Codeinfo(username=username,codename=codename,codedata=msg1['msg'])
        codeinfo1.username=username
        codeinfo1.codename=codename
        codeinfo1.codedata=msg1['msg']
        
        codeinfo1.save()

        codeinfo1=Codeinfo.objects.filter(username=username)
        information=''
        for data in codeinfo1:
            information+=data.codedata+'\n'+'---------------------'+'\n'

        return render(request,'contact.html',{'information':information})
    else:
        information=''
        codeinfo1=Codeinfo.objects.filter(username=username)
        for data in codeinfo1:
            information+=data.codedata+'\n'+'---------------------'+'\n'

        return render(request,'contact.html',{'information':information})