# -*- coding: UTF-8 -*-
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    '''try:
        import unicodedata
        unicodedata.mumeric(s)
        return true
    except(TypeError,ValueError):
        pass
    return False'''

print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
