import qubit_hash
import weakref
import binascii
import StringIO
import struct

from binascii import unhexlify

def uint256_from_str(s):
    r = 0L
    t = struct.unpack("<IIIIIIII", s[:32])
    for i in xrange(8):
        r += t[i] << (i * 32)
    return r

teststart = '700000009da3e71afe06285056f917d22343faaf58655cfa75beb268452c082c00000000f54b50a00de0f7769b7a2c5b4b2203269f50a1a5c62d301b10ff5dc5a5e51d57006dd852060e631cd00b85d60101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff2902fe35062f503253482f04026dd85208f800000300000000102f536d616c6c54696d65506f6f6c732f00000000010000350c000000001976a914b18a7b92c4b55a1458c4522ff88f44201916f33088ac00000000';
testbin = unhexlify(teststart)
hash_bin = qubit_hash.getPoWHash(testbin)
hash_int = uint256_from_str(hash_bin)
print("%s" % hash_int)

