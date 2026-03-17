class DataProcessor: 
   def __init__(self): 
       self.data = [] 
 
   def add_number(self, number): 
       if not isinstance(number, int): 
           raise ValueError("Ожидается целое число") 
       self.data.append(number) 
 
   def add_text(self, text): 
       if not isinstance(text, str): 
           raise ValueError("Ожидается строка") 
       self.data.append(text) 
 
   def get_sum(self): 
       return sum(x for x in self.data if isinstance(x, int)) 
 
   def get_texts(self): 
       return [x for x in self.data if isinstance(x, str)] 

 