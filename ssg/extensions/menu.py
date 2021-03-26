from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p : not p.isinstance(parsers.ResourceParser)

