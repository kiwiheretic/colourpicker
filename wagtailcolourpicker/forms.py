from django import forms

from wagtailcolourpicker.utils.colour import get_colour_choices


class ColourRadioSelect(forms.widgets.RadioSelect):
    option_template_name = 'colourpicker/forms/widgets/colour_option.html'


class ColourForm(forms.Form):
    colour = forms.ChoiceField(
        label="Colours",
        choices=get_colour_choices(),
        widget=ColourRadioSelect,
        required=False
    )
