from django.contrib import admin
from .models import Categoria, Producto, Cliente

# Función para la acción personalizada
def marcar_como_agotado(modeladmin, request, queryset):
    for producto in queryset:
        if "(Agotado)" not in producto.nombre:  # Para evitar duplicados
            producto.nombre = f"{producto.nombre} (Agotado)"
            producto.save()  # Guarda los cambios en la base de datos
    modeladmin.message_user(request, "Los productos seleccionados han sido marcados como 'Agotado'.")

# Personalización de la vista en el admin de Django para la categoría
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')

# Personalización de la vista en el admin de Django para el producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'pub_date')
    actions = [marcar_como_agotado]  # Registrar la acción personalizada

# Registrar el modelo Categoria con las opciones personalizadas
admin.site.register(Categoria, CategoriaAdmin)

# Registrar el modelo Producto con la acción personalizada
admin.site.register(Producto, ProductoAdmin)

# Registrar el modelo Cliente sin modificaciones
admin.site.register(Cliente)
