from django import forms

from .models import Question, Choice


class QuestionForm(forms.ModelForm):  # Se utiliza la clase ModelForm ya que el formulario se va a basar en un modelo

    class Meta:
        model = Question
        fields = '__all__'  # Uso __all__ para renderizar todos los atributos del modelo


class ChoicesForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('question', 'choice_text')
