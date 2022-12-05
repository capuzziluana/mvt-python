from django.shortcuts import render 
from appmtv.modelos import Familiar
import datetime

class Familiar_view:
    def autogenerar_listar_familiares(request):
        fm1= Familiar.create('luana',19, datetime.date(2003,5,17))
        fm2= Familiar.create('leandro',19, datetime.date(2003,5,17))
        fm3= Familiar.create('lucas',20, datetime.date(2002,11,17))

        fm1.save()
        fm2.save()
        fm3.save()


        return render(request,'autogenerarlistafamiliares.html', {'familiares': [fm1,fm2,fm3]})