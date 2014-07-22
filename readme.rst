memory leak tests
=================
This tries a bunch of potential causes of a memory leak in gidden/cyclopts.

Test 1: xdress
--------------
This is not the cause.  To replicate run::

    $ xdress --debug
    $ ./setup.py build
    $ ./memtest.py

Play around with the ``N`` value in memtest and un/comment the gc.collect() call
inside of the loop.  If you are running h/top you'll see that the memory 
resources are cleaned up correctly.

