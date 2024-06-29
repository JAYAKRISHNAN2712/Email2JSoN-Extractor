from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pydantic import BaseModel

# LLM class handles the extraction of email tags in the form of Key-Value pair.
class LLM():
    # initializing llama 3 instance
    def __init__(self, email:str):

        self.llm = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct", max_length=512,huggingfacehub_api_token="HUGGINGFACE-API-KEY")
        self.email = email
     
    # importing prompt
    def Prompt():
        
        prompt = """You are an email extractor bot.
                You are required to extract the values of 'From', 'To', 'Cc', 'Bcc', 'Date', 'Time' and 'Subject' from the email.
                You are also required to extract the values of 'Body' and summarize it.
                email : {email}
                Return the result in JSON format. Do not generate additional dialogues or any explanation.
                Return the JSON in the following format:
                
                    "From": "sender",
                    "To": "recipient",
                    "Cc": "cc",
                    "Bcc": "bcc",
                    "Date": "email_date",
                    "Time": "email_time",
                    "Subject": "email_subject",
                    "Body": "email_body",
                    "Summary": "email_summary"
                
                """
        return prompt
    
    # Chat Template for extraction.
    def ChatTemplate(self,prompt:str = Prompt()):
    
        messages = [
            SystemMessage(content="""You are an helpful assistant"""),
            HumanMessage(content=prompt.format(email=self.email)),
            AIMessage(content='')
        ]
        
        return self.llm.invoke(messages)
