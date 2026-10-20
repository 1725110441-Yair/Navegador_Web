import web

render = web.template.render('views')

historial = []

class Index:
    def GET(self):
        if len(historial) > 0:
            pagina_actual = historial[-1]
        else:
            pagina_actual = "Ninguna"

        historial_descendente = list(reversed(historial))

        return render.index(historial_descendente, pagina_actual)

    def POST(self):
        formulario = web.input()
        accion = formulario.get('accion')

        if accion == "visitar":
            url = formulario.get('url')
            if url:
                historial.append(url)

        elif accion == "regresar":
            if len(historial) > 0:
                historial.pop()

        elif accion == "eliminar":
            historial.clear()

        return self.GET()