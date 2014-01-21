DAY_CHOICES = (
  (0, "Monday"),
  (1, "Tuesday"),
  (2, "Wednesday"),
  (3, "Thursday"),
  (4, "Friday"),
  (5, "Saturday"),
  (6, "Sunday")
)

import string

class BitwiseDays:
  CHOICES = (
    (1, "Su","Sunday"),
    (2, "M","Monday"),
    (4, "Tu","Tuesday"),
    (8, "W","Wednesday"),
    (16, "Th","Thursday"),
    (32, "F","Friday"),
    (64, "Sa","Saturday"),
  )

  SUNDAY,MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY = [2**i for i in range(0,7)]
  WEEKDAYS = 2**6 - 2
  WEEKENDS = SUNDAY + SATURDAY

  def __init__(self,raw_value=0):
    if isinstance(raw_value,list):
      raw_value = sum(raw_value)
    self.raw_value = raw_value

  def __unicode__(self):
    raw_value = self.raw_value
    
    if self.raw_value == BitwiseDays.WEEKENDS:
      return "weekends"
    elif self.raw_value == BitwiseDays.WEEKDAYS:
      return "weekdays"
    elif self.raw_value == 0 or self.raw_value == 2**7 - 1 or self.raw_value == None:
      return "" 
    else:
      days = []
      for raw_value,short_name,long_name in BitwiseDays.CHOICES:
        if raw_value & self.raw_value:
          days.append(short_name)

      return string.join(days,",")

  @property
  def values_list(self):
    days = []
    for raw_value,short_name,long_name in BitwiseDays.CHOICES:
      if raw_value & self.raw_value:
        days.append(raw_value)

    return days

  def included(self,raw_value):
    return self.raw_value & raw_value

  def iso_included(self,iso_value):
    return self.raw_value & 2**(iso_value % 7)

BITWISE_DAY_CHOICES = BitwiseDays.CHOICES
