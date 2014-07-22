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

Test 2: pytables row
--------------------
This test definitely mem leaks. This uses the table row object and the 
memory leak seems to be fairly fast.  Run this test with::

    $ ./pttest.py

Test 3: pytables append
------------------------
This test uses the table append() method rather than the row object. 
It also directly appends numpy arrays.  This may have a minor memory 
leak but it is much slower.  Run this test with::

    $ pttest-np.py

Conclusion
----------
The row attr should probably be avoided, not just because it is slow!

