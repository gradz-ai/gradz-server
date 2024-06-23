
from llama_index.llms.openai import OpenAI
class QueryEngine:
    def __init__(self, index):
        self.index = index

    def query(self, query_text):
        # gpt35_llm = OpenAI(model="gpt-3.5-turbo")
        # gpt4_llm = OpenAI(model="gpt-4")
        gpt_4o = OpenAI(model="gpt-4o", temperature=0, max_tokens=100, top_p=0.9, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"])

        # modify the query engine to give more eloborate responses
        query_engine = self.index.as_query_engine(llm =gpt_4o)
        return query_engine.query(query_text)
