from django_components import component

@component.register("greeting")
class Greeting(component.Component):
    template_name = "greeting/greeting.html"

    def get_context_data(self, name="World"):
        return {
            "name": name,
        }
