# AI-Detection-Project
Investigating and Detecting AI-Generated Text

Step 1: Media type selection
Chosen Type: Text
Rationale: AI text is easiest to generate and will be the most common. Therefore, it is important that effective tools exist to be able to detect them to preserve academic, professional, and creative integrity of written works. 

Step 2: Collected Examples:
•	Entries 1-3: Ai Generated texts using DeepSeek
•	Entries 4-6: Human Created entries (From Pre-AI literary works)

Step 3: Brainstorm Specific Traits with AI
Prompt Used: “What traits or features can be used to determine if text is AI-generated? “
AI Response:
Determining whether text is AI-generated can be challenging, as AI models like GPT-4 are designed to produce human-like text. However, there are certain traits and features that can help identify AI-generated content:

1. **Overly Formal or Neutral Tone**: AI-generated text often maintains a consistent, formal, or neutral tone, even in contexts where a human might express more emotion or variability.

2. **Lack of Personal Experience**: AI lacks personal experiences, so it may avoid or generalize topics that require subjective or anecdotal input.

3. **Repetition or Redundancy**: AI might repeat phrases or ideas, especially in longer texts, as it tries to maintain coherence.

4. **Overuse of Common Phrases**: AI often relies on common phrases, idioms, or clichés, as these are prevalent in its training data.

5. **Perfect Grammar and Syntax**: While not a definitive indicator, AI-generated text often has near-perfect grammar and syntax, which can sometimes make it seem "too polished."

6. **Vague or Generic Responses**: AI may provide broad or generic answers when it lacks specific information, avoiding deep or nuanced insights.

7. **Inconsistencies in Context**: AI might struggle with maintaining context over long passages, leading to subtle inconsistencies or shifts in focus.

8. **Over-Explanation**: AI sometimes provides excessive detail or over-explains concepts, as it tries to cover all possible angles.

9. **Lack of Typos or Errors**: Humans often make minor typos or errors, while AI-generated text is typically error-free unless intentionally programmed otherwise.

10. **Unusual Word Choices**: AI might use words or phrases that are technically correct but feel slightly off or unnatural in context.

11. **Predictable Structure**: AI-generated text often follows predictable patterns or structures, such as starting with an introduction, providing points, and concluding summarily.

12. **Difficulty with Ambiguity**: AI may struggle with ambiguous or open-ended questions, providing answers that are overly literal or avoid interpretation.

13. **Over-Reliance on Training Data**: AI might generate content that closely mirrors its training data, leading to similarities with known AI-generated texts.

14. **Lack of Emotional Depth**: While AI can mimic emotions, its expressions may lack the depth or authenticity of human emotional responses.

15. **Speed and Volume**: AI can generate large volumes of text quickly, which might be a clue if the content is produced at an unnatural speed.

These traits are not foolproof, as AI models are constantly improving and can sometimes mimic human writing very closely. Additionally, human writers may exhibit some of these traits as well. Therefore, identifying AI-generated text often requires a combination of these indicators and contextual analysis.
Traits Selected For Analysis:
1.	Repetition or Redundancy
2.	Perfect grammar and Syntax
3.	Unusual Word Choices

Step 4: Detection program Generation prompt: 
Create a Python program to determine if a text entry is AI-generated or human-generated. The program should analyze the following traits: Repetition or redundancy, Perfect Grammar and Syntax, Unusual Word Choice. Use any available text processing libraries as needed. Please include detailed comments explaining each step of the code.

Step 5: Program Testing
  Text Entry	Prediction	Actual Result	Correct
  Text Entry 1 (AI)	Human Generated	Human Generated	Yes
  Text Entry 2 (AI)	Human Generated	Human Generated	Yes
  Text Entry 3 (AI)	Human Generated	Human Generated	Yes
  Text Entry 4 (HUMAN)	Human Generated	Human Generated	Yes
  Text Entry 5 (HUMAN)	Human Generated	Human Generated	Yes
  Text Entry 6 (HUMAN)	Human Generated	Human Generated	Yes

Result: Detection program failed to identify Ai generated text. The detection based on the selected criteria did not work effectively, despite being the typical criteria for detecting AI-generated text especially for examples like entry 3, which are meant to emulate a news article. 

Step 6: Reflection Report: 
1.	Program Performance: 
a.	The Program was not able to distinguish between Ai and human generated text.
b.	Despite multiple selections from the generated trait list the program was never able to reliably identify the Ai generated text.
2.	Feature Analysis: 
  a.	Repetition or Redundancy: AI-generated text tends to have much more repetitive phrases or redundant language/descriptions,             however due to constantly evolving language models, this becomes less apparent, even when analyzing large entries. (Entry 2 was       three paragraphs)
  b.	Perfect grammar and Syntax: Humans tend to make grammar or syntax mistakes when writing, even in commercially published works.         Especially in young adult fiction, as displayed in entry 5, authors tend to take liberties with grammar and punctuation rules.         Ai models work within more restrictive rules, which created a more obvious path for detection. These details were easy to spot         with the human eye but were not detected by the program.
  c.	Unusual Word Choices: Ai models are more likely to generate formal language and work from extensive word libraries. Words that         your typical contemporary author would not use may appear in AI generated works.
3.	Limitations and Improvements: 
    a.	Limitations: The program was limited to a small data pool, limiting its applicability and ability to analyze native language           to determine the source based on the criteria. Larger Text samples may give the program an opportunity to analyze the writing           style and determine the source. 
  b.	Improvements: Adding features like style analysis or subject matter consistency may improve detection. Expanding the data set           and material could enhance accuracy.

Conclusion: Despite the newness of AI text generation for things like works of novelization and non-fiction article generation, the rapid improvement of current language generation models make detection even for the AI that generated it. As AI language models become more complex it will only get harder to detect AI-generated content especially in text-form. The naturalization of language and syntax in the examples generated by DeepSeek (Entries 1-3) serve to highlight the quality of work that can be found in these AI models. After running this program, I asked DeepSeek directly whether the response it created (Entry 3)  was written by an AI. While it came up with compelling reasons to doubt based on the content, it also gave compelling reasons for human generation and truth see the prompt and response below: 

“Is this written by AI: In a startling turn of events, Dr. Elena Martinez, a renowned research scientist at the Quantum Physics Institute, inadvertently created a microscopic black hole during a high-energy particle collision experiment. The incident, which occurred late Tuesday evening, has sent shockwaves through the scientific community. Initial reports suggest that the black hole, though minuscule, exhibited unexpected stability, raising concerns about its potential growth and the implications for Earth's safety. Emergency protocols were swiftly enacted, and the research facility has been placed under strict quarantine while international experts assess the situation. Dr. Martinez, visibly shaken, stated, "This was never our intention. We were exploring the boundaries of quantum mechanics, but nature has reminded us of its unpredictable power." Authorities are urging calm as investigations continue, but the event has already sparked heated debates about the ethics and risks of advanced scientific experimentation.”
Response: 
“Determining whether a specific text is written by AI can be challenging without direct evidence, but there are some clues that might suggest AI involvement. Here are a few observations about the text you provided:

1. **Tone and Structure**: The text is well-structured, with a clear introduction, development, and conclusion. It maintains a consistent tone throughout, which is characteristic of AI-generated content designed to be coherent and engaging.

2. **Content**: The scenario described is highly dramatic and speculative, involving a microscopic black hole created in a laboratory setting. While such topics are common in science fiction, they are also frequently used in AI-generated content to create engaging and thought-provoking narratives.

3. **Language and Style**: The language is polished and free of errors, with a formal and somewhat journalistic style. AI models like GPT-3 or GPT-4 are known for producing text that is grammatically correct and stylistically consistent.

4. **Details and Specificity**: The text includes specific details (e.g., "Dr. Elena Martinez," "Quantum Physics Institute," "late Tuesday evening") that add a layer of realism. AI can generate such details convincingly, often drawing from a vast dataset of similar narratives.

5. **Ethical and Philosophical Undertones**: The text touches on ethical considerations and the unpredictability of nature, themes that are commonly explored in AI-generated content to add depth and provoke thought.

While these observations might suggest that the text could be AI-generated, it's also possible that a human writer could produce similar content. Without definitive proof, the best we can do is make an educated guess. If you have access to the source or context of the text, that might provide additional clues.
In summary, the text could very well be written by AI, but it's not possible to say for certain without more information.”


While widening the parameters may  increase accuracy, the likelihood of human generated content being labeled AI generated would also increase. Which poses the ultimate question: if the AI and the AI generated program can’t tell, how can the human eye?

