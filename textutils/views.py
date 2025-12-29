from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    return render(requests,'index.html',)

def about(requests):
    return render(requests,'about.html',)

def contact(requests):
    return render(requests,'contact.html')

def analyze(requests):
    # get the text
    global params
    text = requests.POST.get('text', 'default')

    # check checkbox values
    removepunc = requests.POST.get('removepunc','off')
    fullcaps = requests.POST.get('fullcaps','off')
    newlineremove = requests.POST.get('newlineremove','off')
    extraspaceremove = requests.POST.get('extraspaceremove','off')
    charcount = requests.POST.get('charcount','off')
    # print(removepunc)
    # print(text)
    # check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =  ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text':analyzed}
        text = analyzed
        # return render(requests, 'analyze.html',params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        text = analyzed
        # return render(requests, 'analyze.html', params)
    if (newlineremove == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        text = analyzed
        # return render(requests, 'analyze.html', params)
    if (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        text = analyzed
        # return render(requests, 'analyze.html', params)
    if (charcount == "on"):
        analyzed = 0
        for char in text:
            if char.isalpha():
                 analyzed += 1
            params = {'purpose': 'Total Number of Character in textarea', 'analyzed_text': analyzed}
            text = analyzed
    if (removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on"):
        return HttpResponse("error")
    return render(requests, 'analyze.html', params)
# old code
# if (charcount == "on"):
#     #     analyzed = 0
#     #     for char in text:
#     #         if char.isalpha():
#     #             analyzed += 1
#     #     params = {'purpose': 'Total Number of Character in textarea', 'analyzed_text': analyzed}
#         # text = analyzed
#         # return render(requests, 'analyze.html', params)
# def index(requests):
#     return render(requests,'index.html',)
#     nav = '''<a href="removepunc">Remove Punctuation</a>
#             <a href="capitalizefirst">Capitalize first</a>
#             <a href="newlineremove">New Line Remove</a>
#             <a href="spaceremove">Space Remove Punctuatio</a>
#             <a href="charcount">Character Count</a>'''
#     return HttpResponse(nav)

# def removepunc(requests):
#     print(requests.GET.get('text', 'default'))
#     return HttpResponse('''Remove punc <a href="/">Back to home page</a>''')
#
# def capfirst(requests):
#     return HttpResponse('''Capitalize first <a href="/">Back to home page</a>''')
#
# def newlineremove(requests):
#     return HttpResponse('''new line remove <a href="/">Back to home page</a>''')
#
# def spaceremove(requests):
#     return HttpResponse('''space remove <a href="/">Back to home page</a>''')
#
# def charcount(requests):
#     return HttpResponse('''char count <a href="/">Back to home page</a>''')
#
# def about(requests):
#     return HttpResponse("About")