# coinhash

Compilation of coin hash modules.

This package is a collection of various hash algorithms used by cryptocurrencies.

## Usage

```python
    import coinhash
    data = '00'.decode('hex')
    sha256_digest = coinhash.SHA256Hash(data)
    sha256d_digest = coinhash.SHA256dHash(data)
    neoscrypt_digest = coinhash.NeoscryptHash(data)
    skein_digest = coinhash.SkeinHash(data)
    qubit_digest = coinhash.QubitHash(data)
    groestl_digest = coinhash.GroestlHash(data, len(data))
    x11_digest = coinhash.X11Hash(data)
    scrypt_digest = coinhash.ScryptHash(data)
```

## License

Individual licenses are located within each algorithm's directory.
They are also located in the top-level directory in files named
"LICENSE-(package name)".
