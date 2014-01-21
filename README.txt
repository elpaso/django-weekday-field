=====================
django-weekday-field
=====================

A field that encapsulates the handling of selection of 0 or more weekday choices.

Uses Django's CommaSeparatedIntegerField internally.

Usage:

    from django.db import models
    import weekday_field
    
    class MyModel(models.Model):
        weekdays = weekday_field.fields.WeekdayField()


There is also a BitwiseWeekdayFormField, contributed by Andrew Gall <housepage@gmail.com>, which stores the data in a single integer.