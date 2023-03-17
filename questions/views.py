from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy

from questions.forms import SelectTilesFormset
from questions.forms import basic_formset
from questions.forms import ChoiceFormset
from questions.forms import QuestionChoiceForm
from django.forms import modelformset_factory


from questions.models import Question
from questions.models import QuestionChoice
from tiles.models import Tile

# Create your views here.

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question

    fields = ['question_title', 
              'question_body', 
              'question_explanation']
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = basic_formset(self.request.POST,
                                               error_messages={
                                            'too_few_forms': " Please submit at least %(num)d choices."
                                               })
            context['non_form_errors'] = context['formset'].non_form_errors()
        else:
           context['formset'] = basic_formset
        return context
    
    def form_valid(self, form):
        self.formset = ChoiceFormset(self.request.POST)
        # Validate formsets
        if len(self.formset.non_form_errors()) != 0:
            return self.form_invalid(form)
        
        # Create Question 
        question_obj = form.save(commit=False)
        question_obj.owner = self.request.user
        question_obj.save()

        correct_answer_setted = False

        for idx, choice in enumerate(self.formset):
            if choice.is_valid() and (choice.has_changed() or 
                                      choice.cleaned_data.get('choice_text')):
                choice_obj = choice.save(commit=False)
                if not correct_answer_setted:
                    question_obj.correct_choice = choice_obj    
                    correct_answer_setted = True 
                choice_obj.choice_to = question_obj
                choice_obj.choice_id = idx
                choice_obj.save()
            
        # Create Tile
        tile_obj = Tile(
            tile_headline = form.cleaned_data['question_title'],
            author = self.request.user,
            type_of_tile_char='Q',
            expected_reward=0,
            total_questions=1,

        )
        tile_obj.save()
        tile_obj.questions.add(question_obj)

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('select_tiles', kwargs={"pk":self.object.pk})


class MyQuestionsUpdate(UpdateView):
    model = Question
    fields = ['question_title', 
              'question_body', 
              'question_explanation']
    
    basic_modelformset = modelformset_factory(QuestionChoice, 
                                         form=QuestionChoiceForm, extra=0)
        
    def form_valid(self, form):
        self.formset = ChoiceFormset(self.request.POST)

        if len(self.formset.non_form_errors()) != 0:
            return self.form_invalid(form)

        # delete all choices to recreate them
        QuestionChoice.objects.filter(choice_to=self.object).delete()
        correct_answer_setted = False

        for idx, choice in enumerate(self.formset):
            print(choice.is_valid(), choice.cleaned_data)
            if choice.is_valid() and (choice.has_changed() or 
                                      choice.cleaned_data.get('choice_text')):
                choice_obj = choice.save(commit=False)
                if not correct_answer_setted:
                    self.object.correct_choice = choice_obj    
                    correct_answer_setted = True 
                choice_obj.choice_to = self.object
                choice_obj.choice_id = idx
                choice_obj.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            if self.request.POST:
                context['formset'] = ChoiceFormset(self.request.POST,
                                                error_messages={
                                                'too_few_forms': 
                                                " Please submit at least %(num)d choices."
                                                })
                context['non_form_errors'] = context['formset'].non_form_errors()
            else:
                getmodelformset = self.basic_modelformset(
                        queryset=QuestionChoice.objects.filter(choice_to=self.object))
                context['formset'] = getmodelformset
            return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('select_tiles', kwargs={"pk":self.object.pk})
    

class SelectTiles(FormView,  SingleObjectMixin):
    ''' For selecting Tiles after creating Question '''
    model = Question
    template_name = 'tiles/tile_form_list.html'
    form_class = SelectTilesFormset
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['form_kwargs'] = {'obj': self.object}
        return kwargs

