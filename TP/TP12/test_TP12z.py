import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)