from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from models.profissional import Profissional, Profissionais
from datetime import datetime, timedelta

class View:
    def cliente_admin():
        for c in View.cliente_listar():
            if c.__email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)  
        igual = False
        for x in Clientes:
            if c.__email == x.__email:
                igual = True
                break
        if igual == False:
            Clientes.inserir(c)
        else:
            raise ValueError("Email em uso. ")

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        igual = False
        for x in Clientes:
            if c.__email == x.__email:
                igual = True
                break
        if igual == False:
            Clientes.atualizar(c)
        else:
            raise ValueError("Email em uso. ")

    def cliente_excluir(id):
        igual = False
        for x in Horarios:
            if x.__id_cliente == id:
                igual = True
                break
        if igual == False:
            c = Cliente(id, "", "", "", "")
            Clientes.excluir(c)    
        else:
            raise ValueError("O cliente possui horário. ")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.__email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.__confirmado = confirmado
        c.__id_cliente = id_cliente
        c.__id_servico = id_servico
        
        clienteverdadeiro = False
        for x in Clientes:
            if c.__id_cliente == x.__id:
                clienteverdadeiro = True
                break
        servicoverdadeiro = False
        for x in Servicos:
            if c.__id_cliente == x.__id:
                servicoverdadeiro = True
                break
        
        if clienteverdadeiro == True and servicoverdadeiro == True:
            Horarios.inserir(c)
        elif clienteverdadeiro == False and servicoverdadeiro == True:
            raise ValueError("Não há cliente com o id inserido. ")
        elif clienteverdadeiro == True and servicoverdadeiro == False:
            raise ValueError("Não há serviço com o id inserido. ")
        else:
            raise ValueError("Não há cliente com o id insirido nem há serviço com o id inserido. ")

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.__data >= datetime.now() and h.__id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.__confirmado = confirmado
        c.__id_cliente = id_cliente
        c.__id_servico = id_servico
        
        clienteverdadeiro = False
        for x in Clientes:
            if c.__id_cliente == x.__id:
                clienteverdadeiro = True
                break
        servicoverdadeiro = False
        for x in Servicos:
            if c.__id_cliente == x.__id:
                servicoverdadeiro = True
                break
        
        if clienteverdadeiro == True and servicoverdadeiro == True:
            Horarios.atualizar(c)
        elif clienteverdadeiro == False and servicoverdadeiro == True:
            raise ValueError("Não há cliente com o id inserido. ")
        elif clienteverdadeiro == True and servicoverdadeiro == False:
            raise ValueError("Não há serviço com o id inserido. ")
        else:
            raise ValueError("Não há cliente com o id insirido nem há serviço com o id inserido. ")

    def horario_excluir(id):
        igual = False
        for x in Horarios:
            if x.__id == id:
                igual = True
                break
        if igual == False:
            c = Horario(id, None)
            Horarios.excluir(c)       
        else:
            raise ValueError("Horario em uso na agenda. ")
        
         

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        #data = "05/11/2024"
        #inicio = "08:00"
        #fim = "12:00"
        #intervalo = 60
        i = data + " " + hora_inicio   # "05/11/2024 08:00"
        f = data + " " + hora_fim      # "05/11/2024 12:00"
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            #cadastrar o horário x
            View.horario_inserir(x, False, None, None)
            #passar para o próximo horário
            x = x + d

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        igual = False
        for x in Horarios:
            if x.__id_servico == id:
                igual = True
                break
        if igual == False:
            c = Servico(id, "", 0, 0)
            Servicos.excluir(c)    
        else:
            raise ValueError("Serviço em uso na agenda. ")

    def profissional_inserir(nome, especialidade, conselho, email, senha):
        c = Profissional(0, nome, especialidade, conselho, email, senha)
        Profissionais.inserir(c)

    def profissional_listar():
        return Profissionais.listar()    

    def profissional_listar_id(id):
        return Profissionais.listar_id(id)    

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        c = Profissional(id, nome, especialidade, conselho, email, senha)
        Profissionais.atualizar(c)

    def profissional_excluir(id):
        c = Profissional(id, "", "", "", "", "")
        Profissionais.excluir(c)    