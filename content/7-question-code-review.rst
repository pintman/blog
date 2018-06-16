7 Question Code Review
######################
:date: 2008-03-01 16:12
:author: admin
:tags: Informatik, Programmierung, Wissenschaft
:slug: 7-question-code-review
:status: published

`The Seven Question Code
Review <http://www.nofluffjuststuff.com/blog_detail.jsp?rssItemId=117187&utm_source=blogitem&utm_medium=rss&utm_campaign=blogrss>`__
beinhaltet eine Übersicht aus sieben Fragen, die man sich als
Java-Entwickler über seinen Code stellen sollte.

    The 7 question Java Code Review

    #. Are your equals() and hashcode() methods implemented correctly?
       (and there is a precise definition of correct...)
    #. Do you have a build process independent of an IDE?
    #. Do your methods that return collections wrap them as
       unmodifiable?
    #. Are any exceptions either caught, logged, and handled
       appropriately or passed up the calling stack?
    #. Do you know all of the third party libraries your project depends
       upon, and their version numbers?
    #. Do you have unit tests that adequately exercise your code?
    #. Do any of your packages have circular dependencies?
