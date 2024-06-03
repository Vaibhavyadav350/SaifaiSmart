from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import TemplateHTMLRenderer

class JSONRendererWithTemplate(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context['request'].path.startswith('/api/'):
            return super().render(data, accepted_media_type, renderer_context)
        return TemplateHTMLRenderer().render({'data': data}, accepted_media_type, renderer_context)
