import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)