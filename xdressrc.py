from xdress.utils import apiname

package = 'memleak'     # top-level python package name

extra_types = 'extra_types'

stlcontainers = [
    ('vector', 'int'),
    ]

classes = [
    apiname('Hollow', 'hollow.*', incfiles='hollow.h'),
    ]

