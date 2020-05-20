# Simple Persistent Cache
[![Build Status](https://travis-ci.com/pallabpain/pcache.svg?branch=master)](https://travis-ci.com/pallabpain/pcache)
[![Python](https://img.shields.io/pypi/pyversions/pcache)](https://pypi.org/project/persistent)

pcache is simple Python 3 implementation of persistent cache.

## Installation
To install `pcache`, simply run
```
pip install pcache
```

## Usage
**Adding a key**
```
>>> from pcache import PersistentCache
>>> cache = PersistentCache(filename="cachefile")
>>> cache["objId"] = "7sdjhds8"
>>> cache["objId"]
'7sdjhds8'
```
**Cache Expiry**
```
>>> cache.expire("objId", ttl=30) # Expire key in 30 seconds
>>> import time
>>> time.sleep(35)
>>> print(cache["objId"])
None
```
