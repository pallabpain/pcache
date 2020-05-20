# Simple Persistent Cache
[![Build Status](https://travis-ci.com/pallabpain/pcache.svg?branch=master)](https://travis-ci.com/pallabpain/pcache)

pcache is simple Python 3 implementation of persistent cache.

## Installation
To install `pcache`, simply run
```
pip install pcache
```

## Usage
```
>>> from pcache import PersistentCache
>>> cache = PersistentCache(filename="cachefile")
>>> cache["objId"] = "7sdjhds8"
>>> cache["objId"]
'7sdjhds8'
```
