from django.db import models

from forms import WeekdayFormField

def validate_csv(data):
    return all(map(lambda x:isinstance(x, int), data))
    
class WeekdayField(models.CommaSeparatedIntegerField):
    """
    Field to simplify the handling of a multiple choice of None->all days.
    
    Stores as CSInt.
    """
    __metaclass__ = models.SubfieldBase
    
    description = "CSV Weekday Field"
    default_validators = [validate_csv]
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super(WeekdayField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        return super(WeekdayField, self).formfield(form_class=WeekdayFormField, **kwargs)
    
    def get_db_prep_value(self, value, connection=None, prepared=False):
        return ",".join([str(x) for x in value])

    def to_python(self, value):
        if isinstance(value, basestring):
            if value:
                value = [int(x) for x in value.strip('[]').split(',') if x]
            else:
                value = []
        return value

        
def validate_bitwise_notation(data):
  return data > 0 and data <= (2**7 - 1)

class BitwiseWeekdayField(models.IntegerField):
  __metaclass__ = models.SubfieldBase
  
  description = "Bitwise Weekday Field"
  default_validators = [validate_bitwise_notation]

  def to_python(self, value):
    if isinstance(value, int):
      return BitwiseDays(value)
    return value

  def formfield(self, **kwargs):
    return super(BitwiseWeekdayField, self).formfield(form_class=BitwiseWeekdayFormField, **kwargs)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^weekday_field\.fields\.WeekdayField'])
    add_introspection_rules([], ['^weekday_field\.fields\.BitwiseWeekdayField'])
except ImportError:
    pass
