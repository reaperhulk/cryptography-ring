# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import glob
import os

import cffi


ffi = cffi.FFI()
ffi.cdef("""
typedef ... RingDigestContext;
typedef ... RingDigestAlgorithm;

RingDigestAlgorithm *ring_digest_algorithm_sha1(void);
RingDigestAlgorithm *ring_digest_algorithm_sha256(void);
RingDigestAlgorithm *ring_digest_algorithm_sha384(void);
RingDigestAlgorithm *ring_digest_algorithm_sha512(void);
RingDigestContext *ring_digest_context_new(RingDigestAlgorithm *);
RingDigestContext *ring_digest_context_clone(RingDigestContext *);
void ring_digest_context_update(RingDigestContext *, char *, unsigned int);
unsigned int ring_digest_context_finish(RingDigestContext *, char *,
                                        unsigned int);
void ring_digest_context_delete(RingDigestContext *);
""")
current_dir = os.path.abspath(os.path.dirname(__file__))
lib_path = glob.glob(os.path.join(current_dir, "ringffi.so"))
lib = ffi.dlopen(lib_path[0])


class Binding(object):
    """
    RingFFI API wrapper.
    """
    lib = lib
    ffi = ffi
