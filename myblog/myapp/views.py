from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import ListView, TemplateView
from .models import BlogPost, PersonalInfo, MyExpertise, Skills, Languages, Expertise, Education


# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    context_object_name = 'context'
    queryset = {
        'posts': BlogPost.objects.all().order_by('-created_at')[:5],
        'person_info': PersonalInfo.objects.order_by('-created_at')[:1],
        'my_expertise': MyExpertise.objects.all(),
        'skills': Skills.objects.all(),
        'languages': Languages.objects.all(),
        'expertises': Expertise.objects.all(),
        'education': Education.objects.all(),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.queryset)
        return context


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm
        context = {
            "form": form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>biz bilan boglanganiz uchun tashakkur</h2>")
        context = {
            "form": form
        }
        return render(request, 'contact.html', context)

