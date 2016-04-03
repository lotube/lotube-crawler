def to_utf8(val):
    try:
        return unicode(val).encode('utf8')
    except UnicodeDecodeError:
        return ''