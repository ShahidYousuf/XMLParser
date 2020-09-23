from django import forms

class UploadXMLForm(forms.Form):
    xmlfile = forms.FileField(required=True, widget=forms.FileInput(attrs={"class":"form-control"}))

    def clean(self):
        xmlfile = self.cleaned_data.get('xmlfile', None)
        if xmlfile is not None:
            if not str(xmlfile).endswith(".xml"):
                msg = forms.ValidationError("The selected file has invalid extension.")
                self.add_error("xmlfile", msg)
        return self.cleaned_data