from pyramid.scaffolds import PyramidTemplate


class BuildoutTemplate(PyramidTemplate):
    _template_dir = 'buildout_template'
    summary = 'Buildout configuration'
