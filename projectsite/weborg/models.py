from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    priority_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.priority_name

class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Task(BaseModel):
    task_title = models.CharField(max_length=150)
    task_description = models.TextField()
    task_deadline = models.DateField()
    task_status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")],
        default="Pending"
    )
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    task_priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

class Note(BaseModel):
    note_content = models.TextField()
    note_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_content

class SubTask(BaseModel):
    sub_title = models.CharField(max_length=150)
    sub_status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")],
        default="Pending"
    )
    sub_parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_title
