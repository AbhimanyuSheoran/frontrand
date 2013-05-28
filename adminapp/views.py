from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import pdb
from django.core.urlresolvers import reverse
from datetime import datetime
from adminapp.models import BasicStat,Pictures,ImageWithThumbnail
from adminapp.forms import UploadImageForm,UploadFaceForm


def index(request):
    if request.GET:
        abc=BasicStat.objects
        if abc.values():
            base = BasicStat.objects.get(id=1)
            keys=request.GET.keys()
            for key in keys:
                if str(key)=='lenders':
                    base.lenders=request.GET[key]
                elif str(key)=='raised':
                    base.raised=request.GET[key]
                elif str(key)=='livesch':
                    base.livesch=request.GET[key]
                elif str(key)=='repay':
                    base.repay=request.GET[key]
            base.save()
            return HttpResponse('success')    
        

def admin(request):
    
    ini=BasicStat.objects
    inis=ini.values()
    ini=inis.get(id=1)
    documents = Pictures.objects.all()
    faces = ImageWithThumbnail.objects.all()
    form=UploadFaceForm()
    return render_to_response(
                              'main.html',
                              {'form':form,'documents': documents, 'stat':ini,'faces':faces},
                              context_instance=RequestContext(request)
                                )
def picture_upload(request):
    if  request.FILES:
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploadedImage = form['image']
            caption = form['caption']
            newdoc = Pictures(image = request.FILES['image'],caption=request.POST['caption'])
            newdoc.save()
            return HttpResponseRedirect('/admin/')
        else:
            newdoc = Pictures(image = request.FILES['image'],caption="No Caption For this image")
            newdoc.save()
            return HttpResponseRedirect('/admin/')
    newdoc=Pictures.objects.all()
    form = UploadImageForm()

    return render_to_response('picture_upload.html',{'form':form,'last_picture':newdoc},context_instance=RequestContext(request))

def delete_picture(request):
    if request.GET:
        pic=request.GET['pid']
        documents = Pictures.objects.get(id=pic)
        documents.delete()
    return HttpResponseRedirect('/admin/')


def faces(request):
    if  request.FILES:
        form = UploadFaceForm(request.POST, request.FILES)
        if form.is_valid():
            uploadedImage = form['image']
            name = form['name']
            detail = form['detail']
            testimonial = form['testimonial']
            newdoc = ImageWithThumbnail(image = request.FILES['image'],
                                        name=request.POST['name'],
                                        detail=request.POST['detail'],
                                        testimonial=request.POST['testimonial'])
            newdoc.save()
    return HttpResponseRedirect('/admin/')

def delete_face(request):
    if request.GET:
        fid=request.GET['fid']
        documents = ImageWithThumbnail.objects.get(id=fid)
        documents.delete()
    return HttpResponseRedirect('/admin/')

def edit_face(request):
    if request.GET:
        fid=request.GET['fid']
        documents = ImageWithThumbnail.objects.get(id=fid)
        if request.POST['name']:
            documents.name = request.POST['name']
        if request.POST['detail']:
            documents.detail = request.POST['detail']
        if request.POST['testimonial']:
            documents.testimonial = request.POST['testimonial']
        if request.FILES:
            documents.image = request.FILES['image']
         
        documents.save()
    return HttpResponseRedirect('/admin/')

def error403(request):
    return render_to_response('error403.html')

def error404(request):
    return render_to_response('error404.html')