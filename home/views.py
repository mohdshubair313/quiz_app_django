from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
import random

# so Jitna bhi buisness logic hota hai na wo views me function ke roop me likh dete hai aur usko usi app ke urls me specific url se attach kar denge ke jo bhi uss url par jaye to ye wala buisness logic dikhe

def home(request):
    context = {'categories': Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'index.html', context)

def quiz(request):
    context = {'category' : request.GET.get('category') }  # Remove extra space
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()

        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        
        question_objs = list(question_objs)
        print(question_obj.get_answer())
        data = []
        random.shuffle(question_objs)

        # Loop to prepare the question data
        for question_obj in question_objs:
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                'answers': question_obj.get_answer()
            })
        
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)  # Log the error for debugging
        # Always return JSON even in case of an error
        payload = {'status': False, 'message': "Something Went Wrong"}
        return JsonResponse(payload, status=500)
