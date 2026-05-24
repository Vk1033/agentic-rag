from dotenv import load_dotenv

load_dotenv()

from graph.graph import app  # noqa: E402

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "agent memory?"}))
