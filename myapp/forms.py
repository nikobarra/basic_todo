from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(
        label="Describe la tarea",
        required=False,
        widget=forms.Textarea,
    )


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo del proyecto", max_length=200)
