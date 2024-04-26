import requests
from django.shortcuts import render 

def index(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']


  response2 = requests.get('https://freetestapi.com/api/v1/students') # Use this API
  data2 = response2.json()
  name = data2[0]['name']

  return render(request, 'templates/index.html', {'fact': fact, 'dog': dog,  'name': name})


def home(request):
  return render(request, 'templates/home.html')
def about(request):
  return render(request, 'templates/about.html')
  
def dog(request):
  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']
  return render(request, 'templates/dog.html', {'dog': dog})
def fact(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text']
  return render(request, 'templates/fact.html', {'fact' : fact})
def student(request):
  response2 = requests.get('https://freetestapi.com/api/v1/students') # Use this API
  data2 = response2.json()
  name = data2[0]['name']
  return render(request, 'templates/student.html', {'name' : name})