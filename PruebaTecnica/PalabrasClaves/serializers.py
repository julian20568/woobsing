from rest_framework import serializers
from PalabrasClaves.models import Palabras

class PalabrasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Palabras
        fields = [
                  'cod', 'palabra1', 'palabra2', 'palabra3', 'palabra4', 'palabra5', 'palabra6', 'palabra7',
                  'palabra8', 'palabra9', 'palabra10', 'palabra11', 'palabra12', 'palabra13', 'palabra14',
                  'palabra15', 'palabra16', 'palabra17', 'palabra18', 'palabra19', 'palabra20', 'palabra21',
                  'palabra22', 'palabra23', 'palabra24', 'palabra25', 'palabra26', 'palabra27', 'palabra28',
                  'palabra29', 'palabra30', 'palabra31', 'palabra32', 'palabra33', 'palabra34', 'palabra35',
                  'palabra36', 'palabra37', 'palabra38', 'palabra39', 'palabra40', 'palabra41', 'palabra42',
                  'palabra43', 'palabra44', 'palabra45', 'palabra46', 'palabra47', 'palabra48', 'palabra49',
                  'palabra50'
                  ]