from django.contrib import admin
from .models import Post, Comentario

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    search_fields = ('titulo', 'corpo')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ('status', '-publicado')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'nome', 'email', 'criado', 'ativo')
    ordering = ('post', 'ativo', 'criado')
    list_filter = ('post', 'ativo')

