from llama_index.core import SimpleDirectoryReader

class DocumentLoader:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_documents(self):
        return SimpleDirectoryReader(self.data_dir).load_data()
