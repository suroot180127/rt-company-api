from django import forms
from accounts.models import Department

class DepartmentForm(forms.ModelForm):
    
    def save(self, commit=True):
        import pdb
        pdb.set_trace()
        extra_field = self.cleaned_data.get('extra_field', None)
        # ...do something with extra_field here...
        return super(DepartmentForm, self).save(commit=commit)

    class Meta:
        model = Department
        fields = '__all__'