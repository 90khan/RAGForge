from memory.memory_manager import MemoryManager


memory = MemoryManager()

memory.add_user(
    "What is RAG?"
)

memory.add_assistant(
    "RAG stands for Retrieval Augmented Generation."
)

memory.add_user(
    "Explain it simply."
)

print(memory.get_context())