from django.http import HttpResponse, Http404
from django.shortcuts import render

# being init fb
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('./secret/fbkey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
# end init fb

def index(request):
    # doc_ref = db.collection(u'cl-dgy').document(u'3167048')
    docs = (doc.to_dict() for doc in db.collection(u'cl-dgy').get())
    posts = ({
        'id': int(p['id']),
        'status': p['status']['light'],
        'title': p['title'],
        'postDate': p['postDate'].replace('TOP:',''),
    } for p in docs)
    return render(request, 'MyGoodStuff/index.html', {'posts': posts})
    # return HttpResponse(u'Document data: {}'.format(msg))


def imagePostDetail(request, postId):
    fb_ref = db.collection(u'cl-dgy').document(str(postId))
    try:
        fb_data = fb_ref.get().to_dict()
        # print(u'Document data: {}'.format(doc.to_dict()))
    except:
        raise Http404("Blog does not exist")
    # template = loader.get_template('goods/post.html')
    # return HttpResponse(template.render({}, request))
    return render(request, 'MyGoodStuff/post.html', {'post': fb_data})