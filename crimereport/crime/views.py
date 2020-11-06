from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Congressperson
from .serializer import CongresspersonSerializer
from rest_framework import viewsets, mixins, generics
from django.views.generic import DetailView, ListView
import json

#CBV

# class CongressViewSet(viewsets.ModelViewSet):
#     queryset = Congressperson.objects.all()
#     serializer_class = CongresspersonSerializer


# class CongressDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Congressperson.objects.all()
#     serializer_class = CongresspersonSerializer
    
class CongressListView(ListView):
    model = Congressperson
    template_name = 'crime/index.html'
    context_object_name = "congresslist"  


    # def get_queryset(self, district):
    #     return Congressperson.objects.get(district=district) 

def search(request, district):
   info = Congressperson.objects.get(district=district)
   name = info.name
   city = info.district
   crimes = info.crimes
#    photo = info.photo
   elected_num = info.elected_num
   party = info.party
   context = {"name":name, "city":city, "crimes":crimes, "elected_num":elected_num,"party":party}
   context_json = json.dumps(context)
   return HttpResponse(context_json)


# class CongressDetailView(DetailView):
#     model = Congressperson
#     template_name = 'crime/index.html'
#     context_object_name = "congresslistdetail"  


# #     # def get_queryset(self,district):
# #     #     return Congressperson.objects.get(district=district) 
# #     # def get_queryset(self, district, *args, **kwargs):
# #     #     return Congressperson.objects.get(district=district)

#     def get_context_data(self, **kwargs):
#         context = super(CongressDetailView, self).get_context_data(**kwargs)
#         context['all_objects'] = context.objects.all()

#         return context

# class CongressDetailView(DetailView):
#     model = Congressperson

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # self.kwargs['pk']를 통해서 url에서 pk값을 받을 수 있습니다.
#         # url은 `path('<pk>/', PhotoView.as_view())으로 구현되어있어서 해당 pk 부분을 받아옵니다.`
#         context['district'] = Congressperson.objects.filter(district=self.kwargs['district'])
#         return context
