from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc
from tkcalendar import DateEntry

app = Tk()


class PartesBichinho:


    def baterpartesbichinho(self):
        self.app5 = Toplevel()
        self.app5.geometry('970x600+390+56')
        self.app5.resizable(False, False)
        self.app5.transient(app)
        self.app5.focus_force()
        self.app5.grab_set()
        self.app5.configure(bg='#421212')
        self.labelbaterpartesbichinho()
        self.entryspartesbichinho()
        self.botaoesdepartes()
        self.treviewdepartesbichinhos()
        self.treviewbuscatamanho()

    def labelbaterpartesbichinho(self):
        self.labelid = Label(self.app5, text=' ID', bg='#421212', fg='YELLOW', relief=FLAT, font='times 15 bold', )
        self.labelid.place(x=650, y=20)

        self.labeltexto = Label(self.app5, text=' S U B L I M A Ç Ã O', bg='#421212', fg='YELLOW', relief=FLAT,
                                font='times 40 bold',)
        self.labeltexto.place(x=120, y=20)

        self.labelpartestexto = Label(self.app5, text=' P A R T E S    D E    B I C H I N H O S  ', bg='#421212',
                                      fg='white', relief=FLAT, font='times 15 bold')
        self.labelpartestexto.place(x=200, y=100)

        self.labelnome = Label(self.app5, text='SUBLIMADOR', bg='#421212', fg='white', relief=FLAT,
                               font='times 15 bold')
        self.labelnome.place(x=10, y=160)

        self.labelmanga = Label(self.app5, text='MANGA', bg='#421212', fg='white', relief=FLAT, font='times 15 bold')
        self.labelmanga.place(x=65, y=210)

        self.labelcapuz = Label(self.app5, text='CAPUZ', bg='#421212', fg='white', relief=FLAT, font='times 15 bold')
        self.labelcapuz.place(x=70, y=260)

        self.labeltamanho = Label(self.app5, text='TAMANHO', bg='#421212', fg='white', relief=FLAT,
                                  font='times 15 bold')
        self.labeltamanho.place(x=35, y=310)

        self.labelquantidade = Label(self.app5, text='QUANTIDADE', bg='#421212', fg='white', relief=FLAT,
                                     font='times 15 bold')
        self.labelquantidade.place(x=10, y=360)

        self.labelbuscatext = Label(self.app5, text='BUSCA CLIENTE', bg='#421212', fg='white', relief=FLAT,
                                    font='times 15 bold')
        self.labelbuscatext.place(x=560, y=220)

    def entryspartesbichinho(self):

        self.entryid = Entry(self.app5, font='times 15', width=5)
        self.entryid.place(x=685, y=20)

        self.entrypartessublimador = Entry(self.app5, font='times 15')
        self.entrypartessublimador.place(x=155, y=160)

        self.entrypartesmanga = Entry(self.app5, font='times 15', width=10)
        self.entrypartesmanga.place(x=155, y=210)

        self.entrypartescapuz = Entry(self.app5, font='times 15', width=10)
        self.entrypartescapuz.place(x=155, y=260)

        self.entrypartetamanho = Entry(self.app5, font='times 15', width=10)
        self.entrypartetamanho.place(x=155, y=310)

        self.entrypartetamanho = Entry(self.app5, font='times 15', width=10)
        self.entrypartetamanho.place(x=155, y=360)

        self.entrybusca = Entry(self.app5, font='times 15', width=10)
        self.entrybusca.place(x=655, y=260)

    def botaoesdepartes(self):

        self.foto = PhotoImage(file='image/bater.png')
        self.baterpartes = Button(self.app5, text='BATER', image=self.foto, compound=LEFT, font='times 15 bold')
        self.baterpartes.place(x=280, y=320)

        self.labelbusca = Button(self.app5, text='BUSCAR', bg='#421212', fg='white', font='times 12 bold')
        self.labelbusca.place(x=560, y=260)

    def treviewdepartesbichinhos(self):
        self.columns = ('sublimador', 'modelo', 'manga', 'capuz', 'tamanho', 'quantidade')

        self.treviewpartes = ttk.Treeview(self.app5, columns=self.columns, show='headings')

        self.treviewpartes.heading('sublimador', text='SUBLIMADOR')
        self.treviewpartes.heading('modelo', text='MODELO')
        self.treviewpartes.heading('manga', text='MANGA')
        self.treviewpartes.heading('capuz', text='CAPUZ')
        self.treviewpartes.heading('tamanho', text='TAMANHO')
        self.treviewpartes.heading('quantidade', text='QUANTIDADE')

        self.treviewpartes.column('sublimador', width=40)
        self.treviewpartes.column('modelo', width=40)
        self.treviewpartes.column('manga', width=40)
        self.treviewpartes.column('capuz', width=40)
        self.treviewpartes.column('tamanho', width=40)
        self.treviewpartes.column('quantidade', width=40)

        self.treviewpartes.place(x=10, y=420, width=550, height=175)
        self.scrolll = Scrollbar(self.app5, orient=VERTICAL)
        self.scrolll = Scrollbar(self.app5, orient=VERTICAL, command=self.treviewpartes.yview)
        self.treviewpartes.configure(yscrollcommand=self.scrolll.set)
        self.scrolll.place(x=565, y=420, width=25, height=175)

    def treviewbuscatamanho(self):
        self.columns = ('id', 'sublimador', 'modelo', 'manga', 'capuz', 'tamanho', 'quantidade')

        self.treviewbuscarpartes = ttk.Treeview(self.app5, columns=self.columns, show='headings')
        self.treviewbuscarpartes.heading('id', text='ID')
        self.treviewbuscarpartes.heading('sublimador', text='SUBLIMADOR')
        self.treviewbuscarpartes.heading('modelo', text='MODELO')
        self.treviewbuscarpartes.heading('manga', text='MANGA')
        self.treviewbuscarpartes.heading('capuz', text='CAPUZ')
        self.treviewbuscarpartes.heading('tamanho', text='TAMANHO')
        self.treviewbuscarpartes.heading('quantidade', text='QUANTIDADE')

        self.treviewbuscarpartes.column('id', width=10)
        self.treviewbuscarpartes.column('sublimador', width=30)
        self.treviewbuscarpartes.column('modelo', width=20)
        self.treviewbuscarpartes.column('manga', width=20)
        self.treviewbuscarpartes.column('capuz', width=20)
        self.treviewbuscarpartes.column('tamanho', width=40)
        self.treviewbuscarpartes.column('quantidade', width=40)

        self.treviewbuscarpartes.place(x=450, y=310, width=460, height=50)


class CorpoBichinho(PartesBichinho):

    def tela_bichinho(self):
        self.app3 = Toplevel()
        self.app3.geometry('1170x650+110+16')
        self.app3.resizable(False, False)
        self.app3.transient(app)
        self.app3.focus_force()
        self.app3.grab_set()
        self.app3.configure(bg='#2a2a29')
        self.treeview_batida_bichinho()
        self.treeview_busca_corpo()
        self.menudepartesfantasia()
        self.entry_da_telabichinho()
        self.label_da_telabichinho()
        self.botoes_telabichinho()
        self.data()

    def label_da_telabichinho(self):
        self.labelid = Label(self.app3, text='ID', font='times 20 bold', relief=FLAT, bg='#2a2a29', fg='WHITE')
        self.labelid.place(x=850, y=35)

        self.labelote = Label(self.app3, text='LOTE', font='times ', relief=FLAT, bg='#2a2a29', fg='WHITE')
        self.labelote.place(x=1040, y=15)

        self.sublimador = Label(self.app3, text='SUBLIMADOR', font='times 15 bold', relief=FLAT, bg='#2a2a29', fg='RED')
        self.sublimador.place(x=10, y=10)

        self.texto = Label(self.app3, text='A R E A    D E    S U B L I M A Ç Ã O ', font='times 25 bold', relief=FLAT,
                           bg='#2a2a29', fg='WHITE')
        self.texto.place(x=250, y=40)

        self.textoC = Label(self.app3, text='CORPO DE (FANTASIA) ', font='times 25 bold', relief=FLAT, bg='#2a2a29',
                            fg='YELLOW')
        self.textoC.place(x=350, y=80)

        self.textoestoque = Label(self.app3, text='PESQUISAR  ESTOQUE', font='times 20 bold', relief=FLAT, bg='#2a2a29',
                                  fg='WHITE')
        self.textoestoque.place(x=810, y=320)

        self.cliente = Label(self.app3, text='CLIENTE', relief=FLAT, fg='#98dd45', bg='#2a2a29', font='times 15 bold')
        self.cliente.place(x=10, y=100)
        self.seguimento = Label(self.app3, text='SEGUIMENTO', relief=FLAT, fg='#98dd45', bg='#2a2a29',
                                font='times 15 bold')
        self.seguimento.place(x=10, y=130)

        self.labeltema = Label(self.app3, text='TEMA', relief=FLAT, fg='#98dd45', bg='#2a2a29', font='times 15 bold')
        self.labeltema.place(x=10, y=315)

        self.modelo = Label(self.app3, text='MODELO', relief=FLAT, fg='#98dd45', bg='#2a2a29', font='times 15 bold')
        self.modelo.place(x=10, y=160)

        self.tamanho = Label(self.app3, text='TAMANHO', relief=FLAT, fg='#98dd45', bg='#2a2a29', font='times 15 bold')
        self.tamanho.place(x=10, y=190)

        self.frente = Label(self.app3, text='FRENTE', relief=FLAT, fg='#98dd45', bg='#2a2a29', font='times 15 bold')
        self.frente.place(x=10, y=220)

        self.costa = Label(self.app3, text='COSTA', relief=FLAT, fg='#98dd45', bg='#2a2a29', font='times 15 bold')
        self.costa.place(x=10, y=250)

        self.quantidade = Label(self.app3, text='QUANTIDADE', relief=FLAT, fg='RED', bg='#2a2a29', font='times 15 bold')
        self.quantidade.place(x=5, y=285)

        self.tamanho_lab_busca = Label(self.app3, text='TAMANHO', relief=FLAT, fg='YELLOW', bg='#2a2a29',
                                       font='times 15 bold')
        self.tamanho_lab_busca.place(x=850, y=380)

        self.labelcliente = Label(self.app3, text='CLIENTE', relief=FLAT, fg='YELLOW', bg='#2a2a29',
                                  font='times 15 bold')
        self.labelcliente.place(x=100, y=370)

    def entry_da_telabichinho(self):
        self.id = Entry(self.app3, font='times 15 bold', width=5)
        self.id.place(x=900, y=40)

        self.lote = Entry(self.app3, font='times 15 bold', width=5)
        self.lote.place(x=1090, y=10)

        self.nome_sublimador = Entry(self.app3, font='times 15 bold', width=15)
        self.nome_sublimador.place(x=10, y=40)

        self.temaB = Entry(self.app3, font='times 15 bold', width=20)
        self.temaB.place(x=90, y=315)

        self.clienteB = Entry(self.app3, font='times 15 bold', width=15)
        self.clienteB.place(x=150, y=100)

        self.seguimentoB = Entry(self.app3,  font='times 15 bold', width=15)
        self.seguimentoB.place(x=150, y=132)

        self.modeloB = Entry(self.app3,  font='times 15 bold', width=15)
        self.modeloB.place(x=150, y=162)

        self.tamanhoB = Entry(self.app3, relief=FLAT, font='times 15 bold', width=15)
        self.tamanhoB.place(x=150, y=192)

        self.frenteB = Entry(self.app3, relief=FLAT,  font='times 15 bold', width=15)
        self.frenteB.place(x=150, y=222)

        self.costaB = Entry(self.app3, relief=FLAT,  font='times 15 bold', width=15)
        self.costaB.place(x=150, y=252)

        self.quantidadeB = Entry(self.app3, fg='red', font='times 15 bold', width=8)
        self.quantidadeB.place(x=150, y=285)

# busca corpor
        self.tamanhoc = Entry(self.app3, font='times 15 bold', width=9)
        self.tamanhoc.place(x=970, y=380)

        self.clienteBusca = Entry(self.app3, font='times 15 bold', width=17)
        self.clienteBusca.place(x=100, y=400)

    def botoes_telabichinho(self):

        self.photocliente = PhotoImage(file='image/cliente.png')
        self.clientepesquisa = Button(self.app3, text='BUSCA => ', image=self.photocliente, fg='RED', bg='#2a2a29',
                                      border=4, compound=TOP, relief=FLAT, font='times', command=self.busca_cliente)
        self.clientepesquisa.place(x=5, y=370)

        self.detalhe = PhotoImage(file='image/detalhe.png')
        self.clientepesquisaa = Button(self.app3, image=self.detalhe, compound=TOP, text='+Detalhada', bg='#2a2a29',
                                       fg='RED', font='times 13 bold', relief=FLAT, command=self.busca_detalhada)
        self.clientepesquisaa.place(x=280, y=365)

        self.baterp = PhotoImage(file='image/bater.png')
        self.bater = Button(self.app3, text=' COMPLETO', image=self.baterp, compound=LEFT, fg='RED',
                            font='times 10 bold', bg='#2a2a29', border=5, command=self.bater_corpo_sql)
        self.bater.place(x=310, y=285)

        self.buscacp = PhotoImage(file='image/busca.png')
        self.buscac = Button(self.app3, text='busca', image=self.buscacp, fg='RED', font='times 15 bold',
                             command=self.buscar_corpo_sql)
        self.buscac.place(x=1080, y=370)

        self.batertamanho = Button(self.app3, text='INDIVIDUAL', image=self.baterp, fg='YELLOW', bg='#2a2a29',
                                   font='times 10 bold', compound=LEFT, border=5, command=self.bater_corpo_individual)
        self.batertamanho.place(x=310, y=150)

        self.inserirpartes = Button(self.app3, text='INSERIR F/C', fg='YELLOW', bg='#2a2a29', font='times 10 bold',
                                    compound=LEFT, border=5, command=self.inserircorpo)
        self.inserirpartes.place(x=1080, y=140)

        self.retirarpartes = Button(self.app3, text='RETIRAR', fg='YELLOW', bg='#2a2a29',
                                    font='times 10 bold', compound=LEFT, border=5)
        self.retirarpartes.place(x=1080, y=180)

        self.limparpartes = Button(self.app3, text='LIMPAR', fg='YELLOW', bg='#2a2a29', font='times 10 bold',
                                   compound=LEFT, border=5, command=self.limpar_campo_batida_corpo2)
        self.limparpartes.place(x=1080, y=220)

        self.nonee = Button(self.app3, text='INFORMAR', fg='YELLOW', bg='#2a2a29', font='times 10 bold', compound=LEFT,
                            border=5, command=self.verifica_fc_none)
        self.nonee.place(x=1080, y=260)

    def getbatida(self):
        self.idd = self.id.get().strip().capitalize()
        self.data_b = self.date_batida.get().strip().capitalize()
        self.nome = self.nome_sublimador.get().strip().capitalize()
        self.cliente = self.clienteB.get().strip().capitalize()
        self.seguimento = self.seguimentoB.get().strip().capitalize()
        self.modelo = self.modeloB.get().strip().capitalize()
        self.tamanho = self.tamanhoB.get().capitalize()
        self.frente = self.frenteB.get().capitalize().strip()
        self.costa = self.costaB.get().capitalize().strip()
        self.quantidad = self.quantidadeB.get()
        self.lotee = self.lote.get().capitalize().strip()
        self.temaa = self.temaB.get().capitalize().strip()
        self.nome_cliente = self.clienteBusca.get().capitalize().strip()

    def verifica_fc_none(self):
        self.getbatida()
        self.sql()
        nonne = None

        self.n = self.cursor.execute(f"""SELECT frente_s, costa_s from fantasia
                  WHERE cliente = '{self.cliente}' 
                  and data_batida ='{self.data_b}'
                  and ID = {self.idd}""")

        if self.cliente == '':
            messagebox.showinfo('', 'informe o nome do cliente')
        else:
            for f, c in self.n:
                if c == nonne and f != nonne:
                    self.cursor.execute(f"""UPDATE fantasia SET costa_s=0 where cliente = '{self.cliente}'
                                                                                and ID = '{self.idd}'
                                                                                and tamanho_s = '{self.tamanho}'
                                                                                 and ID = {self.idd}""")
                    self.fechar_comit()
                elif f == nonne and c != nonne:
                    self.cursor.execute(f"""UPDATE fantasia SET frente_s=0 where cliente = '{self.cliente}'
                                                                                   and ID = '{self.idd}'
                                                                                   and tamanho_s = '{self.tamanho}'""")
                    self.fechar_comit()
                else:
                    messagebox.showinfo('', 'nao e possivel liberar para inserir pois o valor ja conta '
                                            f'o valor e de {f} frente')

    def inserir_costa(self):
        self.cursor.execute(f""" UPDATE fantasia SET costa = costa - '{self.quantidad}'
                                                                                  where tamanho = '{self.tamanho}'""")

        self.cursor.execute(f""" UPDATE fantasia SET costa_s = costa_s  + '{self.quantidad}'
                                                                                  where cliente = '{self.cliente}'
                                                                                  and data_batida = '{self.data_b}'
                                                                                  and tamanho_s = '{self.tamanho}'
                                                                                  and ID = '{self.idd}'""")
        self.select_batida()
        self.valorbusca_detalhada()

    def inserir_frente(self):
        self.cursor.execute(f""" UPDATE fantasia SET frente = frente - '{self.quantidad}'
                                                                      where tamanho = '{self.tamanho}'""")

        self.cursor.execute(f""" UPDATE fantasia SET frente_s = frente_s  + '{self.quantidad}'
                                                                              where cliente = '{self.cliente}'
                                                                              and data_batida = '{self.data_b}'
                                                                              and tamanho_s = '{self.tamanho}'
                                                                              and ID = '{self.idd}'""")

        self.select_batida()
        self.valorbusca_detalhada()

    def inserircorpo(self):
        self.sql()
        self.treeview_batida_corpo.delete(*self.treeview_batida_corpo.get_children())
        self.treeviewcorpobichinho.delete(*self.treeviewcorpobichinho.get_children())
        self.getbatida()
        bichinho = 'Bichinho'
        inserir = 'Inserir'

        if self.frente == inserir and self.costa == inserir:
            messagebox.showinfo('AVISO', 'SO E PERMITIDO UMA PARTE POR VEZ'.upper())

        elif self.idd == '' or self.data_b == '' or self.nome == '' or self.cliente == '' or self.seguimento == '' or \
                self.modelo == '' or self.tamanho == '' or self.frente == '' or self.costa == '' or \
                self.quantidad == '' or self.lotee == '' or self.temaa == '' :
            self.messagem_batida_individual()

        elif self.frente == bichinho and self.costa == bichinho:
            messagebox.showinfo('AVISO', 'informe a palavra >> inserir << na parte deseja fazer a incer'.upper())

        elif self.costa == inserir:
            inserir = self.cursor.execute(f"""select frente,costa from fantasia where tamanho = '{self.tamanho}' """)
            for f, c in inserir:
                try:
                    if c >= int(self.quantidad):
                        self.inserir_costa()
                    else:
                        messagebox.showerror('ops',
                                             ' nao foi possivel inserir a quantidade de costa e insulficiente \n '
                                             f'voce esta informando {self.quantidad} costa \n'
                                             f' ea quantidade em estoque e de {f} \n'
                                             'e necessario fazer a reposiçao dessa parte'.upper())
                except:
                    messagebox.showerror('erro', 'nao e possivel inserir, informe a quantidade correta \n '
                                        f'voce esta informando >> {self.quantidad} << esse nao e um valor valido')
        elif self.frente == inserir:
            inserir = self.cursor.execute(f""" SELECT frente,costa FROM fantasia WHERE tamanho = '{self.tamanho}' """)
            for f, c in inserir:
                try:
                    if f >= int(self.quantidad):
                        self.inserir_frente()
                    else:
                        messagebox.showerror(
                            'ops', ' nao foi possivel inserir a quantidade de frente e insulficiente \n '
                                   f'voce esta informando {self.quantidad} frente \n'
                                   f' ea quantidade em estoque e de {f} \n'
                                   'e necessario fazer a reposiçao dessa parte'.upper())
                except:
                    messagebox.showerror('erro', 'nao e possivel inserir, informe a quantidade correta \n '
                                            f'voce esta informando >> {self.quantidad} << esse nao e um valor valido')
        self.fechar_comit()

    def bater_corpo_sql(self):
        self.treeview_batida_corpo.delete(*self.treeview_batida_corpo.get_children())
        self.getbatida()
        self.sql()

        if self.idd == '' or self.data_b == '' or self.nome == '' or self.cliente == '' or self.seguimento == '' or \
                self.modelo == '' or self.tamanho == '' or self.frente == '' or self.costa == '' or \
                self.quantidad == '' or self.lotee == '' or self.temaa == '':
            self.messagem_batida_individual()

        else:
            self.msg1 = messagebox.askyesno(
                'INFORMAÇÃO', f'DESEJA REGISTRAR {self.quantidad} FANTASIA NO TAMANHO {self.tamanho} DO CLIENTE '
                              f'{self.nome}')

            if self.msg1 == TRUE:

                tabela = self.cursor.execute(
                    f"""SELECT frente,costa FROM fantasia WHERE
                                                      seguimento = '{self.seguimento}' AND tamanho = '{self.tamanho}'
                                                                                      AND  ID = {self.idd} """)
                for f, c in tabela:
                    try:
                        if f >= int(self.quantidad) and c >= int(self.quantidad):

                            self.registrar = self.cursor.execute(
                                f"""INSERT INTO fantasia (
                                  data_batida, sublimador, cliente, seguimento_s, modelo_s, tamanho_s, frente_s,costa_s
                                      )
                              VALUES(
                              '{self.data_b}', '{self.nome}', '{self.cliente}', '{self.seguimento}', '{self.modelo}', 
                                      '{self.tamanho}', '{self.quantidad}', '{self.quantidad}')""")

                            self.vender = self.cursor.execute(
                                f"""UPDATE fantasia SET frente = frente - '{self.quantidad}',
                                                                                  costa = costa - '{self.quantidad}'
                                                                        WHERE ID = {self.idd} ; """)
                            self.select_batida()

                        else:
                            messagebox.showerror('ERRO',
                                                 f'A QUATIDADE EM ESTOQUE E INSUFICIENTE VC TEM \n'
                                                 f' {f} FRENTE \n'
                                                 f' E {c} COSTA \n '
                                                 f'VOCE ESTA QUERENDO REGISTRAR UMA QUANTIDADE DE {self.quantidad} '
                                                 f'PEÇAS '
                                                 f'E NECESSARIO FAZER A REPOSIÇAO DA PARTE FALTANTE ENTRE EM CONTATO'
                                                 f' COM O \n '
                                                 f'LELEUZINHO DE AÇUCA ^^'
                                                 f'\n '
                                                 f'ESTOQUE INSIFICIENTE :( ')
                    except:
                        messagebox.showerror('', 'err')
            else:
                messagebox.showinfo('AVISO', 'NENHUM REGISTRO FOI CADASTRADO')
        self.fechar_comit()

    def treeview_batida_bichinho(self):
        self.cols = (
            'id', 'data', 'lote', 'sublimador', 'cliente', 'seguimento', 'tema', 'modelo', 'tamanho', 'quantidade')

        self.treeview_batida_corpo = ttk.Treeview(self.app3, columns=self.cols, show='headings')

        self.treeview_batida_corpo.column('id', width=8)
        self.treeview_batida_corpo.column('data', width=15)
        self.treeview_batida_corpo.column('lote', width=8)
        self.treeview_batida_corpo.column('sublimador', width=40)
        self.treeview_batida_corpo.column('cliente', width=30)
        self.treeview_batida_corpo.column('seguimento', width=40)
        self.treeview_batida_corpo.column('tema', width=30)
        self.treeview_batida_corpo.column('modelo', width=30)
        self.treeview_batida_corpo.column('tamanho', width=30)
        self.treeview_batida_corpo.column('quantidade', width=30)

        self.treeview_batida_corpo.heading('id', text='ID')
        self.treeview_batida_corpo.heading('data', text='DATA')
        self.treeview_batida_corpo.heading('lote', text='LOTE')
        self.treeview_batida_corpo.heading('sublimador', text='SUBLIMADOR')
        self.treeview_batida_corpo.heading('cliente', text='CLIENTE')
        self.treeview_batida_corpo.heading('seguimento', text='SEGUIMENTO')
        self.treeview_batida_corpo.heading('tema', text='TEMA')
        self.treeview_batida_corpo.heading('modelo', text='MODELO')
        self.treeview_batida_corpo.heading('tamanho', text='TAMANHO')
        self.treeview_batida_corpo.heading('quantidade', text='QTDD')
        self.treeview_batida_corpo.place(x=20, y=440, width=565, height=200)
        self.treeview_batida_corpo.bind("<Double-1>", self.dubloclick_batida)

        self.scrolll = Scrollbar(self.app3, orient=VERTICAL)
        self.scrolll = Scrollbar(self.app3, orient=VERTICAL, command=self.treeview_batida_corpo.yview)
        self.treeview_batida_corpo.configure(yscrollcommand=self.scrolll.set)
        self.scrolll.place(x=595, y=440, width=25, height=200)

    def buscar_corpo_sql(self):

        self.sql()
        self.treeviewcorpobichinho.delete(*self.treeviewcorpobichinho.get_children())
        self.busca_tamanho = self.tamanhoc.get().strip().capitalize()

        self.bd = self.cursor.execute(f"""SELECT id, seguimento, modelo, tamanho, frente, costa 
                                             FROM fantasia WHERE tamanho = '{self.busca_tamanho}' """)

        for Row in self.bd:
            s = list(Row)
            if self.busca_tamanho in s:
                print('ENTROU no if')
                print(s)
                self.resultado = s
                self.treeviewcorpobichinho.insert('', 'end', values=self.resultado)
            else:
                print('ENTROU no else')

    def treeview_busca_corpo(self):
        self.cols = ('id', 'seguimento', 'modelo', 'tamanho', 'frente', 'costa')

        self.treeviewcorpobichinho = ttk.Treeview(self.app3, columns=self.cols, show='headings')

        self.treeviewcorpobichinho.column('id', width=10)
        self.treeviewcorpobichinho.column('seguimento', width=40)
        self.treeviewcorpobichinho.column('modelo', width=30)
        self.treeviewcorpobichinho.column('tamanho', width=30)
        self.treeviewcorpobichinho.column('frente', width=30)
        self.treeviewcorpobichinho.column('costa', width=30)

        self.treeviewcorpobichinho.heading('id', text='ID')
        self.treeviewcorpobichinho.heading('seguimento', text='SEGUIMENTO')
        self.treeviewcorpobichinho.heading('modelo', text='MODELO')
        self.treeviewcorpobichinho.heading('tamanho', text='TAMANHO')
        self.treeviewcorpobichinho.heading('frente', text='FRENTE')
        self.treeviewcorpobichinho.heading('costa', text='COSTA')
        self.treeviewcorpobichinho.place(x=740, y=440, width=400, height=200)

        self.scrolll = Scrollbar(self.app3, orient=VERTICAL)
        self.scrolll = Scrollbar(self.app3, orient=VERTICAL, command=self.treeviewcorpobichinho.yview)
        self.treeviewcorpobichinho.configure(yscrollcommand=self.scrolll.set)
        self.scrolll.place(x=1143, y=440, width=25, height=200)
        self.treeviewcorpobichinho.bind("<Double-1>", self.dubloclick_corpo)

    def menudepartesfantasia(self):
        self.app3.resizable(False, False)
        self.barraMenu = Menu(self.app3)
        self.consulta_exporta = Menu(self.barraMenu, tearoff=0)
        self.consulta_exporta.add_command(label='BICHINHOS', command=self.baterpartesbichinho)
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_separator()
        self.barraMenu.add_cascade(label='PARTES', menu=self.consulta_exporta)

        self.app3.config(menu=self.barraMenu)  # ESTA A BARRA DE MENUS  EAS CONFIGURAÇOES DA TELA APP ####

    def select_batida(self):
        self.pesquisar_venda = self.cursor.execute(
            f""" SELECT id,data_batida, lote, sublimador, cliente,seguimento_s, tema, modelo_s, tamanho_s, quantidade_s
                                                                                   FROM fantasia
                                                                                  WHERE cliente = '{self.cliente}' 
                                                                                  AND data_batida = '{self.data_b}'
                                                                                          """)

        messagebox.showinfo('CADASTRO', 'CADASTRADO COM SUCESSO')

        for linha in self.cursor.fetchall():
            s = list(linha)
            self.pesqui = s
            self.treeview_batida_corpo.insert('', 'end', values=self.pesqui)

    def busca_detalhada(self):
        self.getbatida()
        self.treeviewcorpobichinho.delete(*self.treeviewcorpobichinho.get_children())
        try:
            if self.nome_cliente == '':
                messagebox.showinfo('avisa',
                                    'e nescessario informa o nome do cliente junto com a data da sublimaçao'.upper())
            else:
                self.batida = self.cursor.execute(
                    f"""SELECT ID,seguimento_s, modelo_s, tamanho_s, frente_s,costa_s
                        FROM fantasia WHERE cliente LIKE '{self.nome_cliente}%' AND data_batida = '{self.data_b}' """)
                for linha in self.batida:
                    s = list(linha)
                    self.valor = s
                    self.treeviewcorpobichinho.insert('', 'end', values=self.valor)
        except:
            messagebox.showinfo('','e necessario realizar novamente a'
                                   ' busca pelo cliente e em seguida usa a opçao detalhada'.upper())

    def valorbusca_detalhada(self):
        self.batida = self.cursor.execute(
            f"""SELECT ID,seguimento_s, modelo_s, tamanho_s, frente_s,costa_s
                               FROM fantasia WHERE cliente LIKE '{self.nome_cliente}%' AND data_batida = '{self.data_b}' """)
        for linha in self.batida:
            s = list(linha)
            self.valor = s

            self.treeviewcorpobichinho.insert('', 'end', values=self.valor)

    def messagem_batida_individual(self):
        self.mensagebox = messagebox.showwarning('AVISO', 'para realizar a sublimaçao, \n '
                                                          'e necessario preencher todos os campo corretamente \n '
                                                          'nao pode haver campos em branco'
                                                          f' vc preencheu \n '
                                                          f'id = {self.idd},\n'
                                                          f' sublimador ={self.nome},\n'
                                                          f' data = {self.data_b},\n '
                                                          f'cliente = {self.cliente}, \n '
                                                          f'seguimento = {self.nome} \n'
                                                          f'LOTE = {self.lotee} \n '
                                                          f'modelo = {self.modelo}, \n '
                                                          f'tamanho ={self.tamanho}, \n '
                                                          f'frente = {self.frente}, \n '
                                                          f'costa = {self.costa} \n '
                                                          f', quantidade = {self.quantidad}\n '
                                                          f'TEMA = {self.temaa}'.upper())

    def insert_costa_individual(self):
        self.registrar = self.cursor.execute(
            f"""INSERT INTO fantasia (
                data_batida,lote, sublimador, cliente, seguimento_s, tema ,modelo_s, tamanho_s, costa_s)
                                                VALUES
                ('{self.data_b}', '{self.lotee}', '{self.nome}', '{self.cliente}', '{self.seguimento}', '{self.temaa}', 
                '{self.modelo}', '{self.tamanho}', '{self.quantidad}')""")
        self.update_costa()

    def update_costa(self):
        self.vender = self.cursor.execute(
            f"""UPDATE fantasia SET costa = costa - '{self.quantidad}'WHERE ID = {self.idd} ; """)

    def insert_frente_individual(self):
        self.registrar = self.cursor.execute(
            f"""INSERT INTO fantasia (
            data_batida,lote, sublimador, cliente, seguimento_s, tema, modelo_s, tamanho_s, frente_s
                                   VALUES
            ('{self.data_b}', '{self.lotee}', '{self.nome}', '{self.cliente}', '{self.seguimento}', '{self.temaa}', 
            '{self.modelo}', '{self.tamanho}','{self.quantidad}') """)
        self.update_frente()

    def update_frente(self):
        self.vender = self.cursor.execute(
            f"""UPDATE fantasia SET frente = frente - '{self.quantidad}' WHERE ID = {self.idd} ; """)

    def select_insert_individual(self):
        self.pesquisar_venda = self.cursor.execute(f""" 
                                 SELECT id,data_batida,lote, sublimador, cliente, seguimento_s, tema, modelo_s, tamanho_s, 
                                 quantidade_s
                                                         FROM fantasia
                                                         WHERE cliente = '{self.cliente}' 
                                                         AND data_batida = '{self.data_b}' """)
        messagebox.showinfo('CADASTRO', 'CADASTRADO COM SUCESSO')
        for linha in self.cursor.fetchall():
            s = list(linha)
            self.pesqui = s
            self.treeview_batida_corpo.insert('', 'end', values=self.pesqui)

    def bater_corpo_individual(self):
        self.sql()
        self.treeview_batida_corpo.delete(*self.treeview_batida_corpo.get_children())
        self.getbatida()
        bater = 'Bater'
        bichinho = 'Bichinho'
        idade = 'P' or 'M' or 'G' or 'Gg' or '4 anos' or '6 anos'

        if self.costa == bater and self.frente == bater:
            messagebox.showwarning('AVISO','ESSA AÇÃO SO E PERMITIDA PARA UMA PARTE POR VEZ, \n '
                                                'INFORME A PALAVRA > BATER < NA PARTE QUE DESEJA FAZER A SUBLIMAÇAO ')
        if self.idd == '' or self.data_b == '' or self.nome == '' or self.cliente == '' or self.seguimento == '' or \
                self.modelo == '' or self.tamanho == '' or self.frente == '' or self.costa == '' or \
                self.quantidad == '' or self.lotee == '' or self.temaa == '':
            self.messagem_batida_individual()

        elif self.costa == bichinho and self.frente == bichinho:

            messagebox.showwarning('AVISO', 'ESSA AÇÃO SO E PERMITIDA PARA UMA PARTE POR VEZ, \n '
                                            'INFORME A PALAVRA > BATER < NA PARTE QUE DESEJA FAZER A SUBLIMAÇAO ')

        elif self.costa == bater:
            self.msg1 = messagebox.askyesno(
                        'INFORMAÇÃO', f'DESEJA REGISTRAR {self.quantidad} COSTA NO TAMANHO {self.tamanho} DO CLIENTE '
                                      f'{self.nome}')

            if self.msg1 == TRUE:
                tabela = self.cursor.execute(
                            f"""SELECT frente,costa FROM fantasia WHERE
                                                    seguimento = '{self.seguimento}' AND tamanho = '{self.tamanho}'
                                                                                         AND  ID = {self.idd} """)
                try:
                    for f, c in tabela:
                        if c >= int(self.quantidad):
                            self.insert_costa_individual()
                            self.select_insert_individual()
                        else:
                            messagebox.showerror('ERRO',
                                                    f'A QUATIDADE EM ESTOQUE E INSUFICIENTE VC TEM \n'
                                                    f'  {c} COSTA \n '
                                                    f'VOCE ESTA QUERENDO REGISTRAR UMA QUANTIDADE DE {self.quantidad} '
                                                    f'COSTAS '
                                                    f'E NECESSARIO FAZER A REPOSIÇAO DESSA PARTE ENTRE EM CONTATO'
                                                    f' COM O \n '
                                                    f'LELEUZINHO DE AÇUCA ^^'
                                                    f'\n '
                                                    f'ESTOQUE INSIFICIENTE :( ')
                except:
                    messagebox.showerror('','err')

        elif self.frente == bater:
            self.msg1 = messagebox.askyesno(
                    'INFORMAÇÃO', f'DESEJA REGISTRAR {self.quantidad} FANTASIA NO TAMANHO {self.tamanho} DO CLIENTE '
                                      f'{self.nome}')
            if self.msg1 == TRUE:
                tabela = self.cursor.execute(
                            f"""SELECT frente,id FROM fantasia WHERE
                                                        seguimento = '{self.seguimento}' AND tamanho = '{self.tamanho}'
                                                                                           AND  ID = {self.idd} """)
                try:
                    for f, c in tabela:

                        if f >= int(self.quantidad):
                            self.insert_frente_individual()
                            self.select_insert_individual()
                        else:
                            messagebox.showerror('ERRO',
                                                    f'A QUATIDADE EM ESTOQUE E INSUFICIENTE VC TEM \n'
                                                    f' {f} FRENTE \n' 
                                                    f'VOCE ESTA QUERENDO REGISTRAR UMA QUANTIDADE DE {self.quantidad} '
                                                    f'FRENTE '
                                                    f'E NECESSARIO FAZER A REPOSIÇAO DESSA PARTE ENTRE EM CONTATO'
                                                    f' COM O \n '
                                                    f'LELEUZINHO DE AÇUCA ^^'
                                                         f'\n '
                                                         f'ESTOQUE INSIFICIENTE :( ')
                except:
                    messagebox.showerror('','erro')


            else:
                messagebox.showinfo('AVISO', 'NENHUM REGISTRO FOI CADASTRADO')
        else:
            messagebox.showinfo('','tamsanho b valdo')
        self.fechar_comit()

    def data(self):
        self.date_batida = DateEntry(self.app3, dateformat=3, width=10, background='darkblue', foreground='white',
                                     borderwidth=4, locale='pt_BR', date_pattern='d/m/y', font='TIMES 11 bold')
        self.date_batida.place(x=300, y=10)

    def busca_cliente(self):
        self.sql()
        self.treeview_batida_corpo.delete(*self.treeview_batida_corpo.get_children())
        self.nome_cliente = self.clienteBusca.get()
        self.data_b = self.date_batida.get()

        self.batida = self.cursor.execute(
            f"""SELECT id,data_batida, lote, sublimador, cliente, seguimento_s,tema, modelo_s, tamanho_s, quantidade_s
                FROM fantasia WHERE cliente LIKE '{self.nome_cliente}%' AND data_batida = '{self.data_b}' """)
        for linha in self.batida:
            s = list(linha)
            self.valor = s
            self.treeview_batida_corpo.insert('','end',values=self.valor)

    def dubloclick_corpo(self,event):

        self.treeviewcorpobichinho.selection()
        self.limpar_campo_batida_corpo()
        for v in self.treeviewcorpobichinho.selection():
            print(v)
            col1, col2, col3,col4,col5,col6= self.treeviewcorpobichinho.item(v, 'values')
            self.id.insert(END,col1)
            self.seguimentoB.insert(END, col2)
            self.modeloB.insert(END, col3)
            self.tamanhoB.insert(END, col4)
            self.frenteB.insert(END, col3)
            self.costaB.insert(END, col3)

    def dubloclick_batida(self,event):
        self.treeview_batida_corpo.selection()
        self.limpadoubleclickbatida()
        for v in self.treeview_batida_corpo.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.treeview_batida_corpo.item(v, 'values')
            self.id.insert(END, col1)
            self.nome_sublimador.insert(END,col4)
            self.clienteB.insert(END,col5)
            self.date_batida.insert(END, col2)
            self.temaB.insert(END, col7)
            self.clienteBusca.insert(END, col5)
            self.lote.insert(END, col3)

    def limpar_campo_batida_corpo(self):
        self.id.delete(0,END)
        # self.nome_sublimador.delete(0,END)
        # self.clienteB.delete(0,END)
        self.seguimentoB.delete(0,END)
        self.modeloB.delete(0,END)
        self.tamanhoB.delete(0,END)
        self.frenteB.delete(0,END)
        self.costaB.delete(0,END)
        self.quantidadeB.delete(0,END)

    def limpar_campo_batida_corpo2(self):
        self.limpar_campo_batida_corpo()
        self.treeview_batida_corpo.delete(*self.treeview_batida_corpo.get_children())
        self.treeviewcorpobichinho.delete(*self.treeviewcorpobichinho.get_children())
        self.tamanhoc.delete(0, END)
        self.clienteBusca.delete(0, END)

    def limpadoubleclickbatida(self):
        self.limpar_campo_batida_corpo()
        self.date_batida.delete(0, END)
        self.temaB.delete(0, END)
        self.nome_sublimador.delete(0, END)
        self.clienteB.delete(0, END)
        self.lote.delete(0, END)
        self.clienteBusca.delete(0, END)

    def retirar(self):
        pass

    def sql(self):
        self.conectar = self.conexao_dados = ("Driver={SQL Server};"  # criando a conexao
                                              "Server=DESKTOP-RFPLHG0;"
                                              "Database=seguimentos_cadastrados;")

        self.conexao = pyodbc.connect(self.conectar)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        # self.conexao.close()
        self.cursor.close()

        print('desconectado')

    def fechar_comit(self):
        self.cursor.commit()
        self.desconectar()


class AddPartesBichinho:

    def sql(self):
        self.conectar = self.conexao_dados = ("Driver={SQL Server};"
                                              "Server=DESKTOP-RFPLHG0;"
                                              "Database=seguimentos_cadastrados;")

        self.conexao = pyodbc.connect(self.conectar)
        self.cursor = self.conexao.cursor()

    def desconectar(self):

        self.cursor.close()

        print('desconectado')

    def adicionar_partes_bichinhos(self):
        self.app2 = Toplevel()
        self.app2.title('PARTES BICHINHOS')
        self.app2.geometry('860x400+340+205')
        self.app2.configure(bg='#116185')
        self.app2.resizable(False, False)
        self.app2.focus_force()
        self.app2.grab_set()
        self.app2.transient(app)
        self.combobox_partes()
        self.partes_bichinhos_label()
        self.entrys_adicionar_partes()
        self.treeview_partes_bichinho()
        self.bt_adicionar_partes()

    def partes_bichinhos_label(self):

        self.lab_pesquisa_b = Label(self.app2, text='P E S Q U I S A ', font='times 20 bold', bg='#116185',
                                    fg='YELLOW', relief=FLAT)
        self.lab_pesquisa_b.place(x=70, y=220)

        self.lab_pesquisa_s = Label(self.app2, text='TAMANHO', font='times 13 bold', bg='#116185', fg='YELLOW',
                                    relief=FLAT)
        self.lab_pesquisa_s.place(x=10, y=280)

        self.lab_id_bichinhos = Label(self.app2, text='ID', bg='#116185', font='times 15', fg='white', relief=RAISED)
        self.lab_id_bichinhos.place(x=760, y=20)

        self.lab_seguimento_bichinhos = Label(self.app2, text='SEGUIMENTO', bg='#116185', font='times 15',
                                              fg='white', relief=RAISED)
        self.lab_seguimento_bichinhos.place(x=20, y=40)

        self.lab_modelo_bichinhos = Label(self.app2, text='MODELO', bg='#116185', font='times 15', fg='white',
                                          relief=RAISED)
        self.lab_modelo_bichinhos.place(x=20, y=80)

        self.lab_tamanho = Label(self.app2, text='TAMANHO', bg='#116185', font='times 15', fg='white', relief=RAISED)
        self.lab_tamanho.place(x=20, y=120)

        self.lab_cabelo = Label(self.app2, text='QUANTIDADE', bg='#116185', font='times 15', fg='white', relief=RAISED)
        self.lab_cabelo.place(x=20, y=160)

    def entrys_adicionar_partes(self):

        self.busca_tamanho = Entry(self.app2, width=7, font='times 14')
        self.busca_tamanho.place(x=120, y=280)

        self.entry_id_bichinhos = Entry(self.app2, width=5, font='times 14')
        self.entry_id_bichinhos.place(x=800, y=20)

        self.entry_seguimento_bichinhos = Entry(self.app2, width=15, font='times 14')
        self.entry_seguimento_bichinhos.place(x=165, y=40)

        self.entry_modelo = Entry(self.app2, width=15, font='times 14')
        self.entry_modelo.place(x=165, y=80)

        self.entry_tamanho_bichinhos = Entry(self.app2, width=15, font='times 14')
        self.entry_tamanho_bichinhos.place(x=165, y=120)
        #
        self.entry_quantidade_b = Entry(self.app2, width=15, font='times 14')
        self.entry_quantidade_b.place(x=165, y=160)

    def treeview_partes_bichinho(self):
        self.columns1 = ('id', 'seguimento', 'modelo', 'tamanho', 'quantidade', 'manga', 'capuz', 'carinha')
        self.trevieew_partes = ttk.Treeview(self.app2, columns=self.columns1, show='headings')

        self.trevieew_partes.column('id', width=15)
        self.trevieew_partes.column('seguimento', width=15)
        self.trevieew_partes.column('modelo', width=15)
        self.trevieew_partes.column('tamanho', width=15)
        self.trevieew_partes.column('quantidade', width=15)
        self.trevieew_partes.column('manga', width=30)
        self.trevieew_partes.column('capuz', width=30)
        self.trevieew_partes.column('carinha', width=30)

        self.trevieew_partes.heading('id', text='ID')
        self.trevieew_partes.heading('seguimento', text='Seguimento')
        self.trevieew_partes.heading('modelo', text='Modelo')
        self.trevieew_partes.heading('tamanho', text='Tamanho')
        self.trevieew_partes.heading('quantidade', text='Quantidade')
        self.trevieew_partes.heading('manga', text='Manga')
        self.trevieew_partes.heading('capuz', text='Capuz')
        self.trevieew_partes.heading('carinha', text='Carinha')
        self.trevieew_partes.place(x=270, y=200, height=200, width=570)
        self.trevieew_partes.bind("<Double-1>", self.double_click_partes)

    def bt_adicionar_partes(self):
        self.inserir = PhotoImage(file='image/inserir.png')
        self.bt_adicionar_pt_bichinhos = Button(self.app2, bg='#116185', relief=FLAT, image=self.inserir,
                                                text='INSERIR', command=self.adicionar_partes_sql)
        self.bt_adicionar_pt_bichinhos.place(x=240, y=2)

        self.limpacampo = PhotoImage(file='image/limpacampo.png')
        self.bt_limpar_pt_bichinhos = Button(self.app2, image=self.limpacampo, relief=FLAT, bg='#116185', text='LIMPAR',
                                             command=self.limpa_campos_partes2)
        self.bt_limpar_pt_bichinhos.place(x=350, y=60)

        self.corrigirr = PhotoImage(file='image/corrigir.png')
        self.bt_corrugir_pt_bichinhos = Button(self.app2, bg='#116185', fg='yellow', image=self.corrigirr, relief=FLAT,
                                               compound=LEFT, text='CORRIGIR')
        self.bt_corrugir_pt_bichinhos.place(x=10, y=2)

        self.deleta = PhotoImage(file='image/deletar.png')
        self.bt_deleta_pt_bichinhos = Button(self.app2, image=self.deleta, relief=FLAT, bg='#116185', text='EXCLUIR',
                                             command=self.deletar_bichinhos)
        self.bt_deleta_pt_bichinhos.place(x=180, y=330)

        self.bt_busca_pt_bichinhos = Button(self.app2, text='BUSCA', command=self.busca_partes)
        self.bt_busca_pt_bichinhos.place(x=20, y=330)

        self.adiciona = PhotoImage(file='image/adiciona.png')
        self.bt_adicionar_partes_bichinhos = Button(self.app2, image=self.adiciona, bg='#116185', relief=FLAT,
                                                    text='ADICIONAR', command=self.inserir_partes_fantasia)
        self.bt_adicionar_partes_bichinhos.place(x=795, y=160)

    def busca_partes(self):
        self.sql()
        self.trevieew_partes.delete(*self.trevieew_partes.get_children())
        self.buscabichinho = self.busca_tamanho.get().strip()

        if self.buscabichinho == '':
            self.busca1 = self.cursor.execute(f"""SELECT id,seguimento,modelo,tamanho,
             quantidade ,manga_b,capuz_b,carinha_b FROM fantasia WHERE seguimento='fantasia'
                                                                                        """)
            for linha in self.busca1:
                self.resultado = linha.id, \
                                 linha.seguimento, \
                                 linha.modelo, \
                                 linha.tamanho, \
                                 linha.quantidade, \
                                 linha.manga_b, \
                                 linha.capuz_b, \
                                 linha.carinha_b
                self.trevieew_partes.insert('', 'end', values=self.resultado)

        else:
            busca = self.cursor.execute(f"""SELECT id,seguimento,modelo,tamanho,
             quantidade,manga_b,capuz_b,carinha_b FROM fantasia WHERE seguimento='fantasia'
                                                                       and modelo='bichinho'

                                                                    and  tamanho='{self.buscabichinho}'""")
            for linha in busca:
                self.resultado = linha.id, \
                                 linha.seguimento, \
                                 linha.modelo, \
                                 linha.tamanho, \
                                 linha.quantidade, \
                                 linha.manga_b, \
                                 linha.capuz_b, \
                                 linha.carinha_b
                self.trevieew_partes.insert('', 'end', values=self.resultado)
            self.desconectar()

    def adicionar_partes_sql(self):
        self.sql()
        self.trevieew_partes.delete(*self.trevieew_partes.get_children())

        self.inserir_id_b = int(self.entry_id_bichinhos.get().strip().upper().capitalize())

        self.inserir_seguimeto_b = self.entry_seguimento_bichinhos.get().strip().upper().capitalize()

        self.inserir_modelo_b = self.entry_modelo.get().strip().upper().capitalize()

        self.inserir_tamanho_b = self.entry_tamanho_bichinhos.get().strip().upper().capitalize()

        self.inserir_quantidade_b = int(self.entry_quantidade_b.get().strip().upper().capitalize())

        if self.inserir_id_b == '' or \
                self.inserir_seguimeto_b != 'Fantasia' \
                or self.inserir_modelo_b != 'Bichinho' \
                or self.inserir_tamanho_b == '' or \
                self.inserir_quantidade_b == '':

            self.msg = messagebox.showerror('ERRO !', f'PARA REALIZAR ESSA AÇÃO O SEGUIMENTO DEVE SER  >FANTASIA< \n '
                                                      f'NÃO PODE HAVER VALORES VAZIOS  \n'
                                                      f'VOCÊ ESTA INFOMANDO O SEGUIMENTO COM O NOME\n '
                                                      f' >> {self.inserir_seguimeto_b.upper()}<< \n '
                                                      f'  EO MODELO COM O NOME \n '
                                                      f'>>{self.inserir_modelo_b.upper()} << \n'
                                                      ' E NEM O MODELO PODE SER DIFERENTE DE  \n'
                                                      ' >>> BICHINHO <<<')
        else:
            self.msg = messagebox.askyesno('INSERIR', f'SERÁ INSERIRIDO AS QUANTIDADES\n '
                                                      f'{self.inserir_quantidade_b} PARES EM MANGA BICHINHO,\n '
                                                      f'{self.inserir_quantidade_b} PARES NO CAPUZ BICHINHOS  \n '
                                                      f'{self.inserir_quantidade_b} UN: NA CARINHA BICHINHO NO MODELO '
                                                      f'\n '
                                                      f'{self.inserir_modelo_b} QUE SERÁ REPRESENTADO NO SEGUIMENTO '
                                                      f'{self.inserir_seguimeto_b}\n '
                                                      f'DESEJA CONTINUAR ?')
            if self.msg == True:
                self.cursor.execute(f"""UPDATE FANTASIA SET modelo = '{self.inserir_modelo_b}'
                                                                ,manga_b = {self.inserir_quantidade_b * 2/2},
                                                                capuz_b = {self.inserir_quantidade_b * 2/2},
                                                                carinha_b = {self.inserir_quantidade_b}

                                                                WHERE id ='{self.inserir_id_b}'
                                                                and seguimento ='{self.inserir_seguimeto_b}'
                                                                and tamanho= '{self.inserir_tamanho_b}'                                                                                                    
                                                                                """)
                fantasias = self.cursor.execute(f"""
                SELECT * FROM fantasia where seguimento = '{self.inserir_seguimeto_b}'
                """)
                for linha in fantasias:
                    self.resultado = linha.ID, \
                                     linha.seguimento, \
                                     linha.modelo, \
                                     linha.tamanho, \
                                     linha.quantidade, \
                                     linha.manga_b, \
                                     linha.capuz_b, \
                                     linha.carinha_b
                    self.trevieew_partes.insert('', 'end', values=self.resultado)

                self.cursor.commit()
                self.desconectar()
                messagebox.showinfo('CADASTRO', 'CADASTRO REALIZADO COM SUCESSO')

    def deletar_bichinhos(self):
        self.sql()
        self.msg = messagebox.askyesno('DELETAR', 'DESEJA DELETA O SEGUIMENTO?')
        if self.msg == True:
            self.delet = self.entry_id_bichinhos.get().strip()
            self.dlete = self.cursor.execute(f"""
              DELETE from fantasia where id = {self.delet}
              """)
            messagebox.showinfo('DELETADO', 'SEU REGISTRO FOI DELETADO COM SUCESSO')
        else:
            messagebox.showinfo('CANCELADO', 'NENHUM DADO FOI APAGADO')
        self.cursor.commit()
        self.desconectar()

    def double_click_partes(self, event):
        self.limpa_campos_partes()
        self.trevieew_partes.selection()
        for i in self.trevieew_partes.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.trevieew_partes.item(i, 'values')
            self.entry_id_bichinhos.insert(END, col1)
            self.entry_seguimento_bichinhos.insert(END, col2)
            # self.entry_modelo.insert(END,)
            self.entry_tamanho_bichinhos.insert(END, col4)
            self.entry_quantidade_b.insert(END, col5)

    def limpa_campos_partes(self):
        self.entry_id_bichinhos.delete(0, END)
        self.entry_seguimento_bichinhos.delete(0, END)
        self.entry_modelo.delete(0, END)
        self.entry_tamanho_bichinhos.delete(0, END)
        self.entry_quantidade_b.delete(0, END)
        self.busca_tamanho.delete(0, END)

    def limpa_campos_partes2(self):
        self.limpa_campos_partes()
        self.trevieew_partes.delete(*self.trevieew_partes.get_children())

    def combobox_partes(self):
        self.adicionar_parte = ['MANGA_B', 'CAPUZ_B', 'CARINHA_B','FRENTE', 'COSTA', 'CORPO']
        self.label_adionar = Label(self.app2,text='A D I C I O N A R     P A R T E S ', fg='yellow', bg='#116185',
                                   font='times 12 bold')
        self.label_adionar.place(x=600, y=80)
        self.inserir_partes = ttk.Combobox(self.app2, values=self.adicionar_parte, width=10, font='times 15 bold',
                                           foreground='green')
        self.inserir_partes .place(x=700, y=120)

    def inserir_partes_fantasia(self):
        self.sql()
        self.id = self.entry_id_bichinhos.get().strip().capitalize()
        self.qtdd = self.entry_quantidade_b.get()
        self.seg = self.entry_seguimento_bichinhos.get().strip().capitalize()
        self.re = self.inserir_partes.get().lower()
        try:
            a ='corpo'

            if self.re == a:

                self.msg1 = self.cursor.execute(f"""
                               UPDATE fantasia set frente = frente + {self.qtdd}
                                WHERE seguimento = 'Fantasia'
                                and ID = {self.id}        
                                   """)
                self.msg1 = self.cursor.execute(f"""
                                           update fantasia set costa = costa + {self.qtdd} 
                                           where seguimento = 'Fantasia' and ID = {self.id}        
                                               """)
                messagebox.showinfo('ADICIONADO', f'MAIS {self.qtdd} MANGA FORAM ADICIONADAS COM SUCESSO !')
                self.cursor.commit()
                self.desconectar()
            elif self.re == self.re:
                self.msg= self.cursor.execute(f"""
                    update fantasia set {self.re} = {self.re} + {self.qtdd} where seguimento = 'Fantasia' and ID = 
                        {self.id}
                        """)
                messagebox.showinfo('ADICIONADO',f'MAIS {self.qtdd} MANGA FORAM ADICIONADAS COM SUCESSO !')
                self.cursor.commit()
                self.desconectar()
        except:
            messagebox.showerror('AVISO !!!', 'E NESSECERIO ANTES DE ADICIONAR PARTES DA FANTASIA \n '
                                             'REALIZAR A BUSCA DO SEGUIMENTO DESEJADO E INFORMA AS PARTES QUE DESEJA  '
                                             'ADICIONAR \n '
                                              f'VOCE ESTA  TENTANDO ADICIONAR UM VALOR >>> {self.re} <<<\n'
                                              f'VERIFIQUE SE NAO ESTA INFORMANDO UM VALOR VAZIO \n '
                                              f'OU DIGITOU ALGO ALEM DO PEDIDO NO COMBO')


class CadastroBichinho(AddPartesBichinho):


    def fantasia_bichinho(self):
        self.app1 = Toplevel()
        self.app1.title('ARÉA DE CADASTRO DE FANTASIA BICHINHOS')
        self.app1.geometry('600x500+290+56')
        self.app1.resizable(False, False)
        self.app1.transient(app)
        self.app1.focus_force()
        self.app1.grab_set()
        self.app1.configure(bg='#2a2a29')
        self.menu_bichinhos()
        self.entrys_cadastra_bichinhos()
        self.label_cadastra_bichinhos()
        self.treview_cadastro_bichinhos()
        self.botoes_cadastro_bichinho()

    def cadastrar_bichinhos(self):
        self.sql()
        try:
            self.treeview_bichinhos.delete(*self.treeview_bichinhos.get_children())
            self.c_seguimento = self.seguimento_bicinhos.get().strip().lower().capitalize()
            self.c_tamanho = self.tamanho_bicinhos.get().strip().lower().capitalize()
            self.c_quantidade = int(self.quantidade_bicinhos.get().lower().strip().capitalize())

            if self.c_seguimento != 'Fantasia' or self.c_tamanho == '' or self.c_quantidade == '':
                messagebox.showerror('ATENÇÃO !!', 'ESSA ÁREA SÓ É VALIDA PARA O SEGUIMENTO   >>> FANTASIA <<<\n'
                                                  'E OS CAMPOS DEVEM SER PREENCHIDOS COM O TAMANHO X\n'
                                                  'EA QUANTIDADE X CORRETA EM LETRAS MINUSCULAS, \n'
                                                  'VOCÊ ESTÁ INFORMANDO OS VALORES \n '
                                                  f'SEGUIMENTO= {self.c_seguimento.upper()} \n'
                                                  f'TAMANHO = {self.c_tamanho.upper()} \n'
                                                  f'QUANTIDADE = {self.c_quantidade}  \n'
                                                  f'VERIFIQUE OS VALORES SE ESTÃO CORRETOS OU A ERRO NA DIGITAÇAO\n '
                                                  f'NAO PODE CONTER ESPAÇOS VAZIOS')

            else:
                mensagem_cadastro_bichinhos = messagebox.askyesno(
                    'CADASTAR', F'DESEJA CADASTRAR O SEGUIMENTO {self.c_seguimento} ?')

                if mensagem_cadastro_bichinhos == True:
                    c_bichinho = self.cursor.execute(f"""INSERT INTO fantasia(seguimento,tamanho,frente,costa)
                                                                             VALUES
                                                                              ('{self.c_seguimento}',
                                                                               '{self.c_tamanho}',
                                                                               '{self.c_quantidade}',
                                                                               '{self.c_quantidade}'
                                                                               
                                                                                                  )""")
                    messagebox.showinfo('CADASTRADO','CADASTRO REALIZADO COM SUCESSO')

                    self.vizualizar_cadastro_bichinhos = self.cursor.execute(f"""SELECT * FROM fantasia
                                                                                WHERE seguimento ='{self.c_seguimento}'
                                                                                """)
                    for valor in self.vizualizar_cadastro_bichinhos:
                        self.v = valor.quantidade, valor.seguimento, valor.tamanho, valor.frente, valor.costa, \
                                valor.carinha_b, valor.manga_b, valor.capuz_b
                        self.treeview_bichinhos.insert('','end',values=self.v)

                    self.cursor.commit()
                    self.desconectar()
                else:
                    messagebox.showerror('CANCELADO', 'NENHUM VALOR SERÁ CADASTRADO')
        except:
            messagebox.showerror('ERRO !','PARA REALIZAR O CADASTRO E NECESSÁRIO INFORMAR OS VALORES CORRETAMENTE')

    def entrys_cadastra_bichinhos(self):
        self.id_bicinhos = Entry(self.app1, font='times 15', width=4)
        self.id_bicinhos.place(x=550, y=20)

        self.seguimento_bicinhos = Entry(self.app1, font='times 15', width=15)
        self.seguimento_bicinhos.place(x=150, y=20)

        self.tamanho_bicinhos = Entry(self.app1, font='times 15', width=8)
        self.tamanho_bicinhos.place(x=140, y=60)

        self.quantidade_bicinhos = Entry(self.app1, font='times 15', width=8)
        self.quantidade_bicinhos.place(x=140, y=100)

        self.busca_bicinhos = Entry(self.app1, font='times 15', width=15)
        self.busca_bicinhos.place(x=180, y=280)

    def label_cadastra_bichinhos(self):
        self.label_id_bichinho = Label(self.app1, text='ID', font=FLAT, width=3, bg='#2a2a29', fg='white')
        self.label_id_bichinho.place(x=510, y=20)

        self.label_bicinhos = Label(self.app1, text='SEGUIMENTO', font=FLAT, width=13, bg='#2a2a29', fg='white')
        self.label_bicinhos.place(x=17, y=20)

        self.label_tema_bicinhos = Label(self.app1, text='TAMANHO', font=FLAT, width=13, bg='#2a2a29', fg='white')
        self.label_tema_bicinhos.place(x=8, y=60)

        self.label_descricao_bicinhos = Label(self.app1, text='QUANTIDADE', font=FLAT, width=13, bg='#2a2a29',
                                              fg='white')
        self.label_descricao_bicinhos.place(x=15, y=100)

        self.label_busca_bicinhos = Label(self.app1, text='FANTASIA', font='times 14 bold', relief=RAISED, width=13,
                                          bg='#2a2a29', fg='white')
        self.label_busca_bicinhos.place(x=15, y=280)

    def botoes_cadastro_bichinho(self):

        self.img_cadastro = PhotoImage(file='image/cadastrar.png')
        self.bt_cadastrar_bichinho = Button(self.app1, text='CADASTRAR', image=self.img_cadastro, compound=TOP,
                                            fg='#421212', font='bold', command=self.cadastrar_bichinhos)
        self.bt_cadastrar_bichinho.place(x='230', y='60')

        self.bt_corrigir_bichinho = Button(self.app1, text='CORRIGIR', fg='#421212', font='bold',
                                           command=self.corrigir_cadastro_bichinhos)
        self.bt_corrigir_bichinho.place(x='320', y='20')

        self.pes_img = PhotoImage(file='image/busca.png')
        self.bt_busca_bichinho = Button(self.app1, fg='#421212', font='bold', image=self.pes_img, compound=TOP,
                                        command=self.pesquisa_cadastro_bichinhos)
        self.bt_busca_bichinho.place(x='350', y='280')

        self.limpatela = PhotoImage(file='image/limpa_tela.png')
        self.bt_limpa_bichinho = Button(self.app1, text='LIMPAR', fg='#421212', font='bold',
                                        image=self.limpatela, compound= LEFT, command=self.limpa_tudo_bichinho)
        self.bt_limpa_bichinho.place(x='20', y='140')

    def limpa_campo_bichinhos(self):
        self.limpa_id = self.id_bicinhos.delete(0, END)
        self.limpa_seguimento = self.seguimento_bicinhos.delete(0, END)
        self.limpa_tamanho = self.tamanho_bicinhos.delete(0, END)
        self.lipa_quantidade = self.quantidade_bicinhos.delete(0, END)
        self.limpa_busca_bichinhos = self.busca_bicinhos.delete(0, END)

    def limpa_tudo_bichinho(self):
        self.limpa_campo_bichinhos()
        self.treeview_bichinhos.delete(*self.treeview_bichinhos.get_children())

    def treview_cadastro_bichinhos(self):
        self.columns = ('ID','quantidade', 'seguimento', 'tamanho', 'frente', 'costas', 'carinha', 'manga', 'capuz')
        self.treeview_bichinhos = ttk.Treeview(self.app1, columns=self.columns, show='headings')

        self.treeview_bichinhos.column('ID', width=5)
        self.treeview_bichinhos.column('quantidade', width=5)
        self.treeview_bichinhos.column('seguimento', width=30)
        self.treeview_bichinhos.column('tamanho', width=30)
        self.treeview_bichinhos.column('frente', width=30)
        self.treeview_bichinhos.column('costas', width=30)
        self.treeview_bichinhos.column('carinha', width=30)
        self.treeview_bichinhos.column('manga', width=30)
        self.treeview_bichinhos.column('capuz', width=30)

        self.treeview_bichinhos.heading('ID', text='ID')
        self.treeview_bichinhos.heading('quantidade', text='QTDDS')
        self.treeview_bichinhos.heading('seguimento', text='Seguimento')
        self.treeview_bichinhos.heading('tamanho', text='Tamanho')
        self.treeview_bichinhos.heading('frente', text='Frente')
        self.treeview_bichinhos.heading('costas', text='Costas')
        self.treeview_bichinhos.heading('carinha', text='Carinha')
        self.treeview_bichinhos.heading('manga', text='Manga')
        self.treeview_bichinhos.heading('capuz', text='Capuz')

        self.treeview_bichinhos.place(x=10, y=350, width=500, height=200)
        self.scrol_bich = Scrollbar(self.app1, orient=VERTICAL)
        self.scrol_bich = Scrollbar(self.app1, orient=VERTICAL, command=self.treeview_bichinhos.yview)
        self.treeview_bichinhos.configure(yscrollcommand=self.scrol_bich.set)
        self.scrol_bich.place(x=512, y=352, width=19, height=149)
        self.treeview_bichinhos.bind("<Double-1>", self.double_click_bichinhos)

    def menu_bichinhos(self):
        self.menu_bichinho = Menu(self.app1)
        self.menubichinho = Menu(self.menu_bichinho, tearoff=0)
        self.menubichinho.add_command(label='BICHINHOS',command=self.adicionar_partes_bichinhos)
        self.menubichinho.add_separator()
        self.menubichinho.add_command(label='HEROIS')
        self.menubichinho.add_separator()
        self.menu_bichinho.add_cascade(label='ADICIONAR PARTES', menu=self.menubichinho)
        self.menubichinho.add_separator()
        self.app1.config(menu=self.menu_bichinho)  # ESTA A BARRA DE MENUS  EAS CONFIGURAÇOES DA TELA APP ####

    def pesquisa_cadastro_bichinhos(self):
        self.sql()
        self.treeview_bichinhos.delete(*self.treeview_bichinhos.get_children())
        self.buscar_area_cadastro = self.busca_bicinhos.get().strip().capitalize()

        if self.buscar_area_cadastro == '':
            messagebox.showinfo('', 'SERA MOSTRADO TODOS OS CADASTROS DISTINTOS\n'
                                   'PARA REALIZAR UMA CONSULTA EXPECIFICA INFORME O TAMANHO')

            self.fantasia_cad = self.cursor.execute("""SELECT DISTINCT * FROM fantasia
                                                                       """)
            for linha in self.fantasia_cad:
                self.f = linha.ID,linha.quantidade, linha.seguimento, linha.tamanho,\
                         linha.frente,\
                         linha.costa,\
                         linha.manga_b,\
                         linha.capuz_b,\
                         linha.carinha_b
                self.treeview_bichinhos.insert('', 'end', values=self.f)

        else:
            self.fantasia_cad1 = self.cursor.execute(f"""SELECT * FROM fantasia
                                                                WHERE tamanho = '{self.buscar_area_cadastro}'
                                                                """)
            for linha in self.fantasia_cad1:
                print(linha)

                if self.buscar_area_cadastro in linha:
                    self.res = linha.ID, linha.quantidade, linha.seguimento, linha.tamanho, linha.frente, linha.costa, \
                               linha.carinha_b, linha.manga_b, linha.capuz_b
                    self.treeview_bichinhos.insert('', 'end', values=self.res)
                else:
                    messagebox.showwarning('',f'O TAMANHO {self.buscar_area_cadastro} NAO ESTA CADASTRADO')

    def selecao_bichinho(self):
        self.sql()
        self.corrigir1 = self.cursor.execute(
            f"""SELECT * from fantasia""")
        for linha in self.corrigir1:
            self.valores = linha.ID,linha.quatidade, linha.seguimento, linha.modelo, linha.tamanho, \
                           linha.manga_b, linha.capuz_b, linha.carinha_b,
        self.desconectar()

    def corrigir_cadastro_bichinhos(self):
        self.sql()
        self.corrigirr_id = self.id_bicinhos.get()
        self.corrigirr_seguimento = self.seguimento_bicinhos.get().strip().capitalize()
        self.corrigirr_tamanho = self.tamanho_bicinhos.get().strip().capitalize()
        self.corrigirr_quantidade = self.quantidade_bicinhos.get().strip().capitalize()

        if self.corrigirr_id == '' or self.corrigirr_seguimento == '' or self.corrigirr_tamanho == '' \
                or self.corrigirr_quantidade == '':
            messagebox.showwarning('AVISO!', 'PARA REALIZAR A CORREÇAO DE QUAL QUER CAMPO E NECESSARIO\n'
                                             ' INFORMAR CORRETAMENTE OS VALORES EM TODOS OS CAMPOS')
        else:
            correcao = messagebox.askyesno(
                'ALTERAÇAO', f'DESEJAR REALIZA A ALTERAÇAO INFORMADA PARA O SEGUIMENTO {self.corrigirr_seguimento}')
            if correcao == True:

                self.corrigir1 = self.cursor.execute(
                    f"""UPDATE fantasia SET frente = '{self.corrigirr_quantidade}',
                                   costa = '{self.corrigirr_quantidade}'
                                    WHERE ID = '{self.corrigirr_id}'""")

                self.corrigir2 = self.cursor.execute(
                    f"""SELECT * from fantasia where seguimento= '{self.corrigirr_seguimento}' """)

                for linha in self.corrigir2:
                    self.valores = linha.ID, linha.quantidade, linha.seguimento, linha.tamanho, linha.frente, \
                                   linha.costa, linha.carinha_b, linha.manga_b, linha.capuz_b,
                    self.treeview_bichinhos.delete(*self.treeview_bichinhos.get_children())
                    self.treeview_bichinhos.insert('', 'end', values=self.valores)
                    self.cursor.commit()
                    messagebox.showinfo('', 'ALTERAÇAO REALIZADA COM SUCESSO')
            else:
                messagebox.showinfo('', 'NENHUMA ALTERAÇAO FOI REALIZADA')
                self.limpa_campo_bichinhos()

    def double_click_bichinhos(self, event):
        self.treeview_bichinhos.selection()
        self.limpa_campo_bichinhos()
        for v in self.treeview_bichinhos.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.treeview_bichinhos.item(v, 'values')
            self.id_bicinhos.insert(END, col1)
            self.seguimento_bicinhos.insert(END, col3)
            self.tamanho_bicinhos.insert(END, col4)
            self.quantidade_bicinhos.insert(END, col2)


class Master (CadastroBichinho, CorpoBichinho):


    def __init__(self):
        self.app = app
        self.menu_cadatros()
        self.cor_treeview()
        self.tela()
        self.frame_busca()
        self.frame_producao()
        self.label_producao()
        self.busca_data_producao()
        self.botaoes_app()
        self.entrys_producao()
        self.entrys_pesquisa()
        self.label_pesquisa()
        self.treeview_producao()
        self.treeview_app()


        app.mainloop()

    def menu_cadatros(self):

        self.barraMenu = Menu(self.app)
        self.consulta_exporta = Menu(self.barraMenu, tearoff=0)
        self.consulta_exporta.add_command(label='FANTASIA',command=self.fantasia_bichinho)
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='BICHINHOS')
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='VESTIDO TRAPEZIO')
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='CAMISA MAURICINHO')
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='SHORTE MAURICINHO')
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='REPOSIÇOES')
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='PARTES QUE FALTAM')
        self.consulta_exporta.add_separator()
        self.consulta_exporta.add_command(label='FECHAR O SISTEMA')
        self.consulta_exporta.add_separator()
        self.barraMenu.add_cascade(label='AREA DE CADASTROS',menu=self.consulta_exporta)

        self.app.config(menu=self.barraMenu)  # ESTA A BARRA DE MENUS  EAS CONFIGURAÇOES DA TELA APP ####

    def cor_treeview(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",

                        foreground="#000000",
                        rowheight=20,
                        fieLdbackground="silver"
                        )
        # COR DA SELEÇAO DO TRIVIEW

        style.map("Treeview",
                  background=[('selected', 'GREEN')])

    def sql(self):
        self.conectar = self.conexao_dados = ("Driver={SQL Server};"  # criando a conexao
                                              "Server=DESKTOP-RFPLHG0;"
                                              "Database=seguimentos_cadastrados;")

        self.conexao = pyodbc.connect(self.conectar)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        # self.conexao.close()
        self.cursor.close()

        print('desconectado')

    def tela(self):
        self.app.geometry('1350x700+01+3')
        self.app.configure(bg='#421212')
        self.busca_data_producao()
        self.photo = PhotoImage(file='image/sistema.png')
        self.photo.subsample(0, 1)

        self.l_photo = Label(self.app, image=self.photo, background='#421212')
        self.l_photo.place(x=700, y=200)

        # FRAME SUPERIOR DA TELA APP

    def frame_busca(self):
        self.frame_b = Frame(self.app, width=800, height=200, borderwidth=9, relief="raised", bg='#421212',
                             highlightthickness=2)
        self.frame_b.place(x=30, y=10)
        # FRAME LADO DIREITO DA AREEA DE PRODÇAO

    def frame_producao(self):
        self.frame_p = Frame(self.app, width=400, height=600,
                             borderwidth=9, relief="raised", bg='#421212', highlightthickness=2)
        self.frame_p.place(x=940, y=80)

        # funçao data pesquisa produçao

        # PARTE LADO DIREITO DA AREEA DE PRODÇAO

    def label_producao(self):
        self.l_nome = Label(self.app, text='CONSULTA DE PRODUÇÃO', font='times 23', relief=FLAT, bg='#421212',
                            fg='WHITE')
        self.l_nome.place(x=940, y=30)

        self.data_inicio = Label(self.app, text='INICIO', font='times 17', bg='#421212', fg='WHITE',
                                 highlightthickness=2)
        self.data_inicio.place(x=960, y=100)

        self.data_final = Label(self.app, text='FINAL', font='times 17', bg='#421212', fg='WHITE',
                                highlightthickness=2)
        self.data_final.place(x=960, y=160)

        self.l_seguimento = Label(self.app, text='SEGUIMENTO',
                                  font='times 14',
                                  relief=FLAT,
                                  bg='#421212', fg='WHITE')
        self.l_seguimento.place(x=960, y=260)

        self.l_tamanho = Label(self.app, text='TAMANHO', font='times 14', relief=FLAT, bg='#421212', fg='WHITE')
        self.l_tamanho.place(x=960, y=310)

        # FRAME LADO DIREITO DA AREEA DE PESQUISA

    def label_pesquisa(self):
        self.lab_seguimento = Label(self.app, text='SEGUIMENTO',
                                    font='times 20',
                                    relief=FLAT, bg='#421212',
                                    fg='WHITE')

        self.lab_seguimento.place(x=50, y=280)

        self.lab_tamanho = Label(self.app, text='TAMANHO', font='times 20', relief=FLAT, bg='#421212', fg='WHITE')

        self.lab_tamanho.place(x=50, y=340)

    def entrys_pesquisa(self):
        self.entry_app_seguimento = Entry(self.app, font='times 15')
        self.entry_app_seguimento.focus_force()
        self.entry_app_seguimento.place(x=250, y=285)

        self.entry_app_tamanho = Entry(self.app, font='times 15', width=10)
        self.entry_app_tamanho.place(x=250, y=345)

    def botaoes_app(self):
        # pesquisa data inicio-fim
        self.img = PhotoImage(file='image/pesquisa.png')
        self.busca = Button(self.app, image=self.img)
        self.busca.place(x=1230, y=130)

        # soma a quantidade de peças batidas
        self.soma = Button(self.app, text='SOMA', bg='ORANGE')
        self.soma.place(x=1130, y=210)

        # pesuisa o seguimento e tamanho da produçao
        self.img_b = PhotoImage(file='image/pesquisa.png')
        self.busca_seg = Button(self.app, image=self.img_b)
        self.busca_seg.place(x=1190, y=290)

        self.ftfantasia = PhotoImage(file='image/fantasia.png')
        self.bt_fantasia = Button(self.app, image=self.ftfantasia, bg='#421212',command=self.tela_bichinho)
        self.bt_fantasia.place(x=40, y=20)

        self.img_pes = PhotoImage(file='image/pesquisa.png')
        self.busca_pes = Button(self.app, image=self.img_b,command=self.quantidade_fantasia)

        self.busca_pes.place(x=360, y=320)

    def quantidade_fantasia(self):
        self.sql()
        self.treeview.delete(*self.treeview.get_children())
        quantidade = self.cursor.execute(
            """SELECT seguimento, tamanho, frente, costa, manga_b, capuz_b, carinha_b FROM fantasia
            """)
        for linha in quantidade:
            self.quantidades = linha.seguimento, linha.tamanho, \
                               linha.frente, linha.costa, linha.manga_b, linha.capuz_b, linha.carinha_b
            self.treeview.insert('', 'end', values=self.quantidades)
        self.desconectar()

    def busca_data_producao(self):
        self.date_inicio = DateEntry(self.app, dateformat=3, width=10, background='darkblue', foreground='white',
                                     borderwidth=4, locale='pt_BR', date_pattern='d/m/y', font='TIMES 11 bold')
        self.date_inicio.place(x=1080, y=105)

        self.date_final = DateEntry(self.app, dateformat=3, width=10, background='darkblue', foreground='white',
                                    borderwidth=4, locale='pt_BR', date_pattern='d/m/y', font='TIMES 11 bold')
        self.date_final.place(x=1080, y=165)

    def entrys_producao(self):
        self.entry_seguimento = Entry(self.app, font='times 15', width=18)
        self.entry_seguimento.place(x=1100, y=260)

        self.entry_tamanho = Entry(self.app, font='times 15', width=8)
        self.entry_tamanho.place(x=1100, y=310)

    def treeview_producao(self):
        self.columns = ('seguimento', 'tema', 'quantidade')
        self.treeview = ttk.Treeview(self.app, columns=self.columns, show='headings')

        self.treeview.heading('seguimento', text='Seguimento')
        self.treeview.heading('tema', text='Tema')
        self.treeview.heading('quantidade', text='Quantidade')

        self.treeview.column('seguimento', width=80)
        self.treeview.column('tema', width=80)
        self.treeview.column('quantidade', width=50)
        self.treeview.place(x=950, y=380, width=345, height=290)
        self.scrolll = Scrollbar(self.app, orient=VERTICAL)
        self.scrolll = Scrollbar(self.app, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrolll.set)
        self.scrolll.place(x=1300, y=380, width=25, height=290)

    def treeview_app(self):
        self.columns = ('seguimento', 'tamanho', 'frente', 'costas', 'manga', 'capuz', 'carinha')
        self.treeview = ttk.Treeview(self.app, columns=self.columns, show='headings')

        self.treeview.heading('seguimento', text='Seguimento')
        self.treeview.heading('tamanho', text='Tamanho')
        self.treeview.heading('frente', text='Frente')
        self.treeview.heading('costas', text='Costa')
        self.treeview.heading('manga', text='Manga')
        self.treeview.heading('capuz', text='Capuz')
        self.treeview.heading('carinha', text='Carinha')

        self.treeview.column('seguimento', width=80)
        self.treeview.column('tamanho', width=80)
        self.treeview.column('frente', width=180)
        self.treeview.column('costas', width=180)
        self.treeview.column('manga', width=180)
        self.treeview.column('capuz', width=50)
        self.treeview.column('carinha', width=50)
        self.treeview.place(x=10, y=380, width=895, height=300)
        self.scrolll = Scrollbar(self.app, orient=VERTICAL)
        self.scrolll = Scrollbar(self.app, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrolll.set)
        self.scrolll.place(x=910, y=380, width=25, height=300)


Master()

