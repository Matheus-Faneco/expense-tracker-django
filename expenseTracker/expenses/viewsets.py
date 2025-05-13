from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated

class ExpenseViewSet(viewsets.ModelViewSet):
    #verificação de autenticação
    permission_classes = (IsAuthenticated,)

    queryset = Expense.objects.all() #---> lista todas as depesas de todos os usuários
    serializer_class = ExpenseSerializer
    ordering_fields = '__all__'
    ordering = '-id'

    #sobrescreve o metodo queryset
    #a intenção é filtrar as despesas do usuario para ver somente as dele
    #self.request.user é o usuario autenticado
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    #chamado automaticamente na requisiçao de POST
    #a intenção é atribuir automaticamente a despesa ao usuario AUTENTICADO
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)