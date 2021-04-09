# from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator,EmptyPage , PageNotAnInteger
from .models import Image,Classification
from skimage.transform import resize
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.db.models import F
import tensorflow as tf
import numpy as np
import skimage
import keras
import cv2

classifications = ['aeroplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

#LOADING MODEL
new_model = tf.keras.models.load_model('my_model_CIFAR1.h5')
# print(new_model.get_weights())

def home(request):
    
    if request.method=="POST":
        img = request.FILES.get('image')
        label = request.POST.get('inlabel')
      
        a = Image(image = img)
        a.save()

        # reading and resizing image 
        img1 = cv2.imread('C:/Users/Hp/Desktop/django projects/Photos/media/images/'+str(img))

        img1 = img1/255
        print(img1.shape)
        resized_image = resize(img1 , (32,32,3))
        print('resized image ',resized_image.shape)
        # resizing is done
        
        # call classify image function and send the image as input
        pred = classify_image(resized_image)
        
        classification_object = Classification(image=img,label=label, classification_category=pred[0],probability = pred[1])
        
        classification_object.save()
        
    allImages = Image.objects.all()
    return render(request,'home.html',{'allImages':allImages})

def classify_image(image):

    predictions = new_model.predict(np.array([image]))
    print('predicitons are:',predictions)

    pred = np.argmax(predictions)
    return((classifications[pred].upper(),round(100*np.max(predictions))))


def images(request):

    if request.method == 'POST':
        query = request.POST.get('search')
        allPredsClass = Classification.objects.filter(classification_category__icontains = query)
        allPredsLabel = Classification.objects.filter(label__icontains = query)
        allPreds = allPredsClass.union(allPredsLabel)
        total = len(allPreds)
        pos = 0
        neg = 0
        for i in allPreds:
            if i.classification_category == i.label:
                pos+=1
            else:
                neg+=1
        context={'total':total,'pos':pos,'neg':neg,'pagn':False}
    else:
        allPreds = Classification.objects.all().order_by('-id')
        total = len(allPreds)
        pos = len(Classification.objects.filter(classification_category__contains=F('label')))
        neg = total - pos
        context={'total':total,'pos':pos,'neg':neg,'pagn':True}
        
    paginator = Paginator(allPreds, 8)  
    page_num = request.GET.get('page',1)

    try:
        preds = paginator.page(page_num)
    except EmptyPage:
        preds = paginator.page(2)
    except PageNotAnInteger:
        preds = paginator.page(1)

    context['preds']=preds
    return render(request,'images.html',context)


