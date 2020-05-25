import datetime
class Conta(object):
    def __init__(self, cliente: str, agencia: int, conta: int, data_abertura: datetime, saldo: float, ativo: bool):
        self.cliente = cliente
        self.agencia = agencia
        self.conta   = conta
        self.data_abertura = data_abertura
        self.saldo   = saldo
        self.ativo   = ativo

    def repr_json(self):
        return dict(
            cliente = self.cliente,
            agencia = self.agencia,
            conta   = self.conta,
            data_abertura = self.data_abertura,
            saldo   = self.saldo,
            ativo   = self.ativo
        )