Django Fast Generic Foreign Keys
================================

.. figure:: https://travis-ci.org/praekelt/django-fast-gfk.svg?branch=develop
   :align: center
   :alt: Travis

   Travis

Overview
--------------

Generic foreign keys are incredibly powerful but can't be prefetched, leading
to a large number of SQL queries when accessing a generic foreign key field
while iterating over a queryset. This app provides a function that reduces the
number of SQL queries to ``1 + (number of content types included in the set of
generic foreign keys)``.

Installation
------------

1. Install or add ``django-fast-gfk`` to your Python path.

Usage
-----

The ``fetch`` function returns a generator with the generic foreign key prefetched. Parameter
``field`` is the name of the generic foreign key.::

    from fast_gfk import fetch

    fetch(Bar.objects.all(), field="target"))

