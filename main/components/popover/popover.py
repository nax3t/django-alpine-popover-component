from django_components import component

@component.register("popover")
class Popover(component.Component):
    template_name = "popover/popover.html"

    class Media:
        js = [
            'https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js',
        ]

    def get_context_data(self, title="Dimensions", description="Set the dimensions for the layer."):
        return {
            "title": title,
            "description": description,
        }
