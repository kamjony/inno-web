from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email:example@gmail.com'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Type your message here'}))

    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(ContactForm, self).__init__(*args, **kwargs)

        # remove the label of a non-linked/calculated field (txt01 added at top of form)
        self.fields['email'].label = ''
        self.fields['subject'].label = ''
        self.fields['message'].label = ''
