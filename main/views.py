from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View

from .forms import SearchForm, LeadForm
from .models import PortfolioItem, TechnologiesModel, TypeOfProjModel, LeadModel


def index(request):
    return HttpResponseRedirect('/home/')


class HomeView(View):
    def get(self, request):

        form = SearchForm(request.GET or None)

        portfolio_items = PortfolioItem.objects.all()
        portfolio_count = len(portfolio_items)
        tags_proj = TypeOfProjModel.objects.all()
        tech_stack = TechnologiesModel.objects.all()

        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            type_of_proj = form.cleaned_data.get('type_of_proj')
            tech_stack_filter = form.cleaned_data.get('tech_stack')

            filters = {}

            if search_query:
                filters['title__icontains'] = search_query
            if type_of_proj:
                filters['tag'] = type_of_proj
            if tech_stack_filter:
                filters['tech_stack'] = tech_stack_filter

            portfolio_items = portfolio_items.filter(**filters)

            html = render_to_string('home.html', {"portfolio": portfolio_items,
                                                  "first3_portfolio": portfolio_items[len(portfolio_items) - 3:] if len(
                                                      portfolio_items) > 3 else portfolio_items,
                                                  "completed_count": portfolio_count,
                                                  "tech_stack": tech_stack,
                                                  "types": tags_proj, 'form': form,
                                                  })
            return HttpResponse(html)

        return render(request, 'home.html',
                      context={"portfolio": portfolio_items,
                               "first3_portfolio": portfolio_items[len(portfolio_items) - 3:] if len(
                                   portfolio_items) > 3 else portfolio_items,
                               "completed_count": portfolio_count,
                               "tech_stack": tech_stack,
                               "types": tags_proj, 'form': form, 'lead_form': LeadForm()
                               }
                      )

    def post(self, request):
        form = LeadForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            company_name = form.cleaned_data.get('company_name', None)
            email = form.cleaned_data.get('email')
            description = form.cleaned_data.get('description')

            lead = LeadModel(name=name, email=email, company_name=company_name, description=description)
            lead.save()

        return HttpResponseRedirect('/home/')


class PortfolioItemView(View):
    def get(self, request, id_item):
        item = PortfolioItem.objects.get(id=id_item)
        return render(request, 'portfolio_view.html', context={'item': item})
