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

from datetime import datetime, timedelta

from django.http import Http404
from django.template import Context, Template
from django.test import RequestFactory, TestCase
from django.urls import resolve, reverse

from djangoplicity.products2.base.models import ArchiveCategory
from djangoplicity.products2.models import LineArt, Logo
from djangoplicity.products2.options import LineArtOptions


class ArchiveCategoryTestCase( TestCase ):

    def setUp( self ):
        self.zodiac = ArchiveCategory.objects.create( name='zodiac', fullname='Zodiac' )
        self.north = ArchiveCategory.objects.create( name='north', fullname='Northern Sky' )
        self.unused = ArchiveCategory.objects.create( name='unused', fullname='Unused' )
        # Only used by another product archive
        self.logos = ArchiveCategory.objects.create( name='logos', fullname='Logos only' )

        self.aquarius = self._lineart( 'aquarius', self.zodiac )
        self.andromeda = self._lineart( 'andromeda', self.north )
        self.hidden = self._lineart( 'hidden', self.zodiac, published=False )
        self.future = self._lineart( 'future', self.zodiac, release_date=datetime.now() + timedelta( days=7 ) )
        self.nocategory = self._lineart( 'nocategory' )

        logo = Logo.objects.create( id='logo1', title='logo1', published=True )
        logo.archive_category.add( self.logos )

    def _lineart( self, id, category=None, published=True, release_date=None ):
        obj = LineArt.objects.create( id=id, title=id, published=published,
            release_date=release_date or datetime.now() - timedelta( days=1 ) )
        if category:
            obj.archive_category.add( category )
        return obj

    def _queryset( self, stringparam ):
        request = RequestFactory().get( '/' )
        query = LineArtOptions.Queries.category
        return query.queryset( LineArt, LineArtOptions, request, stringparam=stringparam )

    def _render_tag( self, path ):
        request = RequestFactory().get( path )
        request.resolver_match = resolve( path )
        template = Template( '{% load products2_tags %}{% product_archive_categories %}' )
        return template.render( Context( { 'request': request } ) )


class ArchiveCategoryQueryTestCase( ArchiveCategoryTestCase ):

    def test_only_public_items_in_category( self ):
        ( qs, data ) = self._queryset( 'zodiac' )

        self.assertEqual( [ self.aquarius ], list( qs ) )
        self.assertEqual( self.zodiac, data['category'] )

    def test_unknown_category( self ):
        with self.assertRaises( Http404 ):
            self._queryset( 'missing' )

    def test_missing_category( self ):
        with self.assertRaises( Http404 ):
            self._queryset( None )

    def test_title_includes_category( self ):
        query = LineArtOptions.Queries.category
        self.assertEqual( 'Line Art: Zodiac', query.verbose_name( category=self.zodiac ) )

    def test_url( self ):
        self.assertEqual( '/public/products/line-art/archive/category/zodiac/',
            reverse( 'lineart_query_category', args=[ 'zodiac' ] ) )


class ProductArchiveCategoriesTagTestCase( ArchiveCategoryTestCase ):

    def test_lists_only_categories_with_public_items( self ):
        html = self._render_tag( reverse( 'lineart_defaultquery' ) )

        self.assertIn( 'Zodiac', html )
        self.assertIn( 'Northern Sky', html )
        self.assertNotIn( 'Unused', html )
        self.assertNotIn( 'Logos only', html )
        self.assertIn( 'href="%s" class="selected"' % reverse( 'lineart_defaultquery' ), html )

    def test_selected_category( self ):
        url = reverse( 'lineart_query_category', args=[ 'zodiac' ] )
        html = self._render_tag( url )

        self.assertIn( 'href="%s" class="selected">Zodiac' % url, html )
        self.assertNotIn( 'href="%s" class="selected"' % reverse( 'lineart_defaultquery' ), html )

    def test_keeps_viewmode( self ):
        html = self._render_tag( reverse( 'lineart_defaultquery_viewmode', args=[ 'viewall' ] ) )

        self.assertIn( reverse( 'lineart_query_category_viewmode', args=[ 'zodiac', 'viewall' ] ), html )

    def test_empty_without_categories( self ):
        ArchiveCategory.objects.all().delete()

        self.assertEqual( '', self._render_tag( reverse( 'lineart_defaultquery' ) ).strip() )
