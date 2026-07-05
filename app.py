import streamlit as st
import ollama
import re

st.title("AI Interview Coach")

if "history" not in st.session_state:
    st.session_state.history = []

topic = st.selectbox(
    "Choose Interview Topic",
    ["python", "SQL", "Machine learning", "Deeplearning", "GenAI"]
)

#Generate Question

if st.button("Generate Question"):

    response = ollama.chat(
        model = 'llama3.2:3b',
        messages=[
            {
                'role':'user',
                'content': f'Generate one interview question on {topic}'
            }
        ]
    )
    question = response['message']['content']

    st.session_state["question"] = question
    st.write("### Question")
    st.write(question)

#show question again
if "question" in st.session_state:

    st.write("### Current Question")
    st.write(st.session_state["question"])

    answer = st.text_area(
        "Enter your answer"
    )

    if st.button("Evaluate Answer"):

        prompt = f"""
        You are a senior technical interviewer.

        Interview Questions:
        {st.session_state["question"]}

        Candidate Answer:
        {answer}
        
        Evaluate and provide:

        1. Score out of 10
        2. Strengths
        3. Weaknesses
        4. Improvements
        5. Ideal Answer
        """

        evaluation = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role":"user",
                    "content": prompt
                }
            ]
        )

        
        result = evaluation["message"]["content"]

        score_match = re.search(
            r"(\d+)\s*/\s*10",
            result
        )
        if score_match:
            score = int(score_match.group(1))
        else:
            score = 0    

        st.write("### Evaluation")
        st.write(result)

        #save history
        st.session_state.history.append(
            {
                "question" : st.session_state["question"],
                "answer": answer,
                "evaluation": result,
                "score": score
            }
        )

        if len(st.session_state.history)>0:

            scores = [
                item["score"]
                for item in st.session_state.history
            ]

            total_questions = len(scores)

            avg_score = round(
                sum(scores)/total_questions,
                2
            )

            max_score = max(scores)
            min_score = min(scores)

            st.subheader("Interview Dashboard")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "questions",
                total_questions
            )

            col2.metric(
                "Average",
                avg_score
            )

            col3.metric(
                "Highest",
                max_score
            )

            col4.metric(
                "Lowest",
                min_score
            )
        #show interview history 
        st.subheader("Interview History")
        for item in st.session_state.history:
            st.write(" ### Question")
            st.write(item["question"])

            st.write("### Your Answer")
            st.write(item["answer"])

            st.write("### Evaluation")
            st.write(item["evaluation"])

            st.markdown("-----")






