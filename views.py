# views.py
from django.shortcuts import render
from transformers import CLIPProcessor, CLIPModel
from django.shortcuts import render, redirect
from .forms import ImageUploadForm, QuestionForm  # Assuming you have a form for questions
from .ai_algorithm import ai_generate_answer  # Your AI logic

def home_view(request):
    return render(request, 'home.html')


# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")


def image_recognition_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file from the form
            image = form.cleaned_data['image']

            # You can process the image directly here
            # For example, pass the image to your AI algorithm
            question = "What is in this image?"
            answer = ai_generate_answer(image, question)

            return render(request, 'result.html', {
                'image': image,
                'question': question,
                'answer': answer
            })
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

def result_view(request):
    image_url = request.session.get('image')
    question_form = QuestionForm()

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.cleaned_data['question']
            answer = ai_generate_answer(image_url, question)  # Use the combined function
            return render(request, 'result.html', {
                'image_url': image_url,
                'question': question,
                'answer': answer,
                'question_form': question_form
            })

    return render(request, 'result.html', {
        'image_url': image_url,
        'question_form': question_form
    })
