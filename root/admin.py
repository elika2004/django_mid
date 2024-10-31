from django.contrib import admin

from .models import User , Testimonials, FQA , Services , Services_two , Pros , Prices

admin.site.register(User)
admin.site.register(FQA)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Services_two)
admin.site.register(Pros)
admin.site.register(Prices)


