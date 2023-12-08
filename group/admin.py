from django.contrib import admin
from .models import Teacher, Group, Student

# Register your models here.
admin.site.register(Teacher)


# admin.site.register(Group)
# admin.site.register(Student)

@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'groups_list')

    def student_name(self, obj):
        # print(obj, '!!!!!')
        return obj

    def groups_list(self, obj):
        groups = obj.groups.all()
        return [x for x in groups]


@admin.register(Group)
class Group(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count_of_students', 'list_of_students')

    def count_of_students(self, obj):
        return obj.students.count()

    def list_of_students(self, obj):
        students = obj.students.all()
        return [x for x in students]