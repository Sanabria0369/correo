from rest_framework.decorators import api_view
from rest_framework.response import Response
from .model import model, data

@api_view(['POST'])
def clasificar(request):
 edad = int(request.data['edad'])
 ingresos = float(request.data['ingresos'])
 pred = model.predict([[edad, ingresos]])[0]
 prob = model.predict_proba([[edad, ingresos]])[0][pred]

 return Response({
  'resultado': 'Compra' if pred==1 else 'No compra',
  'confianza': round(prob*100,2),
  'datos': data.to_dict(orient='records'),
  'usuario': {'edad':edad,'ingresos':ingresos,'prediccion':pred}
 })
