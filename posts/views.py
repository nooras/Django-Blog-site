from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post
from .forms import PostForm

from django.core.paginator import Paginator
from django.shortcuts import render

from django.db.models import Q #For search - Q lookup

# from myapp.models import Contact

# Create your views here.
# request.build_absolute_uri
def post_list(request):
    queryset_list = Post.objects.all() #.order_by("-timestamp")

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__username__icontains=query) 
            ).distinct()

    paginator = Paginator(queryset_list, 9) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)

    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, "post_list.html", context)

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    print(form)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance.get_absolute_url())
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.success(request, "Not Successfully Created")
    context  ={
        "form": form
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    print(id)
    queryset = get_object_or_404(Post, id=id)
    print(queryset)
    
    if queryset != None:
        print("Query", queryset)
        context = {
                "object_list": queryset,
                "title": "list"
            }
    else:
        pass
    return render(request, "post_detail.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,  request.FILES or None, instance=instance)
    print(form)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Item Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    print("Query", instance)
    context = {
            "instance": instance,
            "title": instance.title,
            "form":form
        }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Item Updated")

    return redirect("posts:home")



# def listing(request):
#     contact_list = Contact.objects.all()
    
#     return render(request, 'list.html', {'page_obj': page_obj})
