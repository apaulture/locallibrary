from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class BookInstanceInline(admin.StackedInline):
    model = BookInstance
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # fields = [('', '')]
    # exclude = ['']

    inlines = [BookInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'book_author', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]

admin.site.register(Author, AuthorAdmin)