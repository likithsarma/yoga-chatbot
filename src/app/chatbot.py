from .retriever import Retriever

class YogaChatBot:
    def __init__(self):
        self.retriever=Retriever()
    
    def get_response(self,query):
        answer = self.retrever.searh_answer(query) #ask retriever to find related answer
        if answer is None:
            return "Try asking me about yoga routines,categories, or app features!"
        return answer



