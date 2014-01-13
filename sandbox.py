# Copyright 2014 Christopher Thompson <cthompson@cs.berkeley.edu>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import ctypes
from ctypes import c_uint64, c_char_p, byref
from ctypes.util import find_library


# Test that we have sandbox
if not find_library("sandbox"):
    print("sandbox library not found")
    raise ImportError("sandbox library not found")

libsandbox = ctypes.CDLL(find_library("sandbox"), ctypes.RTLD_GLOBAL)


def sandbox_init():
    """
    // /usr/include/sandbox.h
    int sandbox_init(const char *profile, uint64_t flags, char **errorbuf);
    """
    # FIXME Specifying argtypes not working for profile
    # libsandbox.sandbox_init.argtypes = [POINTER(c_char), c_uint64, POINTER(POINTER(c_char))]
    libsandbox.sandbox_init.restype = ctypes.c_int

    # Profile types -- note each leaves existing open file descriptors
    profile = libsandbox.kSBXProfileNoWrite
    # PureComputation = libsandbox.kSBXProfilePureComputation
    # NoInternet = libsandbox.kSBXProfileNoInternet
    # NoNetwork = libsandbox.kSBXProfileNoNetwork
    # NoWrite = libsandbox.kSBXProfileNoWrite
    # NoWriteExceptTemporary = libsandbox.kSBXProfileNoWriteExceptTemporary


    errorbuf_p = c_char_p()
    ret = libsandbox.sandbox_init(profile, 
        c_uint64(0x0001), 
        byref(errorbuf_p))
    if ret != 0:
        # Check errorbuf and free it
        try:
            print(errorbuf_p.value)
            libsandbox.sandbox_free_error(errorbuf_p)
        except TypeError:
            # Wasn't allocated
            pass
        return False
    else:
        return True


if __name__ == "__main__":
    from sys import exc_info
    # Tests
    sandbox_init()
    try:
        open("sandbox.py", "w")
    except OSError:
        type, value, traceback = exc_info()
        print(type, value, traceback)
        print("Test successful. Sandbox enabled.")


