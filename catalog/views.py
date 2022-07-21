from django.db.models import Q
from django.shortcuts import render
from catalog.models import Product, Composition, Usage, Feature
from main.context import context
from django.core.paginator import Paginator

context["usages"] = Usage.objects.all()
context["compositions"] = Composition.objects.all()
context["features"] = Feature.objects.all()

def catalog(request):
    
    product_list = Product.objects.filter(is_active=True)

    if request.method == "GET":

        selected_usages = []
        for usage in context["usages"]: 
            if usage.name in request.GET:
                selected_usages.append(usage.name)
        if selected_usages:
            product_list = product_list.filter(
                usages__name__in= tuple(selected_usages))
            
        selected_compositions = []
        for composition in context["compositions"]:
            if composition.name in request.GET:
                selected_compositions.append(composition.name)
        if selected_compositions:
            product_list = product_list.filter(
                compositions__name__in= tuple(selected_compositions))

        selected_features =[]
        for feature in context["features"]:
            if feature.name in request.GET:
                selected_features.append(feature.name)
        if selected_features:
            product_list = product_list.filter(
                features__name__in= tuple(selected_features))

        ########## Filtering of Width ##########
        gte300 = request.GET.get("gte300")
        gte280 = request.GET.get("gte280")
        lt160 =  request.GET.get("lt160")
        
        if gte300 == "on" and lt160 == "on":
            print("girdytutyi")
            product_list = product_list.filter(Q(width__range=(100,160)) |
            Q(width__range=(301,400)))
        elif gte280 == "on" and lt160 == "on":
            product_list = product_list.filter(Q(width__range=(100,160)) |
            Q(width__range=(280,400)))
        elif gte300 == "on" and gte280 == "on":
            print("ikiliii")
            product_list = product_list.filter(width__gte=280)
        elif gte300 == "on":
            product_list = product_list.filter(width__gte=300)
        elif gte280 == "on":
            product_list = product_list.filter(width__gte=280)
        elif lt160 == "on":
            product_list = product_list.filter(width__lt=160)

        ############ Sorting Queryset via Dropdown ##############
        sort = request.GET.get("sort")

        if sort == "productName":
            product_list = product_list.order_by("name")
        elif sort == "-productName":
            product_list = product_list.order_by("-name")
        elif sort == "width":
            product_list = product_list.order_by("width")
        elif sort == "newest":
            product_list = product_list.order_by("create_date")

    ################## SEARCH BAR QUERY ########################
    ############################################################
    query = request.GET.get("search")
    if query:
        product_list = product_list.filter(name__icontains=query)
    ############################################################

    ###################### PAGINATION ##########################
    ############################################################
    count = product_list.distinct().count()
    paginator = Paginator(product_list.distinct(), 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    nums = page_obj.paginator.num_pages 
    
    page_indexs = []
    if  nums != 1:
        if page_obj.number != nums:
            if page_obj.number != 1:
                page_indexs.append(str(page_obj.number-1))
            page_indexs.append(str(page_obj.number))

            if page_obj.number + 1 <= nums:
                page_indexs.append(str(page_obj.number+1))
            if page_obj.number == 1 and nums >= page_obj.number+2:
                page_indexs.append(str(page_obj.number+2))
        else:
            if page_obj.number != 2 and page_obj.number != 1:
                page_indexs.append(str(page_obj.number-2))
                if page_obj.number != 1:
                    page_indexs.append(str(page_obj.number-1))
            page_indexs.append(str(page_obj.number))

    else:
        page_indexs.append(str(page_obj.number))
        if page_obj.number + 1 <= nums:
            page_indexs.append(str(page_obj.number+1))

    page_str = [str(page_obj.number)]
    ############################################################

    context["parameter"] = request.GET
    context["page_indexs"] = page_indexs
    context["page_obj"] = page_obj
    context["current_list"] = page_str
    context["count"] = count

    return render(request,"catalog/catalog.html",context)


def product_details(request, slug):
    context["product"] = Product.objects.get(slug=slug)

    return render (request, "catalog/product_details.html", context)

# def products_by_category(request,slug):

#     context["products"] = Category.objects.get(slug=slug).product_set.filter(is_active=True)
#     context["selected_category"] = slug
    
    
#     return render(request, "catalog/catalog.html",context)
    
