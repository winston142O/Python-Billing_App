# imports #

from email import message
from tkinter import *
from turtle import bgcolor
from fpdf import FPDF
from matplotlib.colors import cnames
import math,random, os
from tkinter import messagebox
import subprocess

class Bill_App:
    def __init__(self, root):
    # window conf 
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Factuas SJ")
        bg_color="#074463"
        title=Label(self.root,text="SJ Asesores de Seguros",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)        
        
    # variables 
        # seguros humano #
            # salud #
        self.esencial_plus=IntVar()
        self.superior=IntVar()
        self.royal=IntVar()
        self.max=IntVar()
        self.prime=IntVar()
        self.platinum=IntVar()
        self.healthplan=IntVar()
            # vehiculos #
        self.miautobasico=IntVar()
        self.miautopremier=IntVar()
        self.miautoflex=IntVar()
        self.miautomotobasico=IntVar()
        self.miautofull=IntVar()  
        # seguros atlantica #
            # salud
        self.orion=IntVar()
        self.orion_plus=IntVar()
        self.guardian=IntVar()
        self.guardian_plus=IntVar()
        self.vida_credito=IntVar()
        self.vida_beca=IntVar()
        self.vida_grupo=IntVar()
        self.acc_pers=IntVar()
        self.autoatlanta_basico=IntVar()
        self.autoatlanta_ultra=IntVar()
        self.atlantico_rentacar=IntVar()
        self.atlantico_total=IntVar()
        self.atlantico_totalplus=IntVar()
        self.atlanta_vip=IntVar()
        self.atlanta_0km=IntVar()
        self.atlanta_seriem=IntVar()
        self.atlanta_economax=IntVar()
        self.atlanta_taxirenta=IntVar()
        self.motoresatlanta_basico=IntVar()
        self.motoresatlanta_deportivo=IntVar()
        self.motoresatlanta_totalplus=IntVar()
        # product total price #
        self.product1_price=StringVar()
        self.product2_price=StringVar()
        self.product3_price=StringVar()
        # product tax #
        self.product1_tax=StringVar()
        self.product2_tax=StringVar()
        self.product3_tax=StringVar()
        # cliente #
        self.c_name=StringVar()
        self.date=StringVar()        
        self.c_phone=StringVar()        
        x=random.randint(1000,9999) # random bill_no for testing purposes
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        self.paym=StringVar()
        self.bamnt=StringVar()
              
    # detalles de factura 
    
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Detalles de factura",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=169,width=970,height=100)
        
        date_lbl=Label(F1,text="Fecha",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=0,column=0,padx=20,pady=5)
        date_txt=Entry(F1,width=15,textvariable=self.date,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        pay_lbl=Label(F1,text="Forma de pago",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=0,column=2,padx=20,pady=5)
        pay_txt=Entry(F1,width=15,textvariable=self.paym,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
    
        bamnt_lbl=Label(F1,text="Monto",bg=bg_color,fg="white", font=("times new roman",12,"bold")).grid(row=0,column=4,padx=20,pady=5)
        bamnt_txt=Entry(F1,width=15,textvariable=self.bamnt,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
    
    # detalles de cliente 
    
        F_1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Detalles del cliente",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F_1.place(x=0,y=71,relwidth=1)
        
        cname_lbl=Label(F_1,text="Nombre",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F_1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F_1,text="Número de teléfono",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F_1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(F_1,text="Nombre de factura",bg=bg_color,fg="white", font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F_1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F_1,text="Buscar",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
                                      
    # fila de seguros Humano
    
        # humano info functions #
        def esenc_plus_info():
            messagebox.showinfo("Esencial Plus", (
                "Planes privados a través de los cuales ponemos a tu alcance los servicios de salud que tanto tú como los tuyos necesitan. Se encuentran dirigidos principalmente a los trabajadores del sector informal, pequeñas y medianas empresas."                     
                )
            )
            
        def esenc_plus_cover1():
            messagebox.showinfo("Esencial Plus", (                
                "***Coberturas Ambulatorias***"+
                "\n"+
                f"\nConsultas Ambulatorias - Ilimitado. Pago diferencia por consulta"+
                "\n"+
                f"\nLaboratorios y Rayos X - 70% (ilimitado)"+
                "\n"+
                f"\nVacunas - 80% hasta los 10 años"+
                "\n"+
                f"\nTerapias Físicas - 80% LH* (6 por año)"+
                "\n"+
                f"\nConsultas psicológicas y psiquiátricas - 80% (5 por año) "+
                "\n"+
                f"\nProcedimientos ambulatorios - 60% (ilimitado)"+
                "\n"+
                f"\nEstudios Especiales - 70% LH* (ilimitado)"+
                "\n"+
                f"\nEmergencias - 100% dentro de la red (80% en caso de urgencias médicas)")
            )
            
        def esenc_plus_cover2():
            messagebox.showinfo("Esencial Plus", (
                "***Coberturas de Hospitalización***"+
                "\n"+
                f"\nHabitación - 100% (RD$2,600 por día/ilimitado)"+
                "\n"+
                f"\nMedicinas en internamiento - 100% (RD$1,500 por día/ilimitado)"+
                "\n"+
                f"\nSala de cirugía - 80% LH*"+
                "\n"+
                f"\nAnestesia y material gastable - 100% (ilimitado)"+
                "\n"+
                f"\nHonorarios Médicos - 100% LH*"+
                "\n"+
                f"\nLaboratorios y Rayos X - 80% LH*"+
                "\n"+
                f"\nEstudios Especiales - 80% LH*"+
                "\n"+
                f"\nSala de cuidados intensivos - 100% (RD$2,000 por día / ilimitado)"
                )
            )
            
        def esenc_plus_cover3():
            messagebox.showinfo("Esencial Plus", (
                "***Coberturas de Maternidad***"+
                "\n"+
                f"\nParto Normal - 70% LH*"+
                "\n"+
                f"\nCesárea - 70% LH*"+
                "\n"+
                f"\nNiños Recien Nacidos - 70% LH*"        
                )
            )
        
        def esenc_plus_cover4():
            messagebox.showinfo("Esencial Plus", (
                "***Otras Coberturas***"+
                "\n"+
                f"\nGasto Médico Mayor - 70% LH*"+
                "\n"+
                f"\nÚltimos Gastos - 70% LH*"+
                "\n"+
                f"\nAmbulancia Terrestre - 70% LH*"+
                "\n"+
                f"\nPlan Odontológico- 70% LH*"+
                "\n"+
                f"\nLímite por caso - 70% LH*"         
                )
            )

        def superior_info():
            messagebox.showinfo("Superior", (
                "Plan privado a través del cual ponemos a tu alcance los servicios de salud que tanto tú como los tuyos necesitan. Cuentas con una amplia cobertura local en aten​​ción ambulatoria, procedimientos diagnósticos, ​servicios de hospitalización, cirugías y parto, así como acceso directo a la prestigiosa red de prestadores de servicios de salud contratada por Humano."                     
                )
            )
            
        def superior_cover1():
            messagebox.showinfo("Superior", (                
                "***Coberturas Ambulatorias***"+
                "\n"+
                f"\nConsultas Ambulatorias - Ilimitado. Pago diferencia por consulta"+
                "\n"+
                f"\nLaboratorios y Rayos X - 80% LH* (ilimitado)"+
                "\n"+
                f"\nVacunas - 80% hasta los 10 años (dentro de la red)*"+
                "\n"+
                f"\nTerapias Físicas - 80% LH* (12 por año)"+
                "\n"+
                f"\nConsultas psicológicas y psiquiátricas - 80% LH* (10 por año)"+
                "\n"+
                f"\nProcedimientos ambulatorios - 80% LH*"+
                "\n"+
                f"\nEstudios Especiales - 70% LH* (ilimitado)"+
                "\n"+
                f"\nEmergencias - 100% dentro de la red (80% en caso de urgencia médica).")
            )
            
        def superior_cover2():
            messagebox.showinfo("Superior", (
                "***Coberturas de Hospitalización***"+
                "\n"+
                f"\nHabitación - 100% (RD$3,000 por día/ilimitado)"+
                "\n"+
                f"\nMedicinas en internamiento - 100% (RD$3,000 por día/ilimitado)"+
                "\n"+
                f"\nSala de cirugía - 100% LH*"+
                "\n"+
                f"\nAnestesia y material gastable - 100% LH*"+
                "\n"+
                f"\nHonorarios Médicos - 100% LH*"+
                "\n"+
                f"\nLaboratorios y Rayos X - 100% LH*"+
                "\n"+
                f"\nEstudios Especiales - 100% LH*"+
                "\n"+
                f"\nSala de cuidados intensivos - 100% (RD$4,000 por día/ilimitado)"
                )
            )
            
        def superior_cover3():
            messagebox.showinfo("Superior", (
                "***Coberturas de Maternidad***"+
                "\n"+
                f"\nParto Normal - 100% LH*"+
                "\n"+
                f"\nCesárea - 100% LH*"+
                "\n"+
                f"\nNiños Recien Nacidos - 100% (hasta RD$125,000)"        
                )
            )
        
        def superior_cover4():
            messagebox.showinfo("Superior", (
                "***Otras Coberturas***"+
                "\n"+
                f"\nGasto Médico Mayor - RD$750,000 por año"+
                "\n"+
                f"\nEnfermedades Mayores - RD$50,000"
                "\n"+
                f"\nÚltimos Gastos - RD$50,000"+
                "\n"+
                f"\nSeguro de vida (Titular) - RD$100,000"
                "\n"+
                f"\nAmbulancia Terrestre - Incluido"+
                "\n"+
                f"\nPlan Odontológico- Dental Humano"+
                "\n"+
                f"\nLímite por caso - RD$300,000"         
                )
            )
        
        def royal_info():
            messagebox.showinfo("Royal", (
                "Plan privado a través del cual ponemos a tu alcance los servicios de salud que tanto tú como los tuyos necesitan. Cuentas con una amplia cobertura local en atención ambulatoria, procedimientos diagnósticos, servicios de hospitalización, cirugías y parto, obteniendo acceso directo a la prestigiosa red de prestadores de servicios de salud contratada por Humano."                     
                )
            )
        
        def royal_cover1():
            messagebox.showinfo("Royal", (                
                "***Coberturas Ambulatorias***"+
                "\n"+
                f"\nConsultas Ambulatorias - Ilimitado. Pago diferencia por consulta"+
                "\n"+
                f"\nLaboratorios y Rayos X - 80% (ilimitado)"+
                "\n"+
                f"\nVacunas - 80% hasta los 10 años (en centros afiliados dentro de la red)*"+
                "\n"+
                f"\nTerapias Físicas - 80% LH* (20 por año)"+
                "\n"+
                "\n"+
                f"\nTerapias del Habla - 80% LH* (20 horas por año)"+
                "\n"+
                f"\nConsultas psicológicas y psiquiátricas - 80% LH* (25 por año)"+
                "\n"+
                f"\nProcedimientos ambulatorios - 80% LH* (ilimitado)"+
                "\n"+
                f"\nEstudios Especiales - 80% LH* (ilimitado)"+
                "\n"+
                f"\nEmergencias - 100% dentro de la red (80% en caso de urgencia médica, reembolso hasta RD$1,500 fuera de la red)")
            )
            
        def royal_cover2():
            messagebox.showinfo("Royal", (
                "***Coberturas de Hospitalización***"+
                "\n"+
                f"\nHabitación - 100% (RD$4,000 por día/ilimitado)"+
                "\n"+
                f"\nMedicinas en internamiento - 100% (ilimitado)"+
                "\n"+
                f"\nSala de cirugía - 100% LH*"+
                "\n"+
                f"\nAnestesia y material gastable - 100% LH*"+
                "\n"+
                f"\nHonorarios Médicos - 100% LH*"+
                "\n"+
                f"\nLaboratorios y Rayos X - 100% LH*"+
                "\n"+
                f"\nEstudios Especiales - 100% LH*"+
                "\n"+
                f"\nSala de cuidados intensivos - 100% (RD$5,000 por día/ilimitado)"
                )
            )
            
        def royal_cover3():
            messagebox.showinfo("Royal", (
                "***Coberturas de Maternidad***"+
                "\n"+
                f"\nParto Normal - 100% LH*"+
                "\n"+
                f"\nCesárea - 100% LH*"+
                "\n"+
                f"\nNiños Recien Nacidos - 100% (hasta RD$125,000)"        
                )
            )
        
        def royal_cover4():
            messagebox.showinfo("Royal", (
                "***Otras Coberturas***"+
                "\n"+
                f"\nGasto Médico Mayor - RD$850,000 por año"+
                "\n"+
                f"\nEnfermedades Mayores - RD$50,000"
                "\n"+
                f"\nÚltimos Gastos - RD$50,000"+
                "\n"+
                f"\nSeguro de vida (Titular) - RD$100,000"
                "\n"+
                f"\nAmbulancia Terrestre - Incluida"+
                "\n"+
                f"\nPlan Odontológico- Dental Humano"+
                "\n"+
                f"\nLímite por caso - RD$500,000"         
                )
            )
        
        def max_info():
            messagebox.showinfo("Max", (
                "Plan privado a través de​​l cual ponemos a tu alcance los servicios de salud que tanto tú como los tuyos necesitan. Cuentas con una amplia cobertura local en atención ambulatoria, ayudas diagnósticas, servicios de hospitalización, cirugías y parto, además de proporciona​rte acceso directo a la prestigiosa red de prestadores de servicios de mediante la facilidad de reembolso."                     
                )
            )
        
        def max_cover1():
            messagebox.showinfo("Max", (                
                "***Coberturas Ambulatorias***"+
                "\n"+
                f"\nConsultas Ambulatorias - Ilimitado. Pago diferencia por consulta - Reembolso: 80% (hasta RD$2,000 por consulta)"+
                "\n"+
                f"\nLaboratorios y Rayos X - 85% (ilimitado) - Reembolso: 80% GR**"+
                "\n"+
                f"\nVacunas - 80% (hasta los 10 años en centros afiliados) - Reembolso: 80% GR**"+
                "\n"+
                f"\nTerapias Físicas - 80% LH* (20 por año) - Reembolso: 80% GR**"+
                "\n"+
                "\n"+
                f"\nTerapias del Habla - 85% LH* (20 horas por año) - Reembolso: 80% GR**"+
                "\n"+
                f"\nConsultas psicológicas y psiquiátricas - 80% LH* (25 por año) - Reembolso: 80% (Hasta RD$2,000 por consulta)"+
                "\n"+
                f"\nProcedimientos ambulatorios - 85% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nEstudios Especiales - 85% (ilimitado) - Reembolso: 80% GR**"+
                "\n"+
                f"\nEmergencias - 100% en centros afiliados (80% en caso de urgencia médica) - Reembolso: 80% GR**")
            )
            
        def max_cover2():
            messagebox.showinfo("Max", (
                "***Coberturas de Hospitalización***"+
                "\n"+
                f"\nHabitación - 100% (RD$4,000 por día/ilimitado) - Reembolso: 80% (hasta RD$4,000 por día/ilimitado)"+
                "\n"+
                f"\nMedicinas en internamiento - 100% (ilimitado) - Reembolso: 80% GR**"+
                "\n"+
                f"\nSala de cirugía - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nAnestesia y material gastable - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nHonorarios Médicos - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nLaboratorios y Rayos X - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nEstudios Especiales - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nSala de cuidados intensivos - 100% (ilimitado) - Reembolso: 80% GR**"
                )
            )
            
        def max_cover3():
            messagebox.showinfo("Max", (
                "***Coberturas de Maternidad***"+
                "\n"+
                f"\nParto Normal - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nCesárea - 100% LH* - Reembolso: 80% GR**"+
                "\n"+
                f"\nNiños Recien Nacidos - Hasta el límite por caso - Reembolso: 80% GR**"        
                )
            )
        
        def max_cover4():
            messagebox.showinfo("Max", (
                "***Otras Coberturas***"+
                "\n"+
                f"\nGasto Médico Mayor - RD$1,000,000 por año"+
                "\n"+
                f"\nEnfermedades Mayores - RD$50,000"
                "\n"+
                f"\nÚltimos Gastos - RD$100,000"+
                "\n"+
                f"\nSeguro de vida (Titular) - RD$100,000"
                "\n"+
                f"\nAmbulancia Terrestre - Incluida"+
                "\n"+
                f"\nAmbulancia Aérea Nacional - Disponible por reembolso con el proveedor de su preferencia (100% hasta RD$500,000 por año)"+
                "\n"+                
                f"\nPlan Odontológico- Dental Humano"+
                "\n"+
                f"\nLímite por caso - RD$750,000"         
                )
            )
        
        def prime_info():
            messagebox.showinfo("Prime", (
                "Si buscas un plan privado de salud que te ofrezca excelente cobertura local, considerando una buena relación calidad precio, esta opción es para ti.  Con Mi Salud Prime, siente la tranquilidad de contar con acceso a la más prestigiosa red de Prestadores de Servicios de Salud, así como coberturas  en consultas ambulatorias, hospitalización, maternidad, entre otras. Además, puedes solicitar reembolsos del 90% en gastos médicos fuera de la red de prestadores, según los honorarios médicos establecidos."                     
                )
            )
        
        def prime_cover1():
            messagebox.showinfo("Prime", (                
                "***Coberturas Ambulatorias***"+
                "\n"+
                f"\nConsultas Ambulatorias - Ilimitado. Pago diferencia por consulta - Reembolso: 90% GR** (hasta RD$ 4,000 por consulta)"+
                "\n"+
                f"\nLaboratorios y Rayos X - 90% (ilimitado) - Reembolso: 90% GR**"+
                "\n"+
                f"\nVacunas - 90% (hasta los 10 años) - Reembolso: 90% GR**"+
                "\n"+
                f"\nTerapias Físicas - 90% (25 por año) - Reembolso: 90% GR**"+
                "\n"+
                f"\nTerapias del Habla - 90% (20 por año) - Reembolso: 90% GR**"+
                "\n"+
                f"\nConsultas psicológicas y psiquiátricas - 90% (25 por año) - Reembolso: 90% GR** (hasta RD$ 4,000 por consulta)"+
                "\n"+
                f"\nProcedimientos ambulatorios - 90% (ilimitado) - Reembolso: 90% GR**"+
                "\n"+
                f"\nMedicina ambulatoria - 80% (hasta RD$5,000) - Reembolso: 80% GR**"+
                "\n"+
                f"\nEstudios Especiales - 90% (ilimitado) - Reembolso: 90% GR**"+
                "\n"+
                f"\nEmergencias - 100% (ilimitado) - Reembolso: 90% GR**")
            )
            
        def prime_cover2():
            messagebox.showinfo("Prime", (
                "***Coberturas de Hospitalización***"+
                "\n"+
                f"\nHabitación - 100% (RD$6,000 por día/ilimitado) - Reembolso: 90% GR**"+
                "\n"+
                f"\nMedicinas en internamiento - 100% (ilimitado) - Reembolso: 90% GR*^"+
                "\n"+
                f"\nSala de cirugía - 100% LH* - Reembolso: 90% GR**"+
                "\n"+
                f"\nAnestesia y material gastable - 100% LH* - Reembolso: 90% GR**"+
                "\n"+
                f"\nHonorarios Médicos - 100% LH* - Reembolso: 90% GR**"+
                "\n"+
                f"\nLaboratorios y Rayos X - 100% LH* - Reembolso: 90% GR**"+
                "\n"+
                f"\nEstudios Especiales - 100% LH* - Reembolso: 90% GR**"+
                "\n"+
                f"\nSala de cuidados intensivos - 100% (ilimitado) - Reembolso: 90% GR**"
                )
            )
            
        def prime_cover3():
            messagebox.showinfo("Prime", (
                "***Coberturas de Maternidad***"+
                "\n"+
                f"\nParto Normal - 100% LH*(hasta RD$250,000) - Reembolso: 90% GR**"+
                "\n"+
                f"\nCesárea - 100% LH* (hasta RD$250,000) - Reembolso: 90% GR**"+
                "\n"+
                f"\nNiños Recien Nacidos - 100% (hasta RD$1,000,000) - Reembolso: 90% GR**"        
                )
            )
        
        def prime_cover4():
            messagebox.showinfo("Prime", (
                "***Otras Coberturas***"+
                "\n"+
                f"\nGasto Médico Mayor - RD$1,500,000 por año"+
                "\n"+
                f"\nEnfermedades Mayores - RD$50,000"
                "\n"+
                f"\nÚltimos Gastos - RD$150,000"+
                "\n"+
                f"\nSeguro de vida (Titular) - RD$100,000"
                "\n"+
                f"\nAmbulancia Terrestre - Incluida"+
                "\n"+
                f"\nAmbulancia Aérea Nacional - Alert Plus"+
                "\n"+                
                f"\nPlan Odontológico- Dental Humano"+
                "\n"+
                f"\nLímite por caso - RD$1,500,000"         
                )
            )
        
        def platinum_info():
            messagebox.showinfo("Platinum", (
                "El más completo plan privado a través del cual ponemos a tu alcance los servicios de salud que tanto tú como los tuyos necesitan. Cuentas con la más completa cobertura local en atención ambulatoria, ayudas diagnósticas, servicios de hospitalización, cirugías y parto, con acceso directo a la exclusiva red de prestadores de servicios de salud contratada por Humano."                     
                )
            )
        
        def platinum_cover1():
            messagebox.showinfo("Platinum", (                
                "***Coberturas Ambulatorias***"+
                "\n"+
                f"\nConsultas Ambulatorias - Ilimitadas. Diferencia por consulta - Reembolso: 90%"+
                "\n"+
                f"\nLaboratorios y Rayos X - 100% (ilimitado) - Reembolso: 90%"+
                "\n"+
                f"\nVacunas - 100% (hasta los 10 años) - Reembolso: 90%"+
                "\n"+
                f"\nTerapias Físicas - 100% (30 por año) - Reembolso: 90%"+
                "\n"+
                f"\nTerapias del Habla - 100% (8 horas al mes) - Reembolso: 90%"+
                "\n"+
                f"\nConsultas psicológicas y psiquiátricas - 100% (ilimitado) - Reembolso: 90%"+
                "\n"+
                f"\nProcedimientos ambulatorios - 100% (ilimitado) - Reembolso: 90%"+
                "\n"+
                f"\nMedicina ambulatoria - 80% (hasta RD$10,000) - Reembolso: 80%"+
                "\n"+
                f"\nEstudios Especiales - 100% (ilimitado) - Reembolso: 90%"+
                "\n"+
                f"\nEmergencias - 100% (ilimitado) - Reembolso: 90%")
            )
            
        def platinum_cover2():
            messagebox.showinfo("Platinum", (
                "***Coberturas de Hospitalización***"+
                "\n"+
                f"\nHabitación - 100% - Reembolso: 90%"+
                "\n"+
                f"\nMedicinas en internamiento - 100% - Reembolso: 90%"+
                "\n"+
                f"\nSala de cirugía - 100% - Reembolso: 90%"+
                "\n"+
                f"\nAnestesia y material gastable - 100% - Reembolso: 90%"+
                "\n"+
                f"\nHonorarios Médicos - 100% - Reembolso: 90%"+
                "\n"+
                f"\nLaboratorios y Rayos X - 100% - Reembolso: 90%"+
                "\n"+
                f"\nEstudios Especiales - 100% - Reembolso: 90%"+
                "\n"+
                f"\nSala de cuidados intensivos - 100% - Reembolso: 90%"
                )
            )
            
        def platinum_cover3():
            messagebox.showinfo("Platinum", (
                "***Coberturas de Maternidad***"+
                "\n"+
                f"\nParto Normal - 100% (hasta RD$400,000) - Reembolso: 90%"+
                "\n"+
                f"\nCesárea - 100% LH* (hasta RD$400,000) - Reembolso: 90%"+
                "\n"+
                f"\nNiños Recien Nacidos - Hasta el límite por caso - Reembolso: 90%"+
                "\n"+
                f"\nScreening Neonatal - 100% - Reembolso: 90%"            
                )
            )
        
        def platinum_cover4():
            messagebox.showinfo("Platinum", (
                "***Otras Coberturas***"+
                "\n"+
                f"\nGasto Médico Mayor - RD$2,500,000 por año"+
                "\n"+
                f"\nEnfermedades Mayores - RD$50,000"
                "\n"+
                f"\nÚltimos Gastos - RD$200,000"+
                "\n"+
                f"\nSeguro de vida (Titular) - RD$100,000 por año"
                "\n"+
                f"\nAmbulancia Terrestre - Incluida"+
                "\n"+
                f"\nAmbulancia Aérea Nacional - Alert Plus"+
                "\n"+   
                f"\nSeguro Viajero - US$10,000"+
                "\n"+ 
                f"\nReembolso Gastos Médicos en el extranjero - US$1,000 por año"+
                "\n"+              
                f"\nAsistencia Force SOS - Incluido"+
                "\n"+              
                f"\nSala VIP en Aeropuerto - Incluido"+
                "\n"+  
                f"\nMillas AA - Incluido"+
                "\n"+               
                f"\nPlan Odontológico- Dental Platinum"+
                "\n"+
                f"\nReembolso terapias ABA - 90% (24 horas por mes hasta RD$1,500 por hora)"+
                "\n"+
                f"\nLímite por caso - RD$2,000,000"         
                )
            )
        
        def miautomotorbasico_info():
            messagebox.showinfo("Mi Auto Motor Básico", (
                "Ofrece cobertura de daños a terceros (Pasajeros, propiedad de terceros, fianza), y de manera opcional pueden ser contratadas las coberturas de otros servicios."                     
                )
            )
            
        def miautomotorbasico_cover1():
            messagebox.showinfo("Mi Auto Motor Básico", (
                "*** Riesgos Cubiertos ***"+                     
                "\n"+
                f"\nResponsabilidad Civil"+
                "\n"+
                f"\nFianza judicial"+
                "\n"                
                )
            )
            
        def miautomotorbasico_cover2():
            messagebox.showinfo("Mi Auto Motor Básico", (                
                f"*** Beneficios Opcionales ***"+
                "\n"+
                f"\nCasa del conductor o Centro de Asistencia al Asegurado (A elección del cliente)"
                )
            )
        
        def miautobasico_info():
            messagebox.showinfo("Mi Auto Básico",
                (                                
                "Ofrece cobertura de daños a terceros (Pasajeros, conductor, propiedad de terceros, fianza), para vehículos sin restricción en edad de fabricación y de manera opcional pueden ser contratadas las coberturas de otros servicios."
                )
            )
            
        def miautobasico_cover1():
            messagebox.showinfo("Mi Auto Básico",
                (
                "*** Riesgos Cubiertos (Plan Ley) ***"+
                "\n"+
                f"\nLesiones corporales y/o muerte a un tercero"+
                "\n"+
                f"\nLesiones corporales y/o muerte a más de un tercero"+
                "\n"+
                f"\nDaños a la propiedad de terceros"+
                "\n"+
                f"\nLesiones corporales y/o muerte a un pasajero"+
                "\n"+
                f"\nLesiones corporales y/o muerte a más de un pasajero"+
                "\n"+
                f"\nAccidentes personales conductor"+
                "\n"+
                f"\nGastos médicos al conductor"+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nDefensa legal"
                )
            )
            
        def miautobasico_cover2():
            messagebox.showinfo("Mi Auto Básico",
                (                
                "*** Beneficios Opcionales ***"+
                "\n"+
                f"\nAsistencia Vial – Vehículos Livianos menos de 3,500 kgrms"+
                "\n"+
                f"\nCasa del Conductor o Centro de Asistencia al Asegurado, a elección del cliente"+
                "\n"+
                f"\nAsistencia Vial – Vehículos Pesados más de 3,500 kgrms"+
                "\n"+
                f"\nSeguridad Vial"+
                "\n"+
                f"\nÚltimos Gastos"+
                "\n"+
                f"\nAeroambulancia (7 pasajeros o menos)"                                    
                )
            )
        
        def miautoflex_info():
            messagebox.showinfo("Mi Auto Flex",
                (                                
                "Ofrece cobertura de daños al casco del Vehículo de 11 a 15 años de fabricación, adicional a las coberturas de responsabilidad civil a terceros, pasajeros, y propiedad de terceros. Coberturas amparadas siempre que se produzca una pérdida total conforme lo establece el Condicionado General del producto."
                )
            )
            
        def miautoflex_cover1():
            messagebox.showinfo("Mi Auto Flex", (
                "*** Plan Todo Riesgo ***"+                                     
                "\n"+
                f"\nPérdida total por daños materiales"+
                "\n"+                
                f"\nPérdida total por robo o hurto"+
                "\n"+  
                f"\nDaños por pavimento irregular"+
                "\n"+ 
                f"\nDaños por agua"                            
                )
            )
        
        def miautoflex_cover2():
            messagebox.showinfo("Mi Auto Flex", (
                "*** Plan Ley ***"+                     
                "\n"+
                f"\nLesiones corporales y/o muerte a un tercero"+
                "\n"+
                f"\nLesiones corporales y/o muerte a más de un tercero"+
                "\n"+
                f"\nDaños a la propiedad de terceros"+
                "\n"+     
                f"\nLesiones corporales y/o muerte a un pasajero"+
                "\n"+  
                f"\nLesiones corporales y/o muerte a más de un pasajero"+
                "\n"+
                f"\nAccidentes personales conductor" 
                "\n"+
                f"\nGastos médicos al conductor"+
                "\n"+ 
                f"\nFianza judicial"+
                "\n"+ 
                f"\nDefensa legal"                            
                )
            )
        
        def miautoflex_cover3():
            messagebox.showinfo("Mi Auto Flex", (
                "*** Beneficios Incluidos ***"+                     
                "\n"+
                f"\nAsistencia Vial – Vehículos Livianos menos de 3,500 kgrms "+
                "\n"+
                f"\nGrúa por averías, accidente o maniobras"+
                "\n"+                
                f"\nCasa del Conductor o Centro de Asistencia al Automovilista, a elección del cliente"                                
                )
            )
            
        def miautoflex_cover4():
            messagebox.showinfo("Mi Auto Flex", (
                "*** Beneficios Opcionales ***"+                     
                "\n"+
                f"\nAsistencia Vial – Vehículos Pesados más de 3,500 kgrms"+
                "\n"+
                f"\nSeguridad Vial"+
                "\n"+
                f"\nÚltimos Gastos"+
                "\n"+     
                f"\nAeroambulancia (7 pasajeros o menos)"            
                )
            )
            
        def miautofull_info():
            messagebox.showinfo("Mi Auto Full", (
                "Ofrece cobertura de daños al casco del Vehículo hasta 10 años de fabricación, adicional a las coberturas de responsabilidad civil a terceros, pasajeros, y propiedad de terceros."
                )
            )
           
        def miautofull_cover1():
            messagebox.showinfo("Mi Auto Full", (
                "*** Planes Todo Riesgo ***"+                     
                "\n"+
                f"\nPérdida parcial por daños materiales"+
                "\n"+
                f"\nPérdida total por daños materiales"+
                "\n"+
                f"\nPérdida parcial por robo o hurto"+
                "\n"+     
                f"\nPérdida total por robo o hurto"+
                "\n"+  
                f"\nRotura de cristales"+
                "\n"+ 
                f"\nRobo de partes externas"+
                "\n"+ 
                f"\nDaños por pavimento irregular"+
                "\n"+
                f"\nDaños por agua"                          
                )
            ) 
            
        def miautofull_cover2():
            messagebox.showinfo("Mi Auto Full", (
                "*** Plan Ley ***"+                     
                "\n"+
                f"\nLesiones corporales y/o muerte a un tercero"+
                "\n"+
                f"\nLesiones corporales y/o muerte a más de un tercero"+
                "\n"+
                f"\nDaños a la propiedad de terceros"+
                "\n"+     
                f"\nLesiones corporales y/o muerte a un pasajero"+
                "\n"+  
                f"\nLesiones corporales y/o muerte a más de un pasajero"+
                "\n"+ 
                f"\nGastos médicos al conductor"+
                "\n"+ 
                f"\nFianza judicial"+
                "\n"+
                f"\nDefensa legal" 
                )
            ) 
        
        def miautofull_cover3():
            messagebox.showinfo("Mi Auto Full", (
                "*** Beneficios Incluidos ***"+                     
                "\n"+
                f"\nAsistencia Vial – Vehículos Livianos menos de 3,500 kgrms "+
                "\n"+
                f"\nGrúa por averías, accidente o maniobras"+
                "\n"+
                f"\nAuxilio Vial para paso de corriente, cambio de neumático, envío de combustible, mecánica ligera y cerrajería vial"+
                "\n"+     
                f"\nTraslado Médico Terrestre"+
                "\n"+  
                f"\nCasa del Conductor o Centro de Asistencia al Automovilista, a elección del cliente"+
                "\n"+ 
                f"\nPlan Auto Rentado: incluye 10 días de vehículo rentado con opciones de incremento de días de renta hasta un máximo de 30."+
                "\n"+ 
                f"\nPick up de vehículo en mantenimiento: recibe asistencia de un chofer provisional para el traslado del vehículo hasta el concesionario o taller mecánico para fines de mantenimiento periódico o reparación por daño accidental, y traslado del vehículo desde estos, hasta la residencia u oficina del asegurado una vez finalizado el mantenimiento o reparación."+
                "\n"+
                f"\nCoordinación de trámites vehiculares: cuenta con servicios de reposición de matrículas por pérdida o deterioro y traspaso de vehículo de motor."                          
                )
            )
            
        def miautofull_cover4():
            messagebox.showinfo("Mi Auto Full", (
                "*** Beneficios Opcionales ***"+                     
                "\n"+
                f"\nAsistencia Vial – Vehículos Pesados más de 3,500 kgrms"+
                "\n"+
                f"\nSeguridad Vial"+
                "\n"+
                f"\nÚltimos Gastos"+
                "\n"+     
                f"\nAeroambulancia (7 pasajeros o menos)"            
                )
            )
         
        def miautopremier_info():
            messagebox.showinfo(
                "Mi Auto Premier","Ofrece cobertura de daños al casco del Vehículo hasta 3 años de antigüedad y extendido hasta 5 años para renovación, adicional a las coberturas de responsabilidad civil a terceros, pasajeros, y propiedad de terceros."    
            )
            
        def miautopremier_cover1():
            messagebox.showinfo("Mi Auto Premier", (
                "*** Planes Todo Riesgo ***"+
                "\n"+
                f"\nPérdida parcial por daños materiales"+
                "\n"+
                f"\nPérdida total por daños materiales"+
                "\n"+
                f"\nPérdida parcial por robo o hurto"+
                "\n"+
                f"\nPérdida total por robo o hurto"+
                "\n"+
                f"\nRotura de cristales"+
                "\n"+
                f"\nRobo de partes externas"+
                "\n"+
                f"\nDaños por pavimento irregular"+
                "\n"+
                f"\nDaños por agua"
                )
            )
        
        def miautopremier_cover2():
            messagebox.showinfo("Mi Auto Premier", (
                "*** Beneficios Incluidos ***"+
                "\n"+
                f"\nAsistencia Vial – Vehículos Livianos menos de 3,500 kgrms"+
                "\n"+
                f"\nGrúa por averías, accidente o maniobras"+
                "\n"+
                f"\nAuxilio Vial para paso de corriente, cambio de neumático, envío de combustible, mecánica ligera y cerrajería vial"+
                "\n"+
                f"\nTraslado Médico Terrestre"+
                "\n"+
                f"\nCasa del Conductor o Centro de Asistencia al Automovilista, a elección del cliente"+
                "\n"+
                f"\nPlan Auto Rentado: incluye 10 días de vehículo rentado con opciones de incremento de días de renta hasta un máximo de 30."+
                "\n"+
                f"\nPick up de vehículo en mantenimiento: recibe asistencia de un chofer provisional para el traslado del vehículo hasta el concesionario o taller mecánico para fines de mantenimiento periódico o reparación por daño accidental, y traslado del vehículo desde estos, hasta la residencia u oficina del asegurado una vez finalizado el mantenimiento o reparación."+
                "\n"+
                f"\nCoordinación de trámites vehiculares: cuenta con servicios de reposición de matrículas por pérdida o deterioro y traspaso de vehículo de motor."
                )
            )
            
        def miautopremier_cover3():
            messagebox.showinfo("Mi Auto Premier", (
                "*** Beneficios Opcionales ***"+
                "\n"+
                f"\nAsistencia Vial - Vehículos Pesados de más de 3,500 kgrms"+
                "\n"+
                f"\nSeguridad Vial"+
                "\n"+
                f"\nÚltimos Gastos"+
                "\n"+
                f"\nAeroambulancia (7 pasajeros o menos)"
                )
            )
         
        # humano page 2 #
        
        F2_2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Salud Humano",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2_2.place(x=0,y=290,width=925,height=260)   
            
        prime_lbl=Label(F2_2,text="Prime", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        prime_txt=Entry(F2_2, width=2,textvariable=self.prime,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        prime_info1=Button(F2_2,text="Info.",command=prime_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        prime_info2=Button(F2_2,text="Cobertura Amb.",command=prime_cover1,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        prime_info3=Button(F2_2,text="Cobertura Hosp.",command=prime_cover2,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        prime_info4=Button(F2_2,text="Cobertura Matern.",command=prime_cover3,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")        
        prime_info5=Button(F2_2,text="Otras Coberturas.",command=prime_cover4,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10,sticky="w")                
        
        platinum_lbl=Label(F2_2,text="Platinum", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        platinum_txt=Entry(F2_2, width=2,textvariable=self.platinum,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        platinum_info1=Button(F2_2,text="Info.",command=platinum_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        platinum_info2=Button(F2_2,text="Cobertura Amb.",command=platinum_cover1,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        platinum_info3=Button(F2_2,text="Cobertura Hosp.",command=platinum_cover2,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        platinum_info4=Button(F2_2,text="Cobertura Matern.",command=platinum_cover3,font="arial 12 bold").grid(row=1,column=5,padx=10,pady=10,sticky="w")        
        platinum_info5=Button(F2_2,text="Otras Coberturas.",command=platinum_cover4,font="arial 12 bold").grid(row=1,column=6,padx=10,pady=10,sticky="w")           
        
        healthplan_lbl=Label(F2_2,text="Plan de Salud", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        healthplan_txt=Entry(F2_2, width=2,textvariable=self.healthplan,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)     
        
        # humano page 3 #
        
        F2_3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Vehículos Humano",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2_3.place(x=0,y=290,width=925,height=260) 
        
        miautomotorbasico_lbl=Label(F2_3,text="Mi Auto Moto básico", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        miautomotorbasico_txt=Entry(F2_3, width=2,textvariable=self.miautomotobasico,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        miautomotorbasico_info1=Button(F2_3,text="Info.",command=miautomotorbasico_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        miautomotorbasico_info2=Button(F2_3,text="Riesgos Cubiertos.",command=miautomotorbasico_cover1,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        miautomotorbasico_info3=Button(F2_3,text="Beneficios Opc.",command=miautomotorbasico_cover2,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        
        miautobasico_lbl=Label(F2_3,text="Mi Auto básico", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        miautobasico_txt=Entry(F2_3, width=2,textvariable=self.miautobasico,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        miautobasico_info1=Button(F2_3,text="Info.",command=miautobasico_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        miautobasico_info2=Button(F2_3,text="Riesgos Cubiertos.",command=miautobasico_cover1,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        miautobasico_info3=Button(F2_3,text="Beneficios Opc.",command=miautobasico_cover2,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        
        miautoflex_lbl=Label(F2_3,text="Mi Auto Flex", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        miautoflex_txt=Entry(F2_3, width=2,textvariable=self.miautoflex,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        miautoflex_info1=Button(F2_3,text="Info.",command=miautoflex_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        miautoflex_info2=Button(F2_3,text="Plan Todo Riesgo.",command=miautoflex_cover1,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        miautoflex_info3=Button(F2_3,text="Beneficios Inc.",command=miautoflex_cover3,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")        
        miautoflex_info4=Button(F2_3,text="Beneficios Opc.",command=miautoflex_cover4,font="arial 12 bold").grid(row=2,column=5,padx=10,pady=10,sticky="w")        
        miautoflex_info5=Button(F2_3,text="Plan Ley",command=miautoflex_cover2,font="arial 12 bold").grid(row=2,column=6,padx=10,pady=10,sticky="w")                
        
        miautofull_lbl=Label(F2_3,text="Mi Auto Full", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        miautofull_txt=Entry(F2_3, width=2,textvariable=self.miautofull,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        miautofull_info1=Button(F2_3,text="Info.",command=miautofull_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        miautofull_info2=Button(F2_3,text="Plan Todo Riesgo.",command=miautofull_cover1,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        miautofull_info3=Button(F2_3,text="Beneficios Inc.",command=miautofull_cover3,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")        
        miautofull_info4=Button(F2_3,text="Beneficios Opc.",command=miautofull_cover4,font="arial 12 bold").grid(row=3,column=5,padx=10,pady=10,sticky="w")        
        miautofull_info5=Button(F2_3,text="Plan Ley",command=miautofull_cover2,font="arial 12 bold").grid(row=3,column=6,padx=10,pady=10,sticky="w")                
        
        # humano page 4 # 
           
        F2_4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Vehículos Humano",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2_4.place(x=0,y=290,width=925,height=260) 
        
        miautopremier_lbl=Label(F2_4,text="Mi Auto Premier", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        miautopremier_txt=Entry(F2_4, width=2,textvariable=self.miautopremier,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        miautopremier_info1=Button(F2_4,text="Info.",command=miautopremier_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        miautopremier_info2=Button(F2_4,text="Planes Todo Riesgo",command=miautopremier_cover1,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        miautopremier_info3=Button(F2_4,text="Beneficios Inc.",command=miautopremier_cover2,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        miautopremier_info4=Button(F2_4,text="Beneficios Opc.",command=miautopremier_cover3,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")        
        
        # humano page selector #
        
        F2_Menu=LabelFrame(self.root,bg=bg_color)
        F2_Menu.place(x=0,y=267,width=925,height=24)      
        
        def f2_2():            
            F2_2.lift()
        
        def f2_3():
            F2_3.lift()
            
        def f2_4():
            F2_4.lift()
        
        def f2_1():
            F2.lift()
        
        F2_page1=Button(F2_Menu,text="1",command=f2_1,font="arial 12 bold").place(x=0,y=0,width=232,height=24)
        F2_page2=Button(F2_Menu,text="2",command=f2_2,font="arial 12 bold").place(x=233,y=0,width=232,height=24)
        F2_page3=Button(F2_Menu,text="3",command=f2_3,font="arial 12 bold").place(x=465,y=0,width=232,height=24)        
        F2_page4=Button(F2_Menu,text="4",command=f2_4,font="arial 12 bold").place(x=697,y=0,width=232,height=24)                
    
        # humano page 1 #
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Salud Humano",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=290,width=925,height=260)                
        
        esencial_plus_lbl=Label(F2,text="Esencial Plus", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        esencial_plus_txt=Entry(F2, width=2,textvariable=self.esencial_plus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        esencial_plus_info1=Button(F2,text="Info.",command=esenc_plus_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        esencial_plus_info2=Button(F2,text="Cobertura Amb.",command=esenc_plus_cover1,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        esencial_plus_info3=Button(F2,text="Cobertura Hosp.",command=esenc_plus_cover2,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        esencial_plus_info4=Button(F2,text="Cobertura Matern.",command=esenc_plus_cover3,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")        
        esencial_plus_info5=Button(F2,text="Otras Coberturas.",command=esenc_plus_cover4,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10,sticky="w")                
        
        superior_lbl=Label(F2,text="Superior", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        superior_txt=Entry(F2, width=2,textvariable=self.superior,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        superior_info1=Button(F2,text="Info.",command=superior_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        superior_info2=Button(F2,text="Cobertura Amb.",command=superior_cover1,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        superior_info3=Button(F2,text="Cobertura Hosp.",command=superior_cover2,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        superior_info4=Button(F2,text="Cobertura Matern.",command=superior_cover3,font="arial 12 bold").grid(row=1,column=5,padx=10,pady=10,sticky="w")        
        superior_info5=Button(F2,text="Otras Coberturas.",command=superior_cover4,font="arial 12 bold").grid(row=1,column=6,padx=10,pady=10,sticky="w")                
        
        royal_lbl=Label(F2,text="Royal", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        royal_txt=Entry(F2, width=2,textvariable=self.royal,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        royal_info1=Button(F2,text="Info.",command=royal_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        royal_info2=Button(F2,text="Cobertura Amb.",command=royal_cover1,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        royal_info3=Button(F2,text="Cobertura Hosp.",command=royal_cover2,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")        
        royal_info4=Button(F2,text="Cobertura Matern.",command=royal_cover3,font="arial 12 bold").grid(row=2,column=5,padx=10,pady=10,sticky="w")        
        royal_info5=Button(F2,text="Otras Coberturas.",command=royal_cover4,font="arial 12 bold").grid(row=2,column=6,padx=10,pady=10,sticky="w")                
        
        max_lbl=Label(F2,text="Max", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        max_txt=Entry(F2, width=2,textvariable=self.max,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)                
        max_info1=Button(F2,text="Info.",command=max_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        max_info2=Button(F2,text="Cobertura Amb.",command=max_cover1,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        max_info3=Button(F2,text="Cobertura Hosp.",command=max_cover2,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")        
        max_info4=Button(F2,text="Cobertura Matern.",command=max_cover3,font="arial 12 bold").grid(row=3,column=5,padx=10,pady=10,sticky="w")        
        max_info5=Button(F2,text="Otras Coberturas.",command=max_cover4,font="arial 12 bold").grid(row=3,column=6,padx=10,pady=10,sticky="w")                
        
    # fila de seguros atlantica
        
        # Atlantica seguros info
        
        def orion_info():
            messagebox.showinfo("Orion", (
                "El Seguro de vida a término se utiliza para cubrir las necesidades de protección financiera de su familia durante un período de tiempo específico. Las primas se fijan y deben ser pagadas dentro de un período de tiempo específico o la póliza es cancelada."+
                "\n"+
                f"\nEste producto ofrece una cobertura con primas niveladas durante la vigencia de la póliza. No tiene un componente de inversión y, como tal, ofrece la suma asegurada al menor costo posible."+
                "\n"+
                f"\nEstá especialmente recomendado para personas que tienen una gran necesidad de protección por un período específico de tiempo, ya que maximiza la relación costo/protección."+
                "\n"+
                f"\nLa prima inicial para la protección es baja, en comparación con otros tipos de pólizas. Esto se debe a que sólo es válida por un tiempo limitado y no genera ingresos por ahorros o inversiones."+
                "\n"+
                "Las primas pueden aumentar si la póliza de seguro se extiende después del plazo inicialmente contratado."
            ))
            
        def orion_characteristics():
            messagebox.showinfo("Orion", (
                "*** Características ***"+
                "\n"+
                f"\nEdad de Suscripción - Planes disponibles para personas desde 3 meses hasta 65 años de edad."+
                "\n"+
                f"\nPeríodo asegurado y extension de cobertura - Cobertura garantizada durante el período de cobertura seleccionada, que puede ser un Período Flexible de Cobertura: 5 a 30 años. Puede extender su cobertura después del período asegurado inicial con primas variables."+
                "\n"+
                f"\nPrimas - Primas fijas acorde a lo definido en el contrato."+
                "\n"+
                f"\nFrecuencia de pago - Semestral y Anual."+
                "\n"+
                f"\nBeneficios - Pesos dominicanos de RD$ 250mil a RD$ 1.25millones"+
                "\n"+
                f"\nMoneda - Pesos Dominicanos."
            ))
            
        def orion_suplements():
            messagebox.showinfo("Orion", (
                "*** Suplementos ***"
                "\n"+
                f"\nBeneficio por Muerte Accidental. - Igual o menor que el beneficio por fallecimiento hasta un máximo de 150,000."+
                "\n"+
                f"\nSeguro para cónyuge u otro asegurado - Monto igual o menor que el beneficio por fallecimiento de la póliza."+
                "\n"+
                f"\nBeneficio por muerte en caso de enfermedad terminal - Hasta un máximo de un 50% de la suma asegurada."+
                "\n"+
                f"\nGastos Funerarios - Hasta un máximo de RD$ 1,250,000."+
                "\n"+
                f"\nIncapacidad Total y Permanente - La suma asegurada será pagadera en 24 cuotas mensuales continuas de igual monto a partir de agotar el período de espera de seis meses"
            ))
        
        def orionplus_info():
            messagebox.showinfo("Orion Plus", (
                "El Seguro de vida a término se utiliza para cubrir las necesidades de protección financiera de su familia durante un período de tiempo específico. Las primas se fijan y deben ser pagadas dentro de un período de tiempo específico o la póliza es cancelada."+
                "\n"+
                f"\nEste producto ofrece una cobertura con primas niveladas durante la vigencia de la póliza. No tiene un componente de inversión y, como tal, ofrece la suma asegurada al menor costo posible."+
                "\n"+
                f"\nEstá especialmente recomendado para personas que tienen una gran necesidad de protección por un período específico de tiempo, ya que maximiza la relación costo/protección."+
                "\n"+
                f"\nLa prima inicial para la protección es baja, en comparación con otros tipos de pólizas. Esto se debe a que sólo es válida por un tiempo limitado y no genera ingresos por ahorros o inversiones."+
                "\n"+
                "Las primas pueden aumentar si la póliza de seguro se extiende después del plazo inicialmente contratado."
            ))
            
        def orionplus_characteristics():
            messagebox.showinfo("Orion Plus", (
                "*** Características ***"+
                "\n"+
                f"\nEdad de Suscripción - Planes disponibles para personas desde 3 meses hasta 65 años de edad."+
                "\n"+
                f"\nPeríodo asegurado y extension de cobertura - Cobertura garantizada durante el período de cobertura seleccionada, que puede ser un Período Flexible de Cobertura: 5 a 30 años. Puede extender su cobertura después del período asegurado inicial con primas variables."+
                "\n"+
                f"\nPrimas - Primas fijas acorde a lo definido en el contrato."+
                "\n"+
                f"\nFrecuencia de pago - Semestral y Anual."+
                "\n"+
                f"\nBeneficios - Pesos dominicanos de RD$ 1.25 millones a RD$ 90millones / Dólares americanos de US$ 25mil a 2 millones"+
                "\n"+
                f"\nMoneda - Pesos Dominicanos y Dólares Estadounidenses."
            ))
            
        def orionplus_suplements():
            messagebox.showinfo("Orion Plus", (
                "*** Suplementos ***"
                "\n"+
                f"\nBeneficio por Muerte Accidental. - Igual o menor que el beneficio por fallecimiento hasta un máximo de 150,000."+
                "\n"+
                f"\nSeguro para cónyuge u otro asegurado - Monto igual o menor que el beneficio por fallecimiento de la póliza."+
                "\n"+
                f"\nBeneficio por muerte en caso de enfermedad terminal - Hasta un máximo de un 50% de la suma asegurada."+
                "\n"+
                f"\nGastos Funerarios - Hasta un máximo de RD$ 1,250,000."+
                "\n"+
                f"\nIncapacidad Total y Permanente - La suma asegurada será pagadera en 24 cuotas mensuales continuas de igual monto a partir de agotar el período de espera de seis meses"
            ))
        
        def guardian_info():
            messagebox.showinfo("Guardian", (
                "El Seguro de vida a término con devolución de prima se utiliza para cubrir las necesidades de protección financiera de su familia durante un período de tiempo específico. Este producto ofrece una cobertura con primas niveladas por la duración de la póliza. Esta póliza no sólo proveerá recursos financieros a su familia en caso de muerte prematura, sino que, además, al final del período de afiliación reembolsará todas las primas pagadas si no hay reclamaciones pendientes en la póliza debido a la muerte del asegurado."+
                "\n"
                f"\nLa cantidad a recibir al final del periodo asegurado es fija y no depende de las fluctuaciones en las tasas de interés o en los mercados de capitales."
                "\n"
                f"\nLa prima inicial para la protección es baja, en comparación con otros tipos de pólizas. Esto se debe a que sólo es válida por un tiempo limitado. Las primas pueden aumentar si la póliza de seguro se extiende después del plazo inicialmente contratado."
            ))
        
        def guardian_characteristicas():
            messagebox.showinfo("Guardian", (
                "*** Características ***"+
                "\n"+
                f"\nEdad de Suscripción - Planes disponibles para personas desde 3 meses hasta 65 años de edad."+
                "\n"+
                f"\nPeríodo asegurado y extension de cobertura - Cobertura garantizada durante el período de cobertura seleccionada, que puede ser un Período Flexible de Cobertura: 5 a 30 años. Puede extender su cobertura después del período asegurado inicial con primas variables."+
                "\n"+
                f"\nPrimas - Primas fijas acorde a lo definido en el contrato."+
                "\n"+
                f"\nFrecuencia de pago - Semestral y Anual."+
                "\n"+
                f"\nBeneficios - Mínimo de $250,000 – Máximo de $1,250,000 RD$  (Pesos dominicanos)."
            ))
            
        def guardian_suplements():
            messagebox.showinfo("Guardian", (
                "*** Suplementos ***"
                "\n"+
                f"\nBeneficio por Muerte Accidental. - Igual o menor que el beneficio por fallecimiento hasta un máximo de 150,000."+
                "\n"+
                f"\nSeguro para cónyuge u otro asegurado - Monto igual o menor que el beneficio por fallecimiento de la póliza."+
                "\n"+
                f"\nBeneficio por muerte en caso de enfermedad terminal - Hasta un máximo de un 50% de la suma asegurada."+
                "\n"+
                f"\nGastos Funerarios - Hasta un máximo de RD$ 1,250,000."+
                "\n"+
                f"\nIncapacidad Total y Permanente - La suma asegurada será pagadera en 24 cuotas mensuales continuas de igual monto a partir de agotar el período de espera de seis meses"
            ))
        
        def guardianplus_info():
            messagebox.showinfo("Guardian Plus", (
                "El Seguro de vida a término con devolución de prima se utiliza para cubrir las necesidades de protección financiera de su familia durante un período de tiempo específico. Este producto ofrece una cobertura con primas niveladas por la duración de la póliza. Esta póliza no sólo proveerá recursos financieros a su familia en caso de muerte prematura, sino que, además, al final del período de afiliación reembolsará todas las primas pagadas si no hay reclamaciones pendientes en la póliza debido a la muerte del asegurado."+
                "\n"
                f"\nLa cantidad a recibir al final del periodo asegurado es fija y no depende de las fluctuaciones en las tasas de interés o en los mercados de capitales."
                "\n"
                f"\nLa prima inicial para la protección es baja, en comparación con otros tipos de pólizas. Esto se debe a que sólo es válida por un tiempo limitado. Las primas pueden aumentar si la póliza de seguro se extiende después del plazo inicialmente contratado."
            ))
        
        def guardianplus_characteristicas():
            messagebox.showinfo("Guardian Plus", (
                "*** Características ***"+
                "\n"+
                f"\nEdad de Suscripción - Planes disponibles para personas desde 3 meses hasta 65 años de edad."+
                "\n"+
                f"\nPeríodo asegurado y extension de cobertura - Cobertura garantizada durante el período de cobertura seleccionada, que puede ser un Período Flexible de Cobertura: 5 a 30 años. Puede extender su cobertura después del período asegurado inicial con primas variables."+
                "\n"+
                f"\nPrimas - Primas fijas acorde a lo definido en el contrato."+
                "\n"+
                f"\nFrecuencia de pago - Semestral y Anual."+
                "\n"+
                f"\nBeneficios - Guardián Plus: Mínimo de $1.25 millones – Máximo de $90millones  (Pesos dominicanos). En dólares americanos mínimo US$ 25,000.00 máximo US$ 90millones"
            ))
            
        def guardianplus_suplements():
            messagebox.showinfo("Guardian Plus", (
                "*** Suplementos ***"
                "\n"+
                f"\nBeneficio por Muerte Accidental. - Igual o menor que el beneficio por fallecimiento hasta un máximo de 150,000."+
                "\n"+
                f"\nSeguro para cónyuge u otro asegurado - Monto igual o menor que el beneficio por fallecimiento de la póliza."+
                "\n"+
                f"\nBeneficio por muerte en caso de enfermedad terminal - Hasta un máximo de un 50% de la suma asegurada."+
                "\n"+
                f"\nGastos Funerarios - Hasta un máximo de RD$ 1,250,000."+
                "\n"+
                f"\nIncapacidad Total y Permanente - La suma asegurada será pagadera en 24 cuotas mensuales continuas de igual monto a partir de agotar el período de espera de seis meses"
            ))
            
        def vidacredito_info():
            messagebox.showinfo("Vida Crédito", (
                "Atlántica Seguros, S.A. ofrece un seguro de vida dirigido a los clientes de cualquier entidad financiera que soliciten un préstamo de consumo, hipotecario o de vehículo."+
                "\n"
                f"\nEl seguro cubre el saldo de sus obligaciones en caso de fallecimiento, con el fin de proteger el patrimonio de su familia."
                "\n"
                f"\nEsta póliza le permite: Cubrir deudas que usted tenga con la entidad financiera, al momento de su fallecimiento. En caso de un accidente fatal o una muerte inesperada, su familia y seres queridos quedarán protegidos económicamente."
            ))
        
        def vidacredito_characteristics():
            messagebox.showinfo("Vida Crédito", (
                "*** Características ***"+
                "\n"+
                f"\nEligibilidad - Todos los deudores del acreedor y los clientes del crédito serán elegibles para ser asegurados, siempre y cuando cumplan el proceso de suscripción. Podrá incluirse, en consideración a una prima adicional, la vida del cónyuge, como deudor colateral cuando sea declarado a la compañía, si cumple con los requisitos."+
                "\n"+
                f"\nPrimas - Primas fijas durante la vigencia de la póliza."+
                "\n"+
                f"\nPeriodo de Contribución - Durante la vigencia de la póliza, según el periodo asegurable escogido."+
                "\n"+
                f"\nPeriodo Asegurable - Este seguro tendrá vigencia durante el periodo de contribución del préstamo cuyo interés asegura, desde el desembolso hasta la finalización del crédito. Este periodo asegurable podrá extenderse, si se modifica el periodo de contribución del préstamo coexistente."+
                "\n"+
                f"\nMoneda - Pesos Dominicanos (DOP) / Dólares Estadounidenses (USD)"
            ))
            
        def vidacredito_suplements():
            messagebox.showinfo("Vida Crédito", (
                "*** Suplementos ***"
                "\n"+
                f"\nPago por incapacidad total y permanente	- Pago de la suma asegurada en 24 mensualidades consecutivas de igual monto al transcurrir 6 meses en que el asegurado permanece con un diagnóstico de incapacidad total y permanente. En caso de fallecimiento durante el transcurso del pago de las mensualidades, los beneficiarios recibirán un pago único por el monto de la suma asegurada menos las mensualidades pagadas por incapacidad total. Pago de beneficio cesará a partir del mes en que el asegurado recupera capacidad productiva y laboral."+
                "\n"+
                f"\nAsegurado Adicional	- La inclusión de un asegurado adicional puede ser seleccionada para cónyuge u otro asegurado."
            ))            
        
        def vidabeca_info():
            messagebox.showinfo("Vida Beca", (
                "Atlantica Seguros, S.A. ofrece el seguro de Vida Beca diseñado para garantizar la educación primaria, secundaria, universitaria y/o de postgrado de los beneficiarios designados, en caso de muerte del asegurado, proveyéndoles de una anualidad que incluye:"+
                "\n"+
                f"\n* Pagos de matrículas para estudios en instituciones reconocidas y aprobadas por el Ministerio de Educación de la República Dominicana (MINERD)."+
                "\n"+
                f"\n* Pagos para materiales educativos (libros y otros)."
                "\n"+
                f"\n* Gastos de nutrición y hospedaje en caso de estudios en ciudades fuera de la residencia principal."+
                "\n"+
                f"\n* Gastos médicos del estudiante (Seguros de salud o tratamientos médicos)."+
                "\n"+
                f"\n* Otros gastos relacionados, pre-aprobados por la aseguradora."
            ))
        
        def vidabeca_characteristics():
            messagebox.showinfo("Vida Beca", (
                "*** Características ***"+
                "\n"+
                f"\nEligibilidad - Padres o representantes de estudiantes en instituciones reconocidas por el Ministerio de Educación de la República Dominicana."+
                "\n"+
                f"\nLimite de edad - Para el padre o representante la edad mínima de ingreso es de dieciocho (18) años y la máxima de sesenta y cinco (65) años. La edad máxima de permanencia es hasta los 75 años.Para el hijo/estudiante es de 0 a 25 años de edad."+
                "\n"+
                f"\nCobertura - Esta póliza puede cubrir la educación primaria, secundaria, universitaria y/o de posgrado de los beneficiarios, según se elija, en caso de fallecimiento del titular."+
                "\n"+
                f"\nPrimas - Primas niveladas por la duración de la póliza."+
                "\n"+
                f"\nSuma Asegurada - Variable. Esta suma dependerá de los montos anuales de educación, basados en promedios actuales en colegios privados de República Dominicana, incluyendo la tasa de inflación anual en el costo educativo, sujeto a los máximos descritos en el condicionado/cotización."+
                "\n"+
                f"\nPesos Dominicanos (DOP) / Dólares Estadounidenses (USD)"
            ))
            
        def vidabeca_suplements():
            messagebox.showinfo("Vida Beca", (
                "*** Suplementos ***"
                "\n"+
                f"\nPago anticipado de capital por invalidez total y permanente. - Si a consecuencia de una enfermedad o accidente el asegurado sufre una condición de invalidez total y permanente, la aseguradora pagará, en calidad de anticipo en vida, la suma asegurada contratada para la cobertura básica de fallecimiento después de transcurrido un período de espera de seis meses contados desde la fecha en que dicha condición haya sido diagnosticada. La suma asegurada será pagadera en 24 cuotas mensuales continuas de igual monto a partir de agotar el período de espera de seis meses."+
                "\n"+
                f"\nEstudios Universitarios fuera de su País de Residencia.	- Consiste en un suplemento que proporciona a los beneficiarios de un monto adicional a ser utilizado exclusivamente para realizar estudios fuera de su país de residencia."
            ))  
            
        def vidagrupo_info():
            messagebox.showinfo("Vida Grupo", (
                "Este seguro está diseñado para proveer protección a los empleados de una empresa o a los integrantes de un grupo asegurable, mediante una cobertura básica de vida que pagará a los beneficiarios del asegurado una suma contratada, en el evento de su fallecimiento. Las ventajas principales de un seguro de vida grupo son:"+
                "\n"+
                f"\n* Permite cubrir deudas u otros compromisos financieros que el asegurado pueda tener, al momento de su fallecimiento."+
                "\n"+
                f"\n* En caso de un accidente fatal o muerte inesperada, los familiares y seres queridos del asegurado recibirán una indemnización económica."
                "\n"+
                f"\n* Protege el patrimonio y los ahorros de la familia del asegurado."+
                "\n"+
                f"\n* Provee asistencia económica en el evento de una incapacidad que prive al asegurado de generar ingresos propios."
            ))
        
        def vidagrupo_characteristics():
            messagebox.showinfo("Vida Grupo", (
                "*** Características ***"+
                "\n"+
                f"\nEligibilidad - Empleados o personas que sean miembros de un grupo asegurable: Conjunto de personas que pertenezcan a una misma empresa o que mantengan un vínculo o interés que sea lícito, previo e independiente del contrato de seguro. Empleados en servicio activo, con una jornada laboral de tiempo completo. Este plan no ofrece cobertura para el cónyuge o los dependientes del asegurado o empleado."+
                "\n"+
                f"\nEdad de Suscripción - La edad mínima de aceptación en el seguro es de dieciocho (18) años y la máxima es de sesenta y cinco (65) años de edad. El seguro terminará cuando el asegurado cumpla los setenta y cinco (75) años de edad."+
                "\n"+
                f"\nPeríodo asegurado y extension de cobertura - Cobertura garantizada durante el período de cobertura seleccionada, que puede ser un Período Flexible de Cobertura: 5 a 30 años. Puede extender su cobertura despues del período asegurado inicial con primas variables."+
                "\n"+
                f"\nModalidad:	Contributivo: diez (10) miembros o setenta y cinco por ciento (75%) del grupo asegurable. No contributivo: cien por ciento (100%) de la nómina."+
                "\n"+
                f"\nBeneficiarios: El pago del beneficio se realizará a los beneficiarios designados por el asegurado o en su ausencia a los herederos legales."+
                "\n"+
                f"\nForma de pago del beneficio: Pago único o en plazos, sujeto a previo acuerdo con la aseguradora."+
                "\n"+
                f"\nMoneda - Pesos Dominicanos."
            ))
            
        def vidagrupo_suplements():
            messagebox.showinfo("Vida Grupo", (
                "*** Suplementos ***"
                "\n"+
                f"\nBeneficio por Muerte Accidental. - Igual o menor que el beneficio por fallecimiento hasta un máximo definido."+
                "\n"+
                f"\nIncapacidad Total y Permanente - La suma asegurada será pagadera en 24 cuotas mensuales continuas de igual monto a partir de agotar el período de espera de seis meses"+
                "\n"+
                f"\nBeneficio de gastos funerarios.	- Cubre los gastos funerarios."
            ))  
        
        def accpers_info():
            messagebox.showinfo("Accidentes Personales", (
                "Al contar con el seguro de accidentes personales de Atlántica Seguros, nuestros asegurados gozarán de los más amplios beneficios para atender los problemas financieros causados por su accidente."+
                "\n"+
                f"\nEste seguro:"+
                "\n"+
                f"\n * Válido en cualquier parte del mundo."+
                "\n"+
                f"\n * Tiene servicio disponible las 24 horas del día y durante todo el año."+
                "\n"+
                f"\n * Proteje contra cualquier hecho fortuito, tanto en actividades personales como profesionales."
            ))
            
        def accpers_characteristics():
            messagebox.showinfo("Accidentes Personales", (
                "*** Características ***"+
                "\n"+
                f"\nMuerte Accidental - Pago de cobertura por muerte accidental del asegurado."+
                "\n"+
                f"\nInvalidez Total y Permanente - Pago por invalidez total y permanente igual a la cobertura máxima."+
                "\n"+
                f"\Invalidez Permanente Parcial	- Pago parcial de la cobertura máxima por invalidez permanente parcial."                
            ))
            
        def accpers_suplements():
            messagebox.showinfo("Accidentes Personales", (
                "*** Suplementos ***"+
                "\n"+
                f"\nMuerte Accidental - Al morir en un accidente la compañía pagará una cantidad adicional basada en la cobertura seleccionada."+
                "\n"+
                f"\nIncapacidad  total y permanente - Pago de la suma asegurada en 24 mensualidades consecutivas de igual monto al transcurrir 6 meses en que el asegurado permanece con un diagnóstico de incapacidad total y permanente. En caso de fallecimiento durante el transcurso del pago de las mensualidades, los beneficiarios recibirán un pago único por el monto de la suma asegurada menos las mensualidades pagadas por incapacidad total. Pago de beneficio cesará a partir del mes en que el asegurado recupera capacidad productiva y laboral."+
                "\n"+
                f"\nReembolso de gastos médicos	- Si como consecuencia de un  accidente el asegurado debe someterse a un tratamiento médico, intervención quirúrgica, hospitalizarse, hacer uso de una ambulancia, servicios de enfermera, medicinas o estudios de laboratorio, se reembolsarán los gastos médicos ocurridos según lo establecido en  las condiciones de la póliza."+                
                "\n"+
                f"\nGastos funerarios - Este suplemento le provee una indemnización adicional para cubrir los gastos funerarios y de entierro."+
                "\n"+
                f"\nRenta diaria por hospitalización - En caso de Hospitalización a causa de un accidente o enfermedad la compañía aseguradora pagara al asegurado una renta diaria según el plan contratado"
            ))
        
        def autoatlantabasico_info():
            messagebox.showinfo("Auto Atlanta Básico", (
                "El plan Básico de protección para vehículos de Atlántica Seguros está diseñado especialmente para aquellos clientes que sólo necesitan un seguro que les permita estar en cumplimiento con la cobertura que exige la ley para poder transitar, sin necesidad de otros beneficios, sabiendo que obtienen el excelente servicio de calidad nacional que nos caracteriza."
            ))
            
        def autoatlantabasico_cobertura():
            messagebox.showinfo("Auto Atlanta Básico", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"
            ))
            
        def autoatlantabasico_suplements():
            messagebox.showinfo("Auto Atlanta Básico", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+
                "\n"
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nFianza judicial adicional - Puede incrementar la cantidad de Fianza judicial provista por el producto."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicópteros o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."
            ))
        
        def autoatlantabasico_conditions():
            messagebox.showinfo("Auto Atlanta Básico", (
                "*** Condiciones ***"+
                "\n"+
                f"\nLas informaciones y/o condiciones requeridas para contratar una póliza de vehículos son las siguientes:"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nTipo de cobertura solicitada."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante."+
                "\n"+
                f"\nMatrícula del vehículo."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))  
            
        def autoatlanticaultra_info():
            messagebox.showinfo("Auto Atlántica Ultra" , (
                "El plan de Protección Ultra para vehículos de Atlántica Seguros, además de la cobertura básica de Ley ampliada, le ofrece protección con un plan de asistencia vial más amplio y el excelente servicio de calidad nacional que nos caracteriza. Este plan es recomendado para aquellos conductores que necesitan estar en cumplimiento con la ley y a la vez contar con la protección de su patrimonio."
            ))      
        
        def autoatlanticaultra_cobertura():
            messagebox.showinfo("Auto Atlántica Ultra", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"
            ))
        
        def autoatlanticaultra_suplements():
            messagebox.showinfo("Auto Atlántica Ultra", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nFianza judicial adicional - Puede incrementar la cantidad de Fianza judicial provista por el producto."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en Helicópteros o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."                
            ))
        
        def autoatlanticaultra_conditions():
            messagebox.showinfo("Auto Atlántica Ultra", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nTipo de cobertura solicitada."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))
        
        def atlantarentacar_info():
            messagebox.showinfo("Auto Básico Rent-a-Car" , (
                "El plan Rent-a-Car de protección para vehículos de Atlántica Seguros, está diseñado especialmente para aquellos clientes de Rent-a-Car que sólo necesitan un seguro que les permita estar en cumplimiento con la cobertura que exige la ley para poder transitar, sin necesidad de otros beneficios, sabiendo que obtienen el excelente servicio de calidad nacional que nos caracteriza."
            ))      
        
        def atlantarentacar_cobertura():
            messagebox.showinfo("Auto Básico Rent-a-Car", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"
            ))
        
        def atlantarentacar_suplements():
            messagebox.showinfo("Auto Básico Rent-a-Car", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."            
            ))
        
        def atlantarentacar_conditions():
            messagebox.showinfo("Auto Básico Rent-a-Car", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nTipo de cobertura solicitada."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del (los) vehículo (s)."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))
        
        def autoatlanticatotal_info():
            messagebox.showinfo("Auto Atlántica Total" , (
                "El plan de Protección Total para vehículos ofrece además de cobertura básica de Ley o con limites ampliados, el respaldo frente a riesgos como colisión, vuelco, incendio y robo a vehículos con 20 años de fabricación, mediante un valor pactado del vehículo. Además, ponemos a su disposición una serie de beneficios que permitirán desenvolverse con mayor facilidad en caso de eventualidades."
            ))      
        
        def autoatlanticatotal_cobertura():
            messagebox.showinfo("Auto Atlántica Total", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco."+
                "\n"+
                f"\nIncendio y robo."+
                "\n"+
                f"\nRotura de cristales."
            ))
        
        def autoatlanticatotal_suplementos():
            messagebox.showinfo("Auto Atlántica Total", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nFianza judicial adicional - Puede incrementar la cantidad de Fianza judicial provista por el producto."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicópteros o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."
            ))
        
        def autoatlanticatotal_condiciones():
            messagebox.showinfo("Auto Atlántica Total", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nTipo de cobertura solicitada."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del (los) vehículo (s)."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))
        
        def autoatlanticatotalplus_info():
            messagebox.showinfo("Auto Atlántica Total Plus" , (
                "El plan de Protección Total Plus para vehículos de Atlántica Seguros provee una protección completa para vehículos hasta 10 años de fabricación. La cobertura comprensiva hace de este plan una opción razonable para disfrutar de una seguridad plena. Además, ponemos a su disposición una serie de beneficios que permitirán desenvolverse con mayor facilidad en caso de eventualidades."
            ))      
        
        def autoatlanticatotalplus_cobertura():
            messagebox.showinfo("Auto Atlántica Total Plus", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRiesgo comprensivo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRotura accidental de cristales."
            ))
        
        def autoatlanticatotalplus_suplementos():
            messagebox.showinfo("Auto Atlántica Total Plus", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nRenta de vehículo - Hasta 5 días por año con opción de aumentar el tiempo de renta hasta 15 días."+
                "\n"+
                f"\nLimitación geográfica - Cubre al vehículo asegurado con seguro de daños propios en el país vecino de Haití por un periodo de 30 días. con notificación previa a la aseguradora."+
                "\n"+
                f"\nTaller autorizado - Acceso a una exclusiva red de talleres autorizados, para conservar la garantía de su vehículo."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."+
                "\n"+
                f"\nAditamientos especiales o electrónicos - Cobertura adicional para equipo especial o electrónico previa declaración."+
                "\n"+
                f"\nRobo o perdida de llaves de vehículo - Aplica para Vehículos de hasta 3 años. Cubre hasta un límite máximo de RD$10,000.00 por perdida robo de la llave principal del vehículo asegurado, con un deducible de RD$500.00, y 2 eventos en el año póliza."+
                "\n"+
                f"\nAuto exceso - Posibilidad de aumentar tu cobertura de responsabilidad civil, hasta limites aceptados."
            ))
        
        def autoatlanticatotalplus_condiciones():
            messagebox.showinfo("Auto Atlántica Total Plus", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nVehículos con 10 años de fabricación o menos."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo o acto de venta a nombre de solicitante."+
                "\n"+
                f"\nPago inicial del 25% del valor de prima. Y acuerdo de pago del restante."
            ))
            
        def autoatlanticavip_info():
            messagebox.showinfo("Auto Atlántica VIP" , (
                "El plan de protección VIP, le ofrece la cobertura más completa disponible para vehículos y el mejor servicio de asistencia, especialmente diseñado para que nuestros clientes puedan transitar con la tranquilidad de saber que cuentan con la mejor protección ante cualquier inconveniente que involucre al vehículo asegurado, a los pasajeros o a terceros. Es para vehículos hasta 3 años de fabricación y tiene el beneficio de no aplicación de deducibles."
            ))      
        
        def autoatlanticavip_cobertura():
            messagebox.showinfo("Auto Atlántica VIP", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."                
            ))
        
        def autoatlanticavip_suplements():
            messagebox.showinfo("Auto Atlántica VIP", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nRenta de vehículo - 15 días por año."+
                "\n"+
                f"\nLimitación geográfica - Cubre al vehículo asegurado con seguro de daños propios en el país vecino de Haití por un periodo de 30 días con notificación previa a la aseguradora."+
                "\n"+
                f"\nTaller autorizado - Acceso a una exclusiva red de talleres autorizados, para conservar la garantía de su vehículo."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."+
                "\n"+
                f"\nAditamientos especiales o electrónicos - Cobertura adicional para equipo especial o electrónico previa declaración."+
                "\n"+
                f"\nRobo o perdida de llaves de vehículo - Aplica para Vehículos de hasta 3 años. Cubre hasta un límite máximo de RD$10,000.00 por perdida robo de la llave principal del vehículo asegurado, con un deducible de RD$500.00, y 2 eventos en el año póliza."+
                "\n"+
                f"\nAuto exceso - Posibilidad de aumentar tu cobertura de responsabilidad civil, hasta limites aceptados."
            ))
        
        def autoatlanticavip_conditions():
            messagebox.showinfo("Auto Atlántica VIP", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nVehículos con 3 años de fabricación o menos."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo o acto de venta a nombre de solicitante."+
                "\n"+
                f"\nPago inicial del 25% del valor de prima. Y acuerdo de pago del restante."
            )) 
        
        def autoatlantica0km_info():
            messagebox.showinfo("Auto Atlántica 0KM" , (
                "El plan de protección 0 km ofrece la cobertura más completa disponible, especialmente diseñado para vehículos del año, adquiridos nuevos y con cero kilómetros. Nuestro plan de 0 km ofrece opciones de deducibles desde 0% hasta 5%."
            ))      
        
        def autoatlantica0km_cobertura():
            messagebox.showinfo("Auto Atlántica 0KM", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRiesgo comprensivo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRotura accidental de cristales."                
            ))
        
        def autoatlantica0km_suplements():
            messagebox.showinfo("Auto Atlántica 0KM", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nRenta de vehículo - 15 días por año."+
                "\n"+
                f"\nLimitación geográfica - Cubre al vehículo asegurado con seguro de daños propios en el país vecino de Haití por un periodo de 30 días con notificación previa a la aseguradora."+
                "\n"+
                f"\nTaller autorizado - Acceso a una exclusiva red de talleres autorizados, para conservar la garantía de su vehículo."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."+
                "\n"+
                f"\nAditamientos especiales o electrónicos - Cobertura adicional para equipo especial o electrónico previa declaración."+
                "\n"+
                f"\nRobo o perdida de llaves de vehículo - Aplica para Vehículos de hasta 3 años. Cubre hasta un límite máximo de RD$10,000.00 por perdida robo de la llave principal del vehículo asegurado, con un deducible de RD$500.00, y 2 eventos en el año póliza."+
                "\n"+
                f"\nAuto exceso - Posibilidad de aumentar tu cobertura de responsabilidad civil, hasta limites aceptados."
            ))
        
        def autoatlantica0km_conditions():
            messagebox.showinfo("Auto Atlántica 0KM", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+                
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo o acto de venta a nombre de solicitante."+
                "\n"+
                f"\nPago inicial del 25% del valor de prima. Y acuerdo de pago del restante."
            ))
            
        def autoatlanticaseriem_info():
            messagebox.showinfo("Auto Atlántica Serie M" , (
                "Serie M es un seguro diseñado específica y exclusivamente para mujeres conductoras, que poseen vehículos con 10 años de fabricación o menos para brindarles la mejor protección, servicio y asistencia ante los inconvenientes que se le puedan presentar con su vehículo o en la carretera, de modo que siempre estén amparadas bajo la cobertura de Atlántica Seguros, S. A."
            ))      
        
        def autoatlanticaseriem_cobertura():
            messagebox.showinfo("Auto Atlántica Serie M", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRiesgo comprensivo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRotura accidental de cristales."                
            ))
        
        def autoatlanticaseriem_suplements():
            messagebox.showinfo("Auto Atlántica Serie M", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nRenta de vehículo - Hasta 5 días por año con opción de aumentar el tiempo de renta hasta 15 días."+
                "\n"+
                f"\nLimitación geográfica - Cubre al vehículo asegurado con seguro de daños propios en el país vecino de Haití por un periodo de 30 días con notificación previa a la aseguradora."+
                "\n"+
                f"\nTaller autorizado - Acceso a una exclusiva red de talleres autorizados, para conservar la garantía de su vehículo."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."+
                "\n"+
                f"\nAditamientos especiales o electrónicos - Cobertura adicional para equipo especial o electrónico previa declaración."+
                "\n"+
                f"\nCirugía Facial Reconstructiva a Causa de un Accidente de Tránsito - cubre hasta 200,000 pesos para reembolsar honorarios y gastos médicos, si a consecuencia de algún accidente de tránsito la asegurada queda lesionada en el rostro o cuello y requiere cirugía fácil reconstructiva, durante un periodo de 90 días de la ocurrencia de dicho accidente."+
                "\n"+
                f"\nCobertura de Cáncer Femenino - cubre hasta 500,000pesos para gastos médicos a la asegurada si en el año póliza es diagnosticada por primera vez con un cáncer femenino (ovarios, mama, útero, cérvix, endometrio) el monto se paga por reembolso."+
                "\n"+
                f"\nBono por buena experiencia - si al momento de la renovación la asegura no reporto ningún siniestro se le otorgará un bono por buena experiencia que estipulará en departamento de renovación."+
                "\n"+
                f"\nAsistencia en Línea en el hogar - la asegurada contara con asistencia vía telefónica ante cualquier eventualidad que pueda presentar en el hogar."+
                "\n"+
                f"\nAuto exceso - Posibilidad de Aumentar tu cobertura de Responsabilidad Civil, hasta límites aceptados."
            ))
        
        def autoatlanticaseriem_conditions():
            messagebox.showinfo("Auto Atlántica Serie M", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+                
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo o acto de venta a nombre de solicitante."+
                "\n"+
                f"\nPago inicial del 25% del valor de prima. Y acuerdo de pago del restante."
            )) 
        
        def autoatlanticaeconomax_info():
            messagebox.showinfo("Auto Atlántica Econo Max" , (
                "El plan de Protección Econo Max para vehículos de Atlántica Seguros, provee una protección completa que usted puede adquirir para su vehículo con muchos años de uso (este plan cubre vehículos manufacturados hace más de 10 años, si es 10 o menos años, puede cubrir su vehículo con nuestro plan Auto Atlántica Total Plus). La cobertura comprensiva hace de este plan una opción razonable para disfrutar de una seguridad plena, y los beneficios incluidos pueden ser ampliados a través de suplementos adicionales de acuerdo a sus necesidades, para que su plan le provea una cobertura personalizada, seguridad completa y una de las ofertas de servicio más amplias en el mercado."
            ))      
        
        def autoatlanticaeconomax_cobertura():
            messagebox.showinfo("Auto Atlántica Econo Max", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRiesgo comprensivo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRotura accidental de cristales."                
            ))
        
        def autoatlanticaeconomax_suplements():
            messagebox.showinfo("Auto Atlántica Econo Max", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nRenta de vehículo - Hasta 5 días por año con opción de aumentar el tiempo de renta hasta 15 días."+
                "\n"+
                f"\nLimitación geográfica - Cubre al vehículo asegurado con seguro de daños propios en el país vecino de Haití por un periodo de 30 días con notificación previa a la aseguradora."+
                "\n"+
                f"\nTaller autorizado - Acceso a una exclusiva red de talleres autorizados, para conservar la garantía de su vehículo."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."+
                "\n"+
                f"\nAditamientos especiales o electrónicos - Cobertura adicional para equipo especial o electrónico previa declaración."+
                "\n"+                
                f"\nAuto exceso - Posibilidad de Aumentar tu cobertura de Responsabilidad Civil, hasta límites aceptados."
            ))
        
        def autoatlanticaeconomax_conditions():
            messagebox.showinfo("Auto Atlántica Econo Max", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+                
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo o acto de venta a nombre de solicitante."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))
        
        def autoatlanticataxirenta_info():
            messagebox.showinfo("Auto Atlántica Taxi/Renta" , (
                "Los planes de Protección Taxi y Rent-a-Car para vehículos de Atlántica Seguros, provee una protección completa en responsabilidad civil y daños propios que usted puede adquirir para su vehículo de Taxi o de Rent-a-Car, hasta 10 años."
            ))      
        
        def autoatlanticataxirenta_cobertura():
            messagebox.showinfo("Auto Atlántica Taxi/Renta", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+
                "\n"+
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRiesgo comprensivo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRotura accidental de cristales."                
            ))
        
        def autoatlanticataxirenta_suplements():
            messagebox.showinfo("Auto Atlántica Taxi/Renta", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+                
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."      
            ))
        
        def autoatlanticataxirenta_conditions():
            messagebox.showinfo("Auto Atlántica Taxi/Renta", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+                
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula del vehículo o acto de venta a nombre de solicitante."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))
        
        def atlantamotoresbasico_info():
            messagebox.showinfo("Motores Atlanta Básico" , (
                "Los planes de Protección Taxi y Rent-a-Car para vehículos de Atlántica Seguros, provee una protección completa en responsabilidad civil y daños propios que usted puede adquirir para su vehículo de Taxi o de Rent-a-Car, hasta 10 años."
            ))              
        
        def atlantamotoresbasico_suplements():
            messagebox.showinfo("Motores Atlanta Básico", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+            
                "\n"+                
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con la motocicleta asegurada. Solo aplica las motocicletas de 625 CC en adelante."      
            ))
        
        def atlantamotoresbasico_conditions():
            messagebox.showinfo("Motores Atlanta Básico", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+                
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula de la motocicleta"+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))
        
        def atlantamotoresdeportivo_info():
            messagebox.showinfo("Motores Atlanta Deportivo" , (
                "Los planes de Protección Taxi y Rent-a-Car para vehículos de Atlántica Seguros, provee una protección completa en responsabilidad civil y daños propios que usted puede adquirir para su vehículo de Taxi o de Rent-a-Car, hasta 10 años."
            ))              
        
        def atlantamotoresdeportivo_cobertura():
            messagebox.showinfo("Motores Atlanta Deportivo", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+            
                "\n"+                
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nFianza judicial"        
            ))           
        
        def atlantamotoresdeportivo_conditions():
            messagebox.showinfo("Motores Atlanta Deportivo", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+                
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante"+
                "\n"+
                f"\nMatrícula de la motocicleta"+
                "\n"+
                f"\nPago inicial del 30% del valor de prima."
            ))
        
        def atlantamotorestotalplus_info():
            messagebox.showinfo("Motores Atlanta Total Plus" , (
                "El plan de Protección Motores Total Plus para vehículos de Atlántica Seguros está dirigido a clientes individuales o empresas propietarios de motocicletas de uso privado que tengan un cilindraje de 125 cc en adelante. Se cubren motores hasta 10 años de fabricación dividido en dos rangos, de 0 a 5 años, y de 6 a 10 años."
            ))              
        
        def atlantamotorestotalplus_cobertura():
            messagebox.showinfo("Motores Atlanta Total Plus", (
                "*** Cobertura ***"+
                "\n"+
                f"\nDaños a la propiedad ajena"+            
                "\n"+                
                f"\nLesiones o muerte a un tercero."+
                "\n"+
                f"\nLesiones o muerte a más de un tercero."+
                "\n"+
                f"\nLesiones o muerte a un pasajero."+
                "\n"+
                f"\nLesiones o muerte a más de un pasajero."+
                "\n"+
                f"\nIndemnización por accidente personal al conductor."+
                "\n"+
                f"\nFianza judicial"+
                "\n"+
                f"\nColisión y vuelco hasta el monto del valor del vehículo."+
                "\n"+
                f"\nIncendio y/o robo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRiesgo comprensivo hasta el monto del valor del vehículo."+
                "\n"+
                f"\nRotura accidental de cristales."
            ))           
        
        def atlantamotorestotalplus_suplements():
            messagebox.showinfo("Motores Atlanta Total Plus", (
                "*** Suplementos ***"+
                "\n"+
                f"\nCasa del Conductor - Le permite agilizar los trámites necesarios para reportar el accidente y notificarnos, para fines de cobertura y reclamos."+
                "\n"+                
                f"\nAsistencia Vial	- Le rescatamos ante cualquier eventualidad que se le presente con el vehículo asegurado."+
                "\n"+
                f"\nAeroambulancia - Provee asistencia al conductor del vehículo y sus pasajeros de traslados y atención médica de emergencia en helicóptero o ambulancia en caso de ocurrir un accidente automovilístico en cualquier ubicación de todo el territorio nacional."            
            ))
            
        def atlantamotorestotalplus_conditions():
            messagebox.showinfo("Motores Atlanta Total Plus", (
                "*** Condiciones ***"+
                "\n"+
                f"\nNombre del solicitante."+
                "\n"+
                f"\nMotocicletas con 10 años de fabricación o menos."+
                "\n"+
                f"\nDatos personales del solicitante."+
                "\n"+
                f"\nCédula del solicitante."+
                "\n"+
                f"\nLicencia de conducir vigente del solicitante."+
                "\n"+
                f"\nMatrícula o acto de venta a nombre del solicitante."+
                "\n"+
                f"\nPago inicial del 30% del valor de prima. Y acuerdo de pago del restante."
            ))

        # selector atlantica
        # atlantica page selector #
        F3_Menu=LabelFrame(self.root,bg=bg_color)
        F3_Menu.place(x=0,y=267,width=925,height=24)      
        
        def f3_2():            
            F3_2.lift()
        
        def f3_3():
            F3_3.lift()
            
        def f3_4():
            F3_4.lift()
        
        def f3_5():
            F3_5.lift()
            
        def f3_6():
            F3_6.lift()
        
        def f3_1():
            F3.lift()
            
        F3_page1=Button(F3_Menu,text="1",command=f3_1,font="arial 12 bold").place(x=0,y=0,width=175,height=24)
        F3_page2=Button(F3_Menu,text="2",command=f3_2,font="arial 12 bold").place(x=175,y=0,width=172,height=24)
        F3_page3=Button(F3_Menu,text="3",command=f3_3,font="arial 12 bold").place(x=347,y=0,width=172,height=24)        
        F3_page4=Button(F3_Menu,text="4",command=f3_4,font="arial 12 bold").place(x=519,y=0,width=172,height=24)       
        F3_page5=Button(F3_Menu,text="5",command=f3_5,font="arial 12 bold").place(x=691,y=0,width=110,height=24)                
        F3_page6=Button(F3_Menu,text="6",command=f3_6,font="arial 12 bold").place(x=801,y=0,width=122,height=24)                
            
        F3_2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Salud Atlántica",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3_2.place(x=0,y=290,width=925,height=260)
        
        F3_3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Vehículos Atlántica",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3_3.place(x=0,y=290,width=925,height=260)
        
        F3_4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Vehículos Atlántica",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3_4.place(x=0,y=290,width=925,height=260)
        
        F3_5=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Vehículos Atlántica",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3_5.place(x=0,y=290,width=925,height=260)
        
        F3_6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Vehículos Atlántica",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3_6.place(x=0,y=290,width=925,height=260)
    
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes de Salud Atlántica",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=0,y=290,width=925,height=260)
        
        orion_lbl=Label(F3,text="Orion", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        orion_txt=Entry(F3, width=2,textvariable=self.orion,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        orion_info1=Button(F3,text="Info.",command=orion_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        orion_info2=Button(F3,text="Características",command=orion_characteristics,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        orion_info3=Button(F3,text="Suplementos",command=orion_suplements,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        
        orionplus_lbl=Label(F3,text="Orion Plus", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        orionplus_txt=Entry(F3, width=2,textvariable=self.orion_plus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        orionplus_info1=Button(F3,text="Info.",command=orionplus_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        orionplus_info2=Button(F3,text="Características",command=orionplus_characteristics,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        orionplus_info3=Button(F3,text="Suplementos",command=orionplus_suplements,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        
        guardian_lbl=Label(F3,text="Guardian", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        guardian_txt=Entry(F3, width=2,textvariable=self.guardian,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        guardian_info1=Button(F3,text="Info.",command=guardian_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        guardian_info2=Button(F3,text="Características",command=guardian_characteristicas,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        guardian_info3=Button(F3,text="Suplementos",command=guardian_suplements,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")        
        
        guardianplus_lbl=Label(F3,text="Guardian Plus", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        guardianplus_txt=Entry(F3, width=2,textvariable=self.guardian_plus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        guardianplus_info1=Button(F3,text="Info.",command=guardianplus_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        guardianplus_info2=Button(F3,text="Características",command=guardianplus_characteristicas,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        guardianplus_info3=Button(F3,text="Suplementos",command=guardianplus_suplements,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")                
        
        vidacredito_lbl=Label(F3_2,text="Vida Crédito", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        vidacredito_txt=Entry(F3_2, width=2,textvariable=self.vida_credito,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        vidacredito_info1=Button(F3_2,text="Info.",command=vidacredito_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        vidacredito_info2=Button(F3_2,text="Características",command=vidacredito_characteristics,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        vidacredito_info3=Button(F3_2,text="Suplementos",command=vidacredito_suplements,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        
        healthplan2_lbl=Label(F3_2,text="Plan de Salud", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=5, padx=10, pady=10, sticky="w")
        healthplan2_txt=Entry(F3_2, width=2,textvariable=self.healthplan,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=6,padx=10,pady=10)     
        
        vidabeca_lbl=Label(F3_2,text="Vida Beca", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        vidabeca_txt=Entry(F3_2, width=2,textvariable=self.vida_beca,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        vidabeca_info1=Button(F3_2,text="Info.",command=vidabeca_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        vidabeca_info2=Button(F3_2,text="Características",command=vidabeca_characteristics,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        vidabeca_info3=Button(F3_2,text="Suplementos",command=vidabeca_suplements,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        
        vidagrupo_lbl=Label(F3_2,text="Vida Grupo", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        vidagrupo_txt=Entry(F3_2, width=2,textvariable=self.vida_grupo,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        vidagrupo_info1=Button(F3_2,text="Info.",command=vidagrupo_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        vidagrupo_info2=Button(F3_2,text="Características",command=vidagrupo_characteristics,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        vidagrupo_info3=Button(F3_2,text="Suplementos",command=vidagrupo_suplements,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")        
        
        accpers_lbl=Label(F3_2,text="Accidentes Personales", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        accpers_txt=Entry(F3_2, width=2,textvariable=self.acc_pers,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        accpers_info1=Button(F3_2,text="Info.",command=accpers_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        accpers_info2=Button(F3_2,text="Características",command=accpers_characteristics,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        accpers_info3=Button(F3_2,text="Suplementos",command=accpers_suplements,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")        
        
        autoatlantabasico_lbl=Label(F3_3,text="Atlanta Básico", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        autoatlantabasico_txt=Entry(F3_3, width=2,textvariable=self.autoatlanta_basico,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        autoatlantabasico_info1=Button(F3_3,text="Info.",command=autoatlantabasico_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        autoatlantabasico_info2=Button(F3_3,text="Cobertura",command=autoatlantabasico_cobertura,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        autoatlantabasico_info3=Button(F3_3,text="Suplementos",command=autoatlantabasico_suplements,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        autoatlantabasico_info4=Button(F3_3,text="Condiciones",command=autoatlantabasico_conditions,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")                
        
        autoatlanticaultra_lbl=Label(F3_3,text="Atlántico Ultra", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        autoatlanticaultra_txt=Entry(F3_3, width=2,textvariable=self.autoatlanta_ultra,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        autoatlanticaultra_info1=Button(F3_3,text="Info.",command=autoatlanticaultra_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        autoatlanticaultra_info2=Button(F3_3,text="Cobertura",command=autoatlanticaultra_cobertura,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        autoatlanticaultra_info3=Button(F3_3,text="Suplementos",command=autoatlanticaultra_suplements,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        autoatlanticaultra_info4=Button(F3_3,text="Condiciones",command=autoatlanticaultra_conditions,font="arial 12 bold").grid(row=1,column=5,padx=10,pady=10,sticky="w")                        
        
        atlanticorentacar_lbl=Label(F3_3,text="Atlántico Rent-a-car", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        atlanticorentacar_txt=Entry(F3_3, width=2,textvariable=self.atlantico_rentacar,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        atlanticorentacar_info1=Button(F3_3,text="Info.",command=atlantarentacar_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        atlanticorentacar_info2=Button(F3_3,text="Cobertura",command=atlantarentacar_cobertura,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        atlanticorentacar_info3=Button(F3_3,text="Suplementos",command=atlantarentacar_suplements,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")        
        atlanticorentacar_info4=Button(F3_3,text="Condiciones",command=atlantarentacar_conditions,font="arial 12 bold").grid(row=2,column=5,padx=10,pady=10,sticky="w")                
        
        autoatlanticatotal_lbl=Label(F3_3,text="Atlántica Total", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        autoatlanticatotal_txt=Entry(F3_3, width=2,textvariable=self.atlantico_total,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        autoatlanticatotal_info1=Button(F3_3,text="Info.",command=autoatlanticatotal_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        autoatlanticatotal_info2=Button(F3_3,text="Cobertura",command=autoatlanticatotal_cobertura,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        autoatlanticatotal_info3=Button(F3_3,text="Suplementos",command=autoatlanticatotal_suplementos,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")        
        autoatlantatotal_info4=Button(F3_3,text="Condiciones",command=autoatlanticatotal_condiciones,font="arial 12 bold").grid(row=3,column=5,padx=10,pady=10,sticky="w")                
        
        autoatlantatotalplus_lbl=Label(F3_4,text="Altanta Total Plus", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        autoatlantatotalplus_txt=Entry(F3_4, width=2,textvariable=self.atlantico_totalplus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        autoatlantatotalplus_info1=Button(F3_4,text="Info.",command=autoatlanticatotalplus_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        autoatlantatotalplus_info2=Button(F3_4,text="Cobertura",command=autoatlanticatotalplus_cobertura,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        autoatlantatotalplus_info3=Button(F3_4,text="Suplementos",command=autoatlanticatotalplus_suplementos,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        autoatlantatotalplus_info4=Button(F3_4,text="Condiciones",command=autoatlanticatotalplus_condiciones,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")                
        
        autoatlantavip_lbl=Label(F3_4,text="Atlántico VIP", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        autoatlantavip_txt=Entry(F3_4, width=2,textvariable=self.atlanta_vip,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        autoatlantavip_info1=Button(F3_4,text="Info.",command=autoatlanticavip_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        autoatlantavip_info2=Button(F3_4,text="Cobertura",command=autoatlanticavip_cobertura,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        autoatlantavip_info3=Button(F3_4,text="Suplementos",command=autoatlanticavip_suplements,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        autoatlantavip_info4=Button(F3_4,text="Condiciones",command=autoatlanticavip_conditions,font="arial 12 bold").grid(row=1,column=5,padx=10,pady=10,sticky="w")                    
        
        atlantico0km_lbl=Label(F3_4,text="Atlántico 0KM", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        atlantico0km_txt=Entry(F3_4, width=2,textvariable=self.atlanta_0km,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        atlantico0km_info1=Button(F3_4,text="Info.",command=autoatlantica0km_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        atlantico0km_info2=Button(F3_4,text="Cobertura",command=autoatlantica0km_cobertura,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        atlantico0km_info3=Button(F3_4,text="Suplementos",command=autoatlantica0km_suplements,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")        
        atlantico0km_info4=Button(F3_4,text="Condiciones",command=autoatlantica0km_conditions,font="arial 12 bold").grid(row=2,column=5,padx=10,pady=10,sticky="w")                
        
        atlanticoseriem_lbl=Label(F3_4,text="Atlántica Serie M (mujer)", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        atlanticoseriem_txt=Entry(F3_4, width=2,textvariable=self.atlanta_seriem,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        atlanticoseriem_info1=Button(F3_4,text="Info.",command=autoatlanticaseriem_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        atlanticoseriem_info2=Button(F3_4,text="Cobertura",command=autoatlanticaseriem_cobertura,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        atlanticoseriem_info3=Button(F3_4,text="Suplementos",command=autoatlanticaseriem_suplements,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")        
        atlanticoseriem_info4=Button(F3_4,text="Condiciones",command=autoatlanticaseriem_conditions,font="arial 12 bold").grid(row=3,column=5,padx=10,pady=10,sticky="w")                
        
        atlantaeconomax_lbl=Label(F3_5,text="Altanta Econo Max", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        atlantaeconomax_txt=Entry(F3_5, width=2,textvariable=self.atlanta_economax,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        atlantaeconomax_info1=Button(F3_5,text="Info.",command=autoatlanticaeconomax_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        atlantaeconomax_info2=Button(F3_5,text="Cobertura",command=autoatlanticaeconomax_cobertura,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        atlantaeconomax_info3=Button(F3_5,text="Suplementos",command=autoatlanticaeconomax_suplements,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        atlantaeconomax_info4=Button(F3_5,text="Condiciones",command=autoatlanticaeconomax_conditions,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")                
        
        atlantataxirenta_lbl=Label(F3_5,text="Atlántico Taxi/Renta", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        atlantataxirenta_txt=Entry(F3_5, width=2,textvariable=self.atlanta_taxirenta,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        atlantataxirenta_info1=Button(F3_5,text="Info.",command=autoatlanticataxirenta_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        atlantataxirenta_info2=Button(F3_5,text="Cobertura",command=autoatlanticataxirenta_cobertura,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        atlantataxirenta_info3=Button(F3_5,text="Suplementos",command=autoatlanticataxirenta_suplements,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        
        atlantataxirenta_info4=Button(F3_5,text="Condiciones",command=autoatlanticataxirenta_conditions,font="arial 12 bold").grid(row=1,column=5,padx=10,pady=10,sticky="w")                
                
        motoresatlantabasica_lbl=Label(F3_5,text="Motores Básico", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        motoresatlantabasica_txt=Entry(F3_5, width=2,textvariable=self.motoresatlanta_basico,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        motoresatlantabasica_info1=Button(F3_5,text="Info.",command=atlantamotoresbasico_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        motoresatlantabasica_info3=Button(F3_5,text="Suplementos",command=atlantamotoresbasico_suplements,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")        
        motoresatlantabasica_info4=Button(F3_5,text="Condiciones",command=atlantamotoresbasico_conditions,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")                
        
        motoresatlantadeportivo_lbl=Label(F3_5,text="Motores Deportivo", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        motoresatlantadeportivo_txt=Entry(F3_5, width=2,textvariable=self.motoresatlanta_deportivo,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        motoresatlantadeportivo_info1=Button(F3_5,text="Info.",command=atlantamotoresdeportivo_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        motoresatlantadeportivo_info2=Button(F3_5,text="Cobertura",command=atlantamotoresdeportivo_cobertura,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        motoresatlantadeportivo_info4=Button(F3_5,text="Condiciones",command=atlantamotoresdeportivo_conditions,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")                
        
        motoresatlanticototalplus_lbl=Label(F3_6,text="Motores Total Plus", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        motoresatlanticototalplus_txt=Entry(F3_6, width=2,textvariable=self.motoresatlanta_totalplus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        motoresatlanticototalplus_info1=Button(F3_6,text="Info.",command=atlantamotorestotalplus_info,font="arial 12 bold").grid(row=3,column=2,padx=10,pady=10,sticky="w")
        motoresatlanticototalplus_info2=Button(F3_6,text="Cobertura",command=atlantamotorestotalplus_cobertura,font="arial 12 bold").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        motoresatlanticototalplus_info3=Button(F3_6,text="Suplementos",command=atlantamotorestotalplus_suplements,font="arial 12 bold").grid(row=3,column=4,padx=10,pady=10,sticky="w")        
        motoresatlanticototalplus_info4=Button(F3_6,text="Condiciones",command=atlantamotorestotalplus_conditions,font="arial 12 bold").grid(row=3,column=5,padx=10,pady=10,sticky="w")                
        
    # fila de seguros monumental 3
    
        # monumental info #
        """ Unused
        def monumplanvida_info():
            messagebox.showinfo("Plan Vida", (
                "La Monumental de Seguros le garantiza que, en caso de fallecimiento, sus hijos(as) y su cónyuge estén cubiertos económicamente para enfrentar los compromisos existentes y la nueva vida familiar, aún con la falta de un ingreso mensual."
            ))
        
        def monumplanvida_auxcover():
            messagebox.showinfo("Plan Vida", (
                "*** Auxilia a Cubrir ***"+
                "\n"+
                f"\n-Pago de préstamos"+
                "\n"+
                f"\n-Pago de deudas pendientes"+
                "\n"+
                f"\n-Educación de los hijos(as)"+
                "\n"+
                f"\n-Estabilidad económica familiar"
            ))
            
        def monumplanvida_options():
            messagebox.showinfo("Plan Vida", (
                "*** El ciente tiene la opción de decidir: ***"+
                "\n"+
                f"\n-La suma asegurada"+
                "\n"+
                f"\n-La duración del plan"+
                "\n"+
                f"\n-Los beneficiarios"+
                "\n"+
                f"\n-La forma de liquidación"
            ))
            
        def monumplanvida_cover():
            messagebox.showinfo("Plan Vida", (
                "*** Coberturas ***"+
                "\n"+
                f"\n-Fallecimiento por causas naturales"+
                "\n"+
                f"\n-Fallecimiento accidental"+
                "\n"+
                f"\n-Desmembramiento"+
                "\n"+
                f"\n-Enfermedades graves"+
                "\n"+
                f"\n-Incapacidad total y permanente"+
                "\n"+
                f"\n-Exoneración del pago de primas por incapacidad total y permanente"            
            ))
        
        def monumaccpers_info():
            messagebox.showinfo("Accidentes Personales", (
                "Para cubrir el riesgo de fallecimiento accidental, así como los gastos médicos productos de un accidente."
            ))
        
        def monumaccpers_cover():
            messagebox.showinfo("Accidentes Personales", (
                "*** Coberturas ***"+
                "\n"+
                f"\nAdicional a la cobertura básica por fallecimiento accidental - Para cubrir el riesgo de fallecimiento accidental, así como los gastos médicos productos de un accidente."+
                "\n"+
                f"\nMuerte accidental simultánea cónyuge - Cubre un 25% adicional si en el mismo accidente fallece el titular y el cónyuge asegurado."+
                "\n"+
                f"\nIncapacidad total y permanente - Si por causa de un accidente dentro de la cobertura de la póliza se comprueba en forma irrefutable que existe incapacidad total y permanente para realizar su función productiva habitual, soló paga al asegurado la suma asegurada total."+
                "\n"+
                f"\nDesmembramiento - Si por causa de un accidente el asegurado pierde alguno de sus miembros o la vista de un ojo o ambos, La Compañía le cubre el porcentaje de la suma asegurada detallado en la póliza."+
                "\n"+
                f"\nGastos médicos y odontológicos - Si por causa de un accidente el asegurado requiere ser atendido por un médico, odontólogo o internarse en algún centro médico, La Compañía le cubre los gastos hasta el tope de la suma contratada."+
                "\n"+
                f"\nGastos funerarios - Le cubre los gastos asegurados por fallecimiento accidental y relativo a funeraria, hasta el tope de la suma contratada."+
                "\n"+
                f"\nRenta diaria por hospitalización - Esta cobertura le concede una renta diaria de acuerdo al plan contratado por cada 24 horas de internamiento en caso de que el asegurado sea ingresado en un centro médico a causa de un accidente."
            ))
            
        def monumaccpers_modes():
            messagebox.showinfo("Accidentes Personales", (
                "*** Modalidades ***"+
                "\n"+
                f"\n-Individual"+
                "\n"+
                f"\n-Familiar"+
                "\n"+
                f"\n-Vida diaria"+
                "\n"+
                f"\n-Viajes de negocios"+
                "\n"+
                f"\n-Sus vacaciones y las de su familia"
            ))
            
        def monumplanhogar_info():
            messagebox.showinfo("Plan Hogar", (
                "Es un plan diseñado para proteger las viviendas, este incluye las coberturas de Responsabilidad Civil y Asistencia Domiciliaria con el fin de garantizar su contenido y la tranquilidad de nuestros asegurados."
            ))
            
        def monumplanhogar_benefits():
            messagebox.showinfo("Plan Hogar", (
                "*** Beneficios ***"+
                "\n"+
                f"\nAsistencia Domicilaria - Asistencia en el hogar por eventualidades básicas tales como: Plomería, electricidad, cerrajería, entre otros."+
                "\n"+
                f"\nPlan Hogar Inquilino - Si su vivienda es alquilada, también puede contar con un plan de seguros para proteger todo el mobiliario y recuperar la inversión frente a siniestros que puedan presentarse afectando el contenido del hogar. Esta póliza incluye cobertura de Responsabilidad Civil y asistencia domiciliaria en el hogar."+
                "\n"+
                f"\nResponsabilidad Civil - Cobertura frente a daños ocasionales a terceros por daños a la propiedad ajena y por lesiones a personas por las cuales sea legalmente responsable el asegurado con un límite de RD$300,000.00 hasta RD$1,000,000.00."
            ))
            
        def monumplanhogar_cover():
            messagebox.showinfo("Plan Hogar", (
                "*** Cobertura ***"+
                "\n"+
                f"\n-Daños por humo"+
                "\n"+
                f"\n-Terremoto"+
                "\n"+
                f"\n-Explosión"+
                "\n"+
                f"\n-Motín, huelgas y/o daños maliciosos"+
                "\n"+
                f"\n-Incendio y/o rayo"+
                "\n"+
                f"\n-Orientación jurídica telefónica"+
                "\n"+
                f"\n-Daños por agua"+
                "\n"+
                f"\n-Huracán, ciclón, tornado y manga de viento"+
                "\n"+
                f"\n-Servicio doméstico por hospitalización"+
                "\n"+
                f"\n-Alojamiento por inhabilitación"+
                "\n"+
                f"\n-Robo con escalamiento y/o violencia al 100%"+
                "\n"+
                f"\n-Daños por naves aéreas y/o vehículos terrestres"+
                "\n"+
                f"\n-Colapso y/o daños a la estructuras 15% s/a y Remoción de escombros"+
                "\n"+
                f"\n-Asistencia domiciliaria (Plomeria, Eléctricidad, Cerrajería)"+
                "\n"+
                f"\n-Daños por agua de lluvia a consecuencia de huracán, ciclón, tornado y manga de viento, inundación y/o ras de mar"
            ))
        """   
        
        # monumental UI #
        """ Unused
        F4_Menu=LabelFrame(self.root,bg=bg_color)
        F4_Menu.place(x=0,y=267,width=925,height=24)   
        
        def f4_2():            
            F3_2.lift()
        
        def f4_3():
            F3_3.lift()
            
        def f4_4():
            F3_4.lift()
        
        def f4_5():
            F3_5.lift()
            
        def f4_6():
            F3_6.lift()
        
        def f4_1():
            F4.lift()
            
        F4_page1=Button(F4_Menu,text="1",command=f4_1,font="arial 12 bold").place(x=0,y=0,width=175,height=24)
        F4_page2=Button(F4_Menu,text="2",command=f3_2,font="arial 12 bold").place(x=175,y=0,width=172,height=24)
        F4_page3=Button(F4_Menu,text="3",command=f3_3,font="arial 12 bold").place(x=347,y=0,width=172,height=24)        
        F4_page4=Button(F4_Menu,text="4",command=f3_4,font="arial 12 bold").place(x=519,y=0,width=172,height=24)       
        F4_page5=Button(F4_Menu,text="5",command=f3_5,font="arial 12 bold").place(x=691,y=0,width=110,height=24)                
        F4_page6=Button(F4_Menu,text="6",command=f3_6,font="arial 12 bold").place(x=801,y=0,width=122,height=24)                

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Planes Monumental",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=0,y=290,width=925,height=260)
        
        monumentalvida_lbl=Label(F4,text="Plan Vida", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        monumentalvida_txt=Entry(F4, width=2,textvariable=self.esencial_plus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        monumentalvida_info1=Button(F4,text="Info.",command=monumplanvida_info,font="arial 12 bold").grid(row=0,column=2,padx=10,pady=10,sticky="w")
        monumentalvida_info2=Button(F4,text="Auxilia a Cubrir",command=monumplanvida_auxcover,font="arial 12 bold").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        monumentalvida_info3=Button(F4,text="Opciones",command=monumplanvida_options,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=10,sticky="w")        
        monumentalvida_info4=Button(F4,text="Coberturas",command=monumplanvida_cover,font="arial 12 bold").grid(row=0,column=5,padx=10,pady=10,sticky="w")                
        
        monumentalaccpers_lbl=Label(F4,text="Accidentes Personales", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        monumentalaccpers_txt=Entry(F4, width=2,textvariable=self.esencial_plus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        monumentalaccpers_info1=Button(F4,text="Info.",command=monumaccpers_info,font="arial 12 bold").grid(row=1,column=2,padx=10,pady=10,sticky="w")
        monumentalaccpers_info2=Button(F4,text="Cobertura",command=monumaccpers_cover,font="arial 12 bold").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        monumentalaccpers_info3=Button(F4,text="Opciones",command=monumaccpers_modes,font="arial 12 bold").grid(row=1,column=4,padx=10,pady=10,sticky="w")        

        monumentalplanhogar_lbl=Label(F4,text="Plan Hogar", font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        monumentalplanhogar_txt=Entry(F4, width=2,textvariable=self.esencial_plus,font=("times new roman",14,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        monumentalplanhogar_info1=Button(F4,text="Info.",command=monumplanhogar_info,font="arial 12 bold").grid(row=2,column=2,padx=10,pady=10,sticky="w")
        monumentalplanhogar_info2=Button(F4,text="Modalidades",command=monumplanhogar_benefits,font="arial 12 bold").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        monumentalplanhogar_info3=Button(F4,text="Cobertura",command=monumplanhogar_cover,font="arial 12 bold").grid(row=2,column=4,padx=10,pady=10,sticky="w")                
        """  
                  
    # selector de compania    
    
        F_Menu=LabelFrame(self.root,bg=bg_color)
        F_Menu.place(x=925,y=267,width=45,height=284)
        
        def all_humano():
            F2.lift()
            F2_Menu.lift()
            
        def all_atlantica():
            F3.lift()
            F3_Menu.lift()
        """ Unused button 
        def all_monumental():
            F4.lift()
            F4_Menu.lift()
        """
        
        F_Hum=Button(F_Menu,text="Humano",command=all_humano,font="arial 7 bold").place(x=0,y=0,width=45,height=134)
        F_Atlan=Button(F_Menu,text="Atlantica",command=all_atlantica,font="arial 7 bold").place(x=0,y=135,width=45,height=143)
        
        """ Unused button
        F_Monum=Button(F_Menu,text="Monum.",command=all_monumental,font="arial 7 bold").place(x=0,y=142,width=45,height=71)        
        F_ARS=Button(F_Menu,text="ARS",command=f2_4,font="arial 9 bold").place(x=0,y=213,width=45,height=71)    
        """    
    
    # Area de facturas #
    
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=970,y=169,width=380,height=525)
        bill_title=Label(F5,text="Área de facturas",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
    # Menu Button Frame #
    
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Menú de factura",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=550,width=975,height=146)

        btn_F=Frame(F6,bg=bg_color)
        btn_F.place(x=5,y=10,width=750,height=81)
        
        total_btn=Button(btn_F,command=self.bill_area,text="Generar",bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Guardar",command=self.save_bill,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Limpiar",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Salir",command=self.Exit_app,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=4,padx=5,pady=5)
        folder_btn=Button(btn_F,text="Ver Facturas",command=self.see_bills,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)        
        self.welcome_bill()
        
    # functionality #
    
    def total(self):
        # individual product 1 prices
        self.hp_esencialplus_p=self.esencial_plus.get()*1640
        self.hp_superior_p=self.superior.get()*2180
        self.hp_royal_p=self.royal.get()*2760
        self.hp_max_p=self.max.get()*3530
        self.hp_prime_p=self.prime.get()*6480
        self.hp_platinum_p=self.platinum.get()*9880
        # total product 1 prices        
        self.total_product1_price=float(
            self.hp_esencialplus_p+
            self.hp_superior_p+
            self.hp_royal_p+
            self.hp_max_p+
            self.hp_prime_p+
            self.hp_platinum_p
        )   
        self.product1_price.set("DOP. "+str(self.total_product1_price))
        self.product1_tax.set("DOP. "+str(round((self.total_product1_price*0.18),2)))
        
        # Total $$
        self.total_price=float(
            self.total_product1_price
        )
        
        self.tax_total=float(
            round(self.total_product1_price*0.18, 2)
        )
        
        self.total_total=float(
            self.total_price+self.tax_total
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tSJ Asesores de Seguros")    
        self.txtarea.insert(END,'\n\t\tSANTIAGO')
        self.txtarea.insert(END,f"\n\t\tTEL. 18096574208")        
        self.txtarea.insert(END,"\n")
        self.txtarea.insert(END,f"\nFecha : {self.date.get()} ")
        self.txtarea.insert(END,f"\nNro. de factura : {self.bill_no.get()} ")
        self.txtarea.insert(END,f"\nNombre : {self.c_name.get()} ")
        self.txtarea.insert(END,f"\nNro. telefónico : {self.c_phone.get()} ")
        self.txtarea.insert(END,"\n")        
        self.txtarea.insert(END,f"==========================================")
        self.txtarea.insert(END,"\nSERVICIOS")        
        self.txtarea.insert(END,"\n")        
        self.txtarea.insert(END,f"==========================================")
        
    def finish_bill(self):
        self.txtarea.insert(END,f"\n------------------------------------------")
        self.txtarea.insert(END,f"\n Forma de pago : {self.paym.get()}")
        self.txtarea.insert(END,f"\n Monto\t\tDOP. {self.bamnt.get()}")                           
        self.txtarea.insert(END,f"\n------------------------------------------")
        
    def save_bill(self):        
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        op=messagebox.askyesno("Guardar factura", "¿Quieres guardar esta factura?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("facturas/"+str(self.c_name.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            f = open("facturas/"+str(self.c_name.get())+".txt","r")
            for x in f:
                pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
            pdf.output(f"facturas/pdf/{self.c_name.get()}.pdf")
            messagebox.showinfo("Guardado", f"Factura nro. : {self.bill_no.get()} guardada correctamente")
        else:
            return
        
    def find_bill(self):
        present="no"
        for i in os.listdir("facturas/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"facturas/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Nombre de factura incorrecto")
        
    def clear_data(self):
        op=messagebox.askyesno("Limpiar","¿Deseas limpiar todas las casillas?")
        if op>0:
            # productos humano #
            self.esencial_plus.set(0)
            self.superior.set(0)
            self.royal.set(0)
            self.max.set(0)
            self.prime.set(0)
            self.platinum.set(0)        
            self.miautobasico.set(0)   
            self.miautopremier.set(0)   
            self.miautoflex.set(0)
            self.miautomotobasico.set(0)
            self.miautofull.set(0) 
            # productos atlantica #
            self.orion.set(0) 
            self.orion_plus.set(0) 
            self.guardian.set(0) 
            self.guardian_plus.set(0) 
            self.vida_credito.set(0) 
            self.vida_beca.set(0) 
            self.vida_grupo.set(0) 
            self.acc_pers.set(0) 
            self.autoatlanta_basico.set(0) 
            self.autoatlanta_ultra.set(0) 
            self.atlantico_rentacar.set(0) 
            self.atlantico_total.set(0) 
            self.atlantico_totalplus.set(0)
            self.atlanta_vip.set(0) 
            self.atlanta_0km.set(0) 
            self.atlanta_seriem.set(0) 
            self.atlanta_economax.set(0) 
            self.atlanta_taxirenta.set(0) 
            self.motoresatlanta_basico.set(0) 
            self.motoresatlanta_deportivo.set(0) 
            self.motoresatlanta_totalplus.set(0) 
            # product total price #
            self.product1_price.set("")
            self.product2_price.set("")
            self.product3_price.set("")
            # product tax #
            self.product1_tax.set("")
            self.product2_tax.set("")
            self.product3_tax.set("")
            # cliente #
            self.c_name.set("")
            self.c_phone.set("")
            x=random.randint(1000,9999) 
            self.bill_no.set(x)
            self.search_bill.set("")
            self.paym.set("")
            self.date.set("")
            self.bamnt.set("")
            self.welcome_bill()
        
    def bill_area(self):
        self.total()
        self.welcome_bill() ##format starter
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error", "No se introdujeron los detalles del cliente.")
        else:
    # display prices
            #products1 humano
            if self.esencial_plus.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Plan Esenc. Plus\t\t{self.esencial_plus.get()}")
            if self.superior.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Plan Superior\t\t{self.superior.get()}")
            if self.royal.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Plan Royal\t\t{self.royal.get()}")
            if self.max.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Plan Max\t\t{self.max.get()}")
            if self.prime.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Plan Prime\t\t{self.prime.get()}")
            if self.platinum.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Plan Platinum\t\t{self.platinum.get()}")                        
            if self.miautobasico.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Mi Auto Motor Básico\t\t{self.miautobasico.get()}")
            if self.miautopremier.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Mi auto Premier\t\t{self.miautopremier.get()}")
            if self.miautoflex.get()!=0:
                self.txtarea.insert(END, f"\n Humano: Mi Auto Flex\t\t{self.miautoflex.get()}")
            if self.miautomotobasico.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Mi Auto Motor Básico\t\t{self.miautomotobasico.get()}")
            if self.miautofull.get()!=0:
                self.txtarea.insert(END,f"\n Humano: Mi Auto Full\t\t{self.miautofull.get()}")
            #products2 atlantica
            if self.orion.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Orion\t\t{self.orion.get()}")
            if self.orion_plus.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Orion Plus\t\t{self.orion_plus.get()}")    
            if self.guardian.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Guardian\t\t{self.guardian.get()}")
            if self.guardian_plus.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Guardian Plus\t\t{self.guardian_plus.get()}")
            if self.vida_credito.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Vida Crédito\t\t{self.vida_credito.get()}")
            if self.vida_beca.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Vida Beca\t\t{self.vida_beca.get()}")
            if self.vida_grupo.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Vida Grupo\t\t{self.vida_grupo.get()}")
            if self.acc_pers.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Accidentes Personales\t\t{self.acc_pers.get()}")
            if self.autoatlanta_basico.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Auto Básico\t\t{self.autoatlanta_basico.get()}")
            if self.autoatlanta_ultra.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Auto Ultra\t\t{self.autoatlanta_ultra.get()}")
            if self.atlantico_rentacar.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Rent-a-Car\t\t{self.atlantico_rentacar.get()}")
            if self.atlantico_total.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Total\t\t{self.atlantico_total.get()}")
            if self.atlantico_totalplus.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Total Plus\t\t{self.atlantico_totalplus.get()}")
            if self.atlanta_vip.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: VIP\t\t{self.atlanta_vip.get()}")
            if self.atlanta_0km.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: 0KM\t\t{self.atlanta_0km.get()}")
            if self.atlanta_seriem.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Serie M\t\t{self.atlanta_seriem.get()}")
            if self.atlanta_economax.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Econo Max\t\t{self.atlanta_economax.get()}")
            if self.atlanta_taxirenta.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Taxi/Renta\t\t{self.atlanta_taxirenta.get()}")
            if self.motoresatlanta_basico.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Motores Básico\t\t{self.motoresatlanta_basico.get()}")
            if self.motoresatlanta_deportivo.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Motores Deportivo\t\t{self.motoresatlanta_deportivo.get()}")
            if self.motoresatlanta_totalplus.get()!=0:
                self.txtarea.insert(END,f"\n Atlántica: Total Plus\t\t{self.motoresatlanta_totalplus.get()}")
            #informal
            if self.healthplan.get()!=0:
                self.txtarea.insert(END,f"\n Plan de Salud\t\t{self.healthplan.get()}")
            #back to bill
            self.finish_bill()              
            
    def Exit_app(self):
        op=messagebox.askyesno("Salir","¿Deseas cerrar la aplicación?")
        if op>0:
            self.root.destroy()
            
    def see_bills(self):
        subprocess.Popen('explorer "facturas"')    

root=Tk()
obj = Bill_App(root)
root.mainloop()