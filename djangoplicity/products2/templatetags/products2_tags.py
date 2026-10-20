# -*- coding: utf-8 -*-
#
# djangoplicity-products
# Copyright (c) 2007-2011, European Southern Observatory (ESO)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
#   * Neither the name of the European Southern Observatory nor the names
#     of its contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY ESO ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL ESO BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE
#

from django import template
from django.urls import NoReverseMatch, reverse

from djangoplicity.products2.base.models import ArchiveCategory
from djangoplicity.products2.queries import ArchiveCategoryQuery

register = template.Library()


def _has_category_query( options ):
    queries = getattr( options, 'Queries', None )
    return isinstance( getattr( queries, 'category', None ), ArchiveCategoryQuery )


def _public_categories( model, options, request ):
    """
    Categories with at least one public item in the archive, based on the
    default query (published, released and not embargoed).
    """
    ( qs, _args ) = options.Queries.default.queryset( model, options, request, only_source=True )
    category_ids = qs.order_by().filter( archive_category__isnull=False ).values( 'archive_category' )
    return ArchiveCategory.objects.filter( pk__in=category_ids ).order_by( 'fullname' )


def _query_url( name, viewmode, args=None ):
    """
    Reverse a query URL, keeping the current view mode (e.g. viewall)
    """
    args = list( args or [] )
    if viewmode:
        return reverse( '%s_viewmode' % name, args=args + [viewmode] )
    return reverse( name, args=args )


@register.inclusion_tag( 'archives/archive_categories.html', takes_context=True )
def product_archive_categories( context ):
    """
    Renders the ArchiveCategory filter of a product archive list view.

    The archive model and options are taken from the URL kwargs, which are
    set when the product URLs are included, e.g. in urls.py:

        url( r'^products/line-art/', include(...), { 'model': LineArt, 'options': LineArtOptions } )
    """
    request = context['request']
    url_kwargs = request.resolver_match.kwargs
    model = url_kwargs.get( 'model' )
    options = url_kwargs.get( 'options' )

    if not _has_category_query( options ):
        return {}

    prefix = options.urlname_prefix
    viewmode = url_kwargs.get( 'viewmode_name' )
    selected = url_kwargs.get( 'stringparam' ) if url_kwargs.get( 'query_name' ) == 'category' else None

    categories = []
    for category in _public_categories( model, options, request ):
        try:
            category.url = _query_url( '%s_query_category' % prefix, viewmode, [category.name] )
        except NoReverseMatch:
            # Category name is not URL safe
            continue
        category.selected = category.name == selected
        categories.append( category )

    if not categories:
        return {}

    return {
        'categories': categories,
        'all_url': _query_url( '%s_defaultquery' % prefix, viewmode ),
        'selected': selected,
        'params_nosearch': context.get( 'params_nosearch' ),
    }
