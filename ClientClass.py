class ClientInfo:
    def __init__(self):
        self.Name = ''                  #имя фамилия
        self.Link = ''                  #ссылка на профиль
        self.Promotion = ''             #сеть продвижения
        self.Product = ''               #продукт
        self.NumRequests = ''           #кол-во заявок
        self.BringToPay = ''            #как доводит до оплаты
        self.Disadvntgs = ''            #нехватки для доведения до оплаты
        self.TaplinkType = ''           #тип таплинка
        self.Deadline = ''              #срок готовности таплинка
        self.Budget = ''                #бюджет на создание таплинка
        self.Target = ''                #цель для таплинка
        self.Emotions = ''              #эмоции, вызываемые таплинком
        self.Blocks = ''                #блоки информации на таплинке
        self.Funtional = ''             #функционал таплинка
        self.Payment = ''               #необходимость в платёжной системе
        self.ActualStage = 1
        self.IsChanging = False
        self.isAllowedAccept = False

    def inc_stage(self):
        self.ActualStage = self.ActualStage + 1        
    def dec_stage(self):
        self.ActualStage = self.ActualStage - 1
    def get_stage(self):
        return self.ActualStage
    
    def set_name(self,Name):
        self.Name = Name
    def get_name(self):
        return self.Name
    
    def set_link(self,Link):
        self.Link = Link 
    def get_link(self):
        return self.Link
    
    def set_promotion(self,Promotion):
        self.Promotion = Promotion 
    def get_promotion(self):
        return self.Promotion
    
    def set_product(self,Product):
        self.Product = Product
    def get_product(self):
        return self.Product
    
    def set_numreq(self,NumRequests):
        self.NumRequests = NumRequests
    def get_numreq(self):
        return self.NumRequests
    
    def set_paybring(self,BringToPay):
        self.BringToPay = BringToPay
    def get_paybring(self):
        return self.BringToPay
    
    def set_disadv(self,Disadvntgs):
        self.Disadvntgs = Disadvntgs
    def get_disadv(self):
        return self.Disadvntgs
    
    def set_taplinktype(self,TaplinkType):
        self.TaplinkType = TaplinkType
    def get_taplinktype(self):
        return self.TaplinkType
    
    def set_deadline(self,Deadline):
        self.Deadline = Deadline
    def get_deadline(self):
        return self.Deadline
    
    def set_budget(self,Budget):
        self.Budget = Budget
    def get_budget(self):
        return self.Budget
    
    def set_target(self,Target):
        self.Target = Target 
    def get_target(self):
        return self.Target
    
    def set_emotions(self,Emotions):
        self.Emotions = Emotions
    def get_emotions(self):
        return self.Emotions
    
    def set_blocks(self,Blocks):
        self.Blocks = Blocks
    def get_blocks(self):
        return self.Blocks
    
    def set_functional(self,Funtional):
        self.Funtional = Funtional
    def get_functional(self):
        return self.Funtional
    
    def set_payment(self,Payment):
        self.Payment = Payment
    def get_payment(self):
        return self.Payment
    
    def allow_accept(self):
        self.isAllowedAccept = True
    def disable_accept(self):
        self.isAllowedAccept = False
