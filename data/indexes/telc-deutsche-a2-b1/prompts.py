few_shot_prompt = """
Q: "how much score will I get for question 31 based in this answer, give me the exact numbers with explanation:\n\nLiebe Frau Martina Winkle,\n\nvielen Dank für die Einladung zum Kindergartenfest.\nÜber eine Teilnahme würde ich mich sehr freuen.\nIch kann Kindergesichter schminken,\ndas Talent habe ich.\n\nIch hoffe du magst es. Ich werde auch ein leckeres\nDessert mitbringen. Wenn möglich, möchte ich, dass\nmeine Schwester, mein Freund und mein Nachbar\nmitkommen.\n\nHerzliche Grüße\nBasel Mzarzaa"
A: Criteria for Evaluation:
Inhaltliche Angemessenheit (Content Appropriateness):

Does the response address the topic?
Your response acknowledges the invitation, expresses joy in participating, mentions face painting, and brings a dessert, indicating good alignment with the invitation's context.
Score: B1 (Fully meets the topic requirements)
Kommunikative Aufgabenbewältigung (Communicative Task Achievement):

How well does the response handle the communicative task?
The letter is polite, mentions specific activities (face painting, bringing a dessert), and includes personal touches (inviting family and friends).
Score: B1 (Good handling of the task)
Sprachliche Angemessenheit (Linguistic Appropriateness):

Language level, correctness, and appropriateness.
The language used is simple but correct, with appropriate vocabulary for the context.
Score: B1 (Good language usage)
Detailed Breakdown:
Inhaltliche Angemessenheit:

You responded to the invitation correctly and provided relevant information about your participation.
Points: 3/3 (B1)
Kommunikative Aufgabenbewältigung:

The response is polite and clear, with good task handling.
Points: 3/3 (B1)
Sprachliche Angemessenheit:

Your letter has appropriate vocabulary and is grammatically correct for the B1 level.
Points: 3/3 (B1)
Total Score for Question 31:
Content Appropriateness: 3 points
Communicative Task Achievement: 3 points
Linguistic Appropriateness: 3 points
Total: 9/9 points

Explanation:
Your answer fully meets the requirements for a B1 level in all three criteria:

It addresses the invitation appropriately.
It handles the communicative task well by being polite and including relevant details.
It uses appropriate and correct language for the B1 level.
Thus, you would score 9 out of 9 points for question 31.

Q: {question}
A: """


def rag_query(question):
    # Retrieve relevant documents from the index
    retrieved_docs = index.query(question, top_k=3)

    # Create the few-shot prompt with retrieved documents
    few_shot_examples = "\n".join([f"Q: {doc}\nA: {retrieved_docs[doc]}" for doc in retrieved_docs])
    prompt = few_shot_prompt.format(question=question)
    full_prompt = few_shot_examples + prompt

    # Use OpenAI's GPT to generate an answer
    response = openai.Completion.create(
        engine="davinci",
        prompt=full_prompt,
        max_tokens=50
    )









