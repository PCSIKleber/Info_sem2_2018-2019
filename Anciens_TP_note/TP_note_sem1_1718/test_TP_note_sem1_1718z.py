import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)