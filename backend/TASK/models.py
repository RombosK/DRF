from django.db import models
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Updated')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Project(BaseModel):
    project_name = models.CharField(max_length=124, verbose_name='Title')
    description = models.CharField(max_length=255, verbose_name='Description', **NULLABLE)
    project_url = models.URLField(max_length=255, verbose_name='Project link', **NULLABLE)
    project_workers = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,
                                        verbose_name='Workers')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created', 'project_name']


class Todo(BaseModel):
    DoesNotExist = models.Manager
    note_header = models.CharField(max_length=64, verbose_name='Header', null=True)
    note_text = models.CharField(max_length=255, verbose_name='Text')
    is_active = models.BooleanField(default=True, verbose_name='Activity')
    note_worker = models.OneToOneField(get_user_model(), on_delete=models.SET_NULL, null=True,
                                       verbose_name='Note creator')
    note_project = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name='Note project')

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
