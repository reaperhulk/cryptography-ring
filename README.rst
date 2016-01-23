Cryptography-ring
=================

**At this time this should be considered experimental software and not ready for
any sort of production use.**

This is the first external backend for `cryptography`_. It uses `ring-ffi`_.

Usage
-----

To use this backend you'll need to invoke Python with a ``RINGFFI_PATH``
environment variable. This should be the absolute path to the ringffi shared
object. Then you can import the backend and use it:

.. code-block:: pycon

    >>> from cryptography_ring.backend import backend


Issues
------

* Right now only ``HashBackend`` is supported.
* When adding the ``ring`` entry point for multibackend it is injected as the
  first element in the array. This is probably not desirable.
* Use of bare asserts.

.. _`cryptography`: https://cryptography.io/
.. _`ring-ffi`: https://github.com/briansmith/ring-ffi
