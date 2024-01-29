from rest_framework import generics
from .models import Region
from .serializers import RegionSerializer
from django.shortcuts import render
from django.http import JsonResponse
import openai
import random
import os
class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetail(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


openai.api_key=os.environ['OPENAI_API_KEY']
def generate_single_mcq(topic):
    prompt = f"""
    Generate multiple-choice Questions quiz about {topic} musical instrument only for Saudia Arab for students. There should be only one correct answer from these options and 3 incorrect answers. The options should be in the following format:
    Option 1: which will always be the correct answer\n
    Option 2: which will always be the incorrect answer\n
    Option 3: which will always be the incorrect answer\n
    Option 4: which will always be the incorrect answer \n

    The correct answer will always be the A. Option 1. All the remaining options:  B. Option 2 , C. Option 3 and D. Option 4 will be incorrect choices.
    """
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        api_key=openai.api_key,
        temperature=0.9
    )

    mcq_with_options = response.choices[0].text.strip()
    return mcq_with_options

def generate_mcqs(request, topic):
    student_responses = []

    for _ in range(5):
        generated_mcq_with_options = generate_single_mcq(topic)

        mcq_with_options_lines = generated_mcq_with_options.split("\n")
        mcq = mcq_with_options_lines[0]
        options = mcq_with_options_lines[1:5]

        for i in range(0, len(options)):
            options[i] = options[i][3:]

        shuffled_options = random.sample(options, len(options))
        correct_option_idx = shuffled_options.index(options[0])
        correct_option = shuffled_options[correct_option_idx]

        response = {
            "mcq": mcq,
            "options": shuffled_options,
            "correct_option": correct_option
        }

        student_responses.append(response)

    return JsonResponse(student_responses, safe=False)