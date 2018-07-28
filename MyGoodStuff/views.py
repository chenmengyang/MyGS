from django.http import HttpResponse

# being init fb
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('./secret/fbkey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
# end init fb

def index(request):
    doc_ref = db.collection(u'cl-dgy').document(u'3167048')
    msg = ''
    try:
        doc = doc_ref.get()
        msg = doc.to_dict()
        # print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        msg = 'error'
        # print(u'No such document!')

    return HttpResponse(u'Document data: {}'.format(msg))
