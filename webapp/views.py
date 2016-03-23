# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def add_info(request):
    # if request.method == 'POST':
    #
    #   form = ItemForm(request.POST)
    #
    # if form.is_valid():
    #
    #   cd = form.cleaned_data
    #
    #   item = Item()
    #
    #   item.ItemCode = cd['ItemCode']
    #
    #   item.ItemName = cd['ItemName']
    #
    #   item.save()
    #
    #   return HttpResponseRedirect('/success/')
    #
    # else:
    #
    #   form = ItemForm( )

    # return render_to_response('ItemAdd.html', {'form': form},
    #
    #         context_instance = RequestContext(request))
    return render_to_response('info_form.html', context_instance=RequestContext(request))
