from django import forms
from django.forms.widgets import CheckboxSelectMultiple

import utils
import operator

class WeekdayFormField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
          kwargs['choices'] = utils.DAY_CHOICES
        kwargs.pop('max_length', None)
        if 'widget' not in kwargs:
          kwargs['widget'] = forms.widgets.SelectMultiple
        super(WeekdayFormField, self).__init__(*args, **kwargs)
        
    def clean(self, value):
      value = super(WeekdayFormField, self).clean(value)
      return value

class BitwiseWeekdayFormField(WeekdayFormField):
  def __init__(self, *args, **kwargs):
    if 'short' in kwargs:
      if kwargs['short']:
        kwargs['choices'] = [(x[0],x[1]) for x in utils.BITWISE_DAY_CHOICES]
      del kwargs['short']
    else:
      kwargs['choices'] = [(x[0],x[2]) for x in utils.BITWISE_DAY_CHOICES]
    super(BitwiseWeekdayFormField, self).__init__(*args, **kwargs)

  def clean(self,value):
    value = [int(x) for x in value]
    if len(value) != 0:
      value = reduce(operator.or_, value)
    else:
      value = 0
    return value

class BitwiseWeekdayCheckbox(CheckboxSelectMultiple,BitwiseWeekdayFormField):
  def render(self, name, value, attrs=None, choices=()):
    if value is None: value = []
    has_id = attrs and 'id' in attrs
    final_attrs = self.build_attrs(attrs)

    output = []

    str_values = set([force_unicode(v) for v in value])
    for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
      if has_id:
          final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
          label_for = u' for="%s"' % final_attrs['id']
      else:
          label_for = ''

      cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
      option_value = force_unicode(option_value)
      rendered_cb = cb.render(name, option_value)
      option_label = conditional_escape(force_unicode(option_label))
      output.append(u'%s <label %s><div class="raw_checkbox">%s</div></label>' % (rendered_cb, label_for, option_label))
    return mark_safe(u'\n'.join(output))
