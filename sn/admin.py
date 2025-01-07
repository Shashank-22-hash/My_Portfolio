from django.contrib import admin
from .models import Home, About, Profile , Category, Skills, Portfolio, Certification

admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1
    
@admin.register(About)  
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2
    
@admin.register(Category)  
class AboutAdmin(admin.ModelAdmin):
    inlines = [SkillsInline]
    
admin.site.register(Certification)
    
admin.site.register(Portfolio)