from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

class IndexManager:
    def __init__(self, index_dir):
        self.index_dir = index_dir
        self.index = None
        self.storage_context = None

    def load_or_create_index(self, documents=None):
        try:
            # Attempt to load the index from storage
            self.storage_context = StorageContext.from_defaults(persist_dir=self.index_dir)
            self.index = load_index_from_storage(self.storage_context)
        except Exception as e:
            print(f"Loading index failed: {e}. Initializing new index.")
            if documents is not None:
                # Create a new index from documents if provided
                self.index = VectorStoreIndex.from_documents(documents)
                self.index.storage_context.persist(persist_dir=self.index_dir)
                self.storage_context = self.index.storage_context
            else:
                raise ValueError("Documents must be provided to create a new index.")

    def get_index(self):
        if self.index is None:
            raise ValueError("Index is not initialized. Please load or create the index first.")
        return self.index
