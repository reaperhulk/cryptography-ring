Cryptography-ring
=================

.. image:: https://travis-ci.org/reaperhulk/cryptography-ring.svg?branch=master
    :target: https://travis-ci.org/reaperhulk/cryptography-ring


**At this time this should be considered experimental software and not ready for
any sort of production use.**

This is the first external backend for `cryptography`_. It uses `ring-ffi`_.

Usage
-----

To use this backend you'll need rust 1.6 (and cargo) in your PATH so
setuptools can build ring and copy the shared object to the right location.

.. code-block:: pycon

    >>> from cryptography_ring.backend import backend


Issues
------

* Right now only ``HashBackend`` is supported.
* When adding the ``ring`` entry point for multibackend it is injected as the
  first element in the array. This is probably not desirable.
* Use of bare asserts.
* setup.py develop does not work due to the `rust_ext` setuptools patching.
* Only tested on OS X at the moment. It will probably work on Linux as well.

.. _`cryptography`: https://cryptography.io/
.. _`ring-ffi`: https://github.com/briansmith/ring-ffi
