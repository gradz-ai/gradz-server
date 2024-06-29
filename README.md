# Gradz Server
This is project is a server that evaluates the writing task of the Telc A2-B1 exam. It is using RAG models to evaluate the text and provide recommended corrections.

```                 
## Installation                     
1. Clone the repository
2. Install the required packages using the following command
```bash
pip install -r requirements.txt
```
### Usage
The API has the following endpoint:  
POST /score: Check the correctness of the letter and assign a score.

sample payload:
```json
{
    "query": "Liebe Frau Martina Winkle,\n\nvielen Dank für die Einladung zum Kindergartenfest.\nÜber eine Teilnahme würde ich mich sehr freuen.\n Wenn möglich, möchte ich, dass\nmeine Schwester, mein Freund und mein Nachbar\nmitkommen.\n\nHerzliche Grüße\nBasel Mzarzaa"}