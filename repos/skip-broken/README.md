# skip-broken

This builds three packages, `broken-a`, `broken-b`, `broken-c`.

It builds three versions of `broken-a`, 1.2.3, 1.2.4, 2.0.0.

`broken-a-2.0.0` depends on a nonexistent package, the other versions do not.

`broken-b` depends on `broken-a-1.2.3`.

`broken-c` depends on `broken-a-1.2.4`.

Cue fun.
