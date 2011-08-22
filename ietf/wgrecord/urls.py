# Copyright The IETF Trust 2011, All Rights Reserved

from django.conf.urls.defaults import patterns, url
from ietf.wgrecord import views_rec, views_search, views_edit, views_ballot, views_submit
from redesign.name.models import CharterDocStateName

urlpatterns = patterns('django.views.generic.simple',
    url(r'^help/state/$', 'direct_to_template', { 'template': 'wgrecord/states.html', 'extra_context': { 'states': CharterDocStateName.objects.all() } }, name='help_charter_states'),
)
urlpatterns += patterns('',
    (r'^/?$', views_search.search_main),
    url(r'^create/$', views_edit.edit_info, name="wg_create"),
    (r'^search/$', views_search.search_results),
    (r'^searchPerson/$', views_search.search_person),
    url(r'^ad/(?P<name>[A-Za-z0-9.-]+)/$', views_search.by_ad, name="wg_search_by_ad"),
    url(r'^in_process/$', views_search.in_process, name="wg_search_in_process"),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/((?P<rev>[0-9][0-9](-[0-9][0-9])?)/)?((?P<tab>ballot|writeup|history)/)?$', views_rec.wg_main, name="wg_view_record"),
    (r'^(?P<name>[A-Za-z0-9._-]+)/_ballot.data$', views_rec.wg_ballot),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/state/$', views_edit.change_state, name='wg_change_state'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/info/$', views_edit.edit_info, name='wg_edit_info'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/conclude/$', views_edit.conclude, name='wg_conclude'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/addcomment/$', views_edit.add_comment, name='wg_add_comment'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/(?P<ann>action|review)/$', views_ballot.announcement_text, name='wg_announcement_text'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/position/$', views_ballot.edit_position, name='wg_edit_position'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/sendballotcomment/$', views_ballot.send_ballot_comment, name='wg_send_ballot_comment'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/edit/approveballot/$', views_ballot.approve_ballot, name='wg_approve_ballot'),
    url(r'^(?P<name>[A-Za-z0-9._-]+)/submit/$', views_submit.submit, name='wg_submit'),

)
