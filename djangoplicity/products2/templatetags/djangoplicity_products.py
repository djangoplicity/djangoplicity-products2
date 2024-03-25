from django import template
from djangoplicity.products2.models import Index
from django.contrib.sites.shortcuts import get_current_site

register = template.Library()


@register.inclusion_tag('tags/index.html', takes_context=True)
def product_index(context):
    index = {}
    items = []
    try:
        sort_by = context.request.GET.get('sort', '')
        index = Index.objects.get(site=get_current_site(None))
        items = index.items.filter(disabled=False)
        if sort_by == 'release_date':
            items = sorted(items, key=lambda x: x.last_release, reverse=True)
        elif sort_by == 'priority':
            items = sorted(items, key=lambda x: x.priority, reverse=True)

    except Index.DoesNotExist:
        pass
    return {
        'request': context.request,
        'index': index,
        'items': items
    }
