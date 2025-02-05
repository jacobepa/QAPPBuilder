from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from teams.models import Team


def contact(request):
  """Render the contact page."""
  assert isinstance(request, HttpRequest)
  return render(
    request,
    'main/contact.html',
    {
      'title': 'Contact',
      'year': datetime.now().year,
    }
  )


@login_required
@staff_member_required
def clean_qapps(request, *args, **kwargs):
  """
  Clean QAPP Data.

  - Remove extra new line characters and spaces.
  - Convert QA_Category to the proper value.
  """
  # sections_a = SectionA.objects.all()
  # for sect in sections_a:
  #   # Clean Section A
  #   a3_clean = sect.a3.replace('\r\n', ' ').replace('    ', ' ')
  #   a9_clean = sect.a9.replace('\r\n', ' ').replace('    ', ' ')
  #   a9_clean = a9_clean.replace('QA QA', 'QA')
  #   if 'B' in sect.qapp.qa_category:
  #       a9_clean = a9_clean.replace('QA Category A', sect.qapp.qa_category)
  #   else:
  #       a9_clean = a9_clean.replace('QA Category B', sect.qapp.qa_category)
  #   sect.a3 = a3_clean
  #   sect.a9 = a9_clean
  #   sect.save()
  return render(request, 'web_dev.html', {})


@login_required
@staff_member_required
def web_dev_tools(request, *args, **kwargs):
  """
  Go to the web developer page with custom admin functionality.

  - Includes various custom admin functionality.
  - Includes button to remove extra new line characters/spaces from QAPP data
  """
  return render(request, 'web_dev.html', {})


class QappIndex(LoginRequiredMixin, TemplateView):
  """Class to return the first page of the Existing Data flow."""

  template_name = 'qapp_index.html'

  def get_context_data(self, **kwargs):
    """
    Override default method to send data to the template.

    Specifically, want to send a list of users and teams to select from.
    """
    context = super().get_context_data(**kwargs)
    context['users'] = User.objects.all()
    context['teams'] = Team.objects.all()
    return context
