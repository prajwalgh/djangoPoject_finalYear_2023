from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import CRUDForm
from .models import CRUD

# from joblib import load
# model = load('./savedmodel/best_model.h5')

from tensorflow.keras.models import load_model
model = load_model('./savedmodel/modelv1.h5')

def CRUDV(request):
    if request.method == "POST":
        form = CRUDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = CRUDForm()
    img = CRUD.objects.all()
    return render(request, 'CRUD/index.html', {'img': img, 'form': form})


# def CRUDURL1(request):
#     img = CRUD.objects.all()
#     ans=[]
#     for i in img:
#         pre=model.predict(i.image.url)
#         print(pre)
#         ans.append(pre)
#     print(ans)
#     return render(request,'CRUD/index1.html')
from PIL import Image
import requests
from io import BytesIO
import numpy as np

def CRUDURL1(request):
    img_data = CRUD.objects.all()
    ans = {}
    ans1=[]
    classes = {
        4: ("nv", " melanocytic nevi"),
        6: ("mel", "melanoma"),
        2: ("bkl", "benign keratosis-like lesions"),
        1: ("bcc", " basal cell carcinoma"),
        5: ("vasc", " pyogenic granulomas and hemorrhage"),
        0: ("akiec", "Actinic keratoses and intraepithelial carcinomae"),
        3: ("df", "dermatofibroma"),
    }
    lesion_ID_dict = {
        'nv,melanocytic nevi ': 0,
        'mel, melanoma': 1,
        'bkl, benign keratosis-like lesions': 2,
        'bcc ,basal cell carcinoma': 3,
        'akiec ,Actinic keratoses and intraepithelial carcinomae': 4,
        'vasc ,  pyogenic granulomas and hemorrhage': 5,
        'df, dermatofibroma': 6
    }

    for data in img_data:
        img = Image.open(data.image)
        img = img.resize((28, 28))
        img_arr = np.array(img)
        img_arr = img_arr / 255.0
        img_arr = np.expand_dims(img_arr, axis=0)
        pre = model.predict(img_arr)

        max_prob = max(pre[0])

        class_ind =list(pre[0]).index(max_prob)
        class_name = list(lesion_ID_dict.keys())[list(lesion_ID_dict.values()).index(class_ind)]
        # class_name = classes[class_ind]
        print(pre)
        print(max_prob)
        print(class_ind)
        print(class_name)
        ans1.append(class_name)
        ans[data.firstname]=class_name
    print(ans)

    #Todo make it so that we save predicted val in database
    return render(request, 'CRUD/index1.html', {'img': img_data,'ans':ans,'ans1':ans1})



# check for indiviual value
#     count=0
#     for data in img_data:
#         x = data
#         count += 1
#         if count==2:
#             break
#
#     img = Image.open(x.image)
#     img = img.resize((28, 28))
#     img_arr = np.array(img)
#     img_arr = img_arr / 255.0
#     img_arr = np.expand_dims(img_arr, axis=0)
#     pre = model.predict(img_arr)
#
#     max_prob = max(pre[0])
#
#     class_ind =list(pre[0]).index(max_prob)
#     class_name = classes[class_ind]
#     print(x.firstname)
#     print(pre)
#     print(max_prob)
#     print(class_ind)
#     print(class_name)
#     ans.append(class_name)
#     print(ans)
#     return render(request, 'CRUD/index1.html', {'img': img_data,'ans':ans})
