import cProfile
import pstats
import tempfile

def profile_this(sort='cumulative', lines=None, strip_dirs=True):
    """
    cProfile decorator.
    """
    def outer(func):
        def inner(*args, **kwargs):
            file = tempfile.NamedTemporaryFile()
            prof = cProfile.Profile()
            try:
                result = prof.runcall(func, *args, **kwargs)
            except:
                file.close()
                raise

            prof.dump_stats(file.name)
            stats = pstats.Stats(file.name)
            if strip_dirs:
                stats.strip_dirs()
            if isinstance(sort, (tuple, list)):
                stats.sort_stats(*sort)
            else:
                stats.sort_stats(sort)
            stats.print_stats(lines)

            file.close()
            return result
        return inner

    # allow @profilethis or @profilethis()
    if hasattr(sort, '__call__'):
        func = sort
        sort = 'cumulative'
        outer = outer(func)
    return outer
