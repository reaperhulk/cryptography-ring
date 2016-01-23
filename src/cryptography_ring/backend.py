# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

from cryptography import utils
from cryptography.hazmat.backends.interfaces import HashBackend


from cryptography_ring.binding import Binding
from cryptography_ring.hashes import _HashContext


@utils.register_interface(HashBackend)
class Backend(object):
    """
    Ring-ffi API wrapper.
    """
    name = "ring"

    def __init__(self):
        self._binding = Binding()
        self._ffi = self._binding.ffi
        self._lib = self._binding.lib

        self._hash_mapping = {
            "sha1": self._lib.ring_digest_algorithm_sha1,
            "sha256": self._lib.ring_digest_algorithm_sha256,
            "sha384": self._lib.ring_digest_algorithm_sha384,
            "sha512": self._lib.ring_digest_algorithm_sha512,
        }

    def hash_supported(self, algorithm):
        return algorithm.name in self._hash_mapping

    def create_hash_ctx(self, algorithm):
        return _HashContext(self, algorithm)


backend = Backend()
