import learningthewordapp.infrastructure.static_cache as static_cache
import pyramid.httpexceptions as exc
from pyramid.renderers import get_renderer


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id
        self.base_title = 'LearningTheWord.com'

        # find renderer
        layout_renderer = get_renderer('learningthewordapp:templates/share/_template.pt')
        impl = layout_renderer.implementation()
        self.template = impl.macros['template']

    @property
    def is_logged_in(self):
        return False

    def redirect(self, to_url, permanent=False):
        if permanent:
            raise exc.HTTPMovedPermanently(to_url)
        raise exc.HTTPFound(to_url)
