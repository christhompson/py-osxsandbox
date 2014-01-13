py-osxsandbox
=============

A ctypes wrapper of the Mac OSX sandbox API.

The Mac OS X sandbox library is `sandbox.h`, and exposes functionality
similar to Linux's seccomp-bpf. Policy can be specified in a Scheme-based
DSL, although several profiles are built-in to the library. Currently,
this wrapper hard-codes which of the built-in profiles it uses.

For more information on the OS X sandbox library:
- Manpages for sandbox.h and its functions 
    - https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man7/sandbox.7.html
- Chromium OS X sandboxing design documents 
    - http://www.chromium.org/developers/design-documents/sandbox/osx-sandboxing-design

Warning!
---

While relatively simple, this is definitely alpha software. 
It's part of a research prototype
I'm developing (a security architecture for visual 
recognizer applications) -- basic tests show that it works, but more
in-depth security testing is required before using this for any security
sensitive applications (also, the OS X sandboxing API sees much less 
attention than the more advanced sandboxing used by Gatekeeper and the 
Mac App Store).

To-do
---

- Clean API for specifying sandbox profile
- Ability to specify profile files (instead of only built-in profiles)

License
---

Copyright 2014 Christopher Thompson (cthompson@cs.berkeley.edu)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
