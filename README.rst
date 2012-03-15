===================
django-nosql-admin
===================

Most NoSQL databases translate into Python as a list of dictionaries, right? So why do us developers try to staple document databases into Django's traditional style relational introspection and tools? It's like we're trying to add object impedance mismatch to something that avoids it in the first place.

Taking lessons learned from django-mongonaut, django-nosql-admin is an introspection tool for NoSQL databases. Our original test case is MongoDB, but if this works we'll invite authorship of interfaces for other NoSQL databases.

Fundamentals
============

* Display the results of lists of dictionaries
* mongoadmin.py features:

    * Define a collection
    * Only show ObjectId by default
    * Can add search fields which attempt to search
    * Can add list fields which try to display