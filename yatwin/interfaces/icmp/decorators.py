"""
Library containing decorators for 'icmp'

Contains:
    kwarg_or_attr
"""

def kwarg_or_attr(key, attr=None, not_in=()):
    """
    Checks that {key} is a class attribute
    ... or present in **kwargs,
    ... else, raises a <TypeError>

    :param key - The key that should be present in the kwargs
    :param attr - The attribute that the class should have
    :param not_in - A list/tuple of illegal values
    """

    if attr is None:
        attr = key

    def decorator(func):
        """
        Decorator to wrap func

        :param func - The function to wrap
        """

        def wrapper(cls, *args, **kwargs):
            """
            The function wrapper
            """

            if hasattr(cls, attr):
                cls_attr = getattr(cls, attr)

                kwargs.update({key: cls_attr})
            elif key not in kwargs:
                raise TypeError(f'Missing kwarg/attr: \'{key}\'')

            val = kwargs.get(key)

            if val in not_in:
                raise TypeError(f'Illegal value for \'{key}\'')

            return func(cls, *args, **kwargs)

        return wrapper

    return decorator
