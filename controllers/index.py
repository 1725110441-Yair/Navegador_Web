import web

# Renderizador de plantillas en la carpeta 'views'
render = web.template.render('views')

# Estructura de datos: Pila (Stack - LIFO)
historial = []

class Index:
    def GET(self):
        # 3. Mostrar la página actual (tope de la pila / peek)
        if len(historial) > 0:
            pagina_actual = historial[-1]
        else:
            pagina_actual = "Ninguna (Navegador en blanco)"

        # 4. Mostrar el historial en orden descendente (LIFO)
        historial_descendente = list(reversed(historial))

        return render.index(historial_descendente, pagina_actual)

    def POST(self):
        # Leemos los datos del formulario
        formulario = web.input(accion=None, url="")
        accion = formulario.accion

        # 1. Visitar una página web (Push / append)
        if accion == "visitar":
            url = formulario.url.strip()
            if url:
                historial.append(url)

        # 2. Regresar a la página anterior (Pop / pop)
        elif accion == "regresar":
            if len(historial) > 0:
                historial.pop()

        # 5. Eliminar / vaciar historial
        elif accion == "eliminar":
            historial.clear()

        # Redirigimos al inicio para refrescar la vista
        raise web.seeother('/')