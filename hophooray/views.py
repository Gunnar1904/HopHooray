from django.views import View
from django.views.generic import TemplateView
from hophooray.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from hophooray.models import Beer
from django.db.models import Sum
from hophooray.forms import CreateForm


class HomeView(TemplateView):
    model = Beer
    template_name = 'hophooray/home.html'

    def get(self, request):
        beerlist = Beer.objects.all().aggregate(summary = Sum('amount'))['summary']
        context = {'beerlist':beerlist}
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'hophooray/about.html'

    def get(self, request):
        return render(request, self.template_name)


class InventoryListView(OwnerListView):
    model = Beer
    template_name = 'hophooray/inventory.html'

    def get(self, request):
        beerlist = Beer.objects.all()
        context = {'beerlist':beerlist}
        return render(request, self.template_name, context)


class InventoryDetailView(OwnerDetailView):
    model = Beer
    template_name = 'hophooray/inventory_detail.html'

    def get(self, request, pk):
        beerdetail = Beer.objects.filter(id=pk)
        context = {'beerdetail':beerdetail}
        return render(request, self.template_name, context)


class InventoryCreateView(LoginRequiredMixin, View):
    fields = ['name', 'origin', 'beertype', 'amount', 'price']
    template_name = 'hophooray/inventory_form.html'
    success_url = reverse_lazy('hophooray:inventory')

    def get(self, request, pk=None):
        form = CreateForm()
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            context = {'form':form}
            return render(request, self.template_name, context)

        x = form.save(commit=False)
        x.owner = self.request.user
        x.save()
        return redirect(self.success_url)


class InventoryUpdateView(LoginRequiredMixin, View):
    template_name = 'hophooray/inventory_form.html'
    success_url = reverse_lazy('hophooray:inventory')

    def get(self, request, pk):
        y = get_object_or_404(Beer, id=pk, owner=self.request.user)
        form = CreateForm(instance=y)
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        y = get_object_or_404(Beer, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=y)

        if not form.is_valid():
            context = {'form':form}
            return render(request, self.template_name, context)

        y = form.save(commit=False)
        y.save()
        return redirect(self.success_url)


class InventoryDeleteView(OwnerDeleteView):
    model = Beer
    template_name = 'hophooray/inventory_confirm_delete.html'
