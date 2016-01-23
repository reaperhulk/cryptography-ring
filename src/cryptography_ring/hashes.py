# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

from cryptography import utils
from cryptography.exceptions import UnsupportedAlgorithm, _Reasons
from cryptography.hazmat.primitives import hashes


@utils.register_interface(hashes.HashContext)
class _HashContext(object):
    def __init__(self, backend, algorithm, ctx=None):
        self._algorithm = algorithm
        self._backend = backend

        if ctx is None:
            try:
                ctx = self._backend._lib.ring_digest_context_new(
                    self._backend._hash_mapping[self.algorithm.name]()
                )
            except KeyError:
                raise UnsupportedAlgorithm(
                    "{0} is not a supported hash on this backend.".format(
                        algorithm.name),
                    _Reasons.UNSUPPORTED_HASH
                )

        self._ctx = ctx

    algorithm = utils.read_only_property("_algorithm")

    def copy(self):
        new_ctx = self._backend._lib.ring_digest_context_clone(self._ctx)
        assert new_ctx != self._backend._ffi.NULL

        return _HashContext(self._backend, self.algorithm, ctx=new_ctx)

    def update(self, data):
        self._backend._lib.ring_digest_context_update(
            self._ctx, data, len(data)
        )

    def finalize(self):
        buf = self._backend._ffi.new("char[]", self.algorithm.digest_size)
        res = self._backend._lib.ring_digest_context_finish(
            self._ctx, buf, self.algorithm.digest_size
        )
        assert res == self.algorithm.digest_size
        return self._backend._ffi.buffer(buf)[:]
