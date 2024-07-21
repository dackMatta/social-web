from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actions.utils import create_action

@login_required
def image_create(request):
    if request.method == 'POST':
        # Form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # Assign current user to the new image
            new_image.user = request.user
            new_image.save()
            create_action(request.user,'bookmarked image',new_image)
            # Success message and redirect to new image page
            messages.success(request, 'Image added successfully')
            return redirect(new_image.get_absolute_url())
    else:
        # Build the form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    # Ensure the form is rendered regardless of POST or GET
    pic = {'section': 'images', 'form': form}
    return render(request, 'images/image/create.html', pic)

@login_required
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                   'images/image/detail.html',
                     {'section': 'images', 'image': image})
    

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images=Image.objects.all()
    paginator=Paginator(images,8)
    page=request.GET.get('page')
    images_only=request.GET.get('images_only')
    try:
        images=paginator.page(page)
    except PageNotAnInteger:
        #if page is not an interger deliver the first page
        images=paginator.page(1)
    except EmptyPage:
        if images_only:
            #if AJAX request and page out of range
            #return an empty page
            return HttpResponse('')
        #if page out of range return last page of results
        image=paginator.page(paginator.num_pages)
    if images_only:
        tip={'section': 'images', 'image': images}
        return render(request,
                      'images/image/list_images.html',
                      tip)
    return render(request,
                  'images/image/list.html',
                  tip)