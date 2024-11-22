import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://reconocimientoemociones-362f8-default-rtdb.firebaseio.com/"
})


#Esto era para cargar los datos iniciales (no darle bola)
'''
ref = db.reference('Emociones')

data = {

    "angry":{
        "times": 0 
    },
    "disgust":{
        "times": 0 
    },
    "fear":{
        "times": 0 
    },
    "happy":{
        "times": 0 
    },
    "sad":{
        "times": 0 
    },
    "surprise":{
        "times": 0 
    },
    "neutral":{
        "times": 0 
    }
}

for key, value in data.items():
    ref.child(key).set(value)
'''

#Metodos de obtencion y carga de datos
def getData():
    angry= db.reference(f'Emociones/angry').get()   
    disgust= db.reference(f'Emociones/disgust').get()
    fear= db.reference(f'Emociones/fear').get()
    happy= db.reference(f'Emociones/happy').get()
    neutral= db.reference(f'Emociones/neutral').get()
    sad= db.reference(f'Emociones/sad').get()
    surprise= db.reference(f'Emociones/surprise').get()
    print(f"angry = {angry['times']}")

def updateData(emotion):
    emotionInfo= db.reference(f'Emociones/{emotion}').get()
    ref=db.reference(f'Emociones/{emotion}')
    emotionInfo['times']+=1
    ref.child('times').set(emotionInfo['times'])

