# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

DOMINGO = 6
ULTIMO_DIA = datetime(2000, 12, 31)

dia_atual = datetime(1901, 1, 1)
qtd_domingos = 0

while dia_atual <= ULTIMO_DIA:
    if dia_atual.weekday() == DOMINGO and dia_atual.day == 1:
        qtd_domingos += 1
    dia_atual = dia_atual + timedelta(days=1)

print qtd_domingos
